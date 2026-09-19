"""Deterministic compiler for secure Gemini agent blueprints.

This module deliberately has no Google SDK dependency. It validates and renders
portable builder artifacts; network/model execution remains an adapter concern.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import json
import re
from typing import Any, Mapping


PLATFORMS = frozenset({"desktop-python", "android-kotlin", "hybrid"})
RISK_LEVELS = frozenset({"low", "medium", "high", "critical"})
SENSITIVE_TOOL_WORDS = re.compile(r"(sms|call|payment|transfer|delete|purchase|shell|exec|chmod|sudo|iam|firewall)", re.I)
SECRET_VALUE_WORDS = re.compile(r'''(?:["']?)(?:api[_-]?key|token|secret|password)(?:["']?)\s*[:=]\s*["']?[^"$'\s},]+''', re.I)


@dataclass(frozen=True)
class ToolBlueprint:
    name: str
    description: str
    permission: str = "read"
    requires_approval: bool = False

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]{1,63}", self.name):
            errors.append(f"invalid tool name: {self.name!r}")
        if not self.description.strip():
            errors.append(f"tool {self.name!r} has empty description")
        if self.permission not in {"read", "local-write", "external-write", "system"}:
            errors.append(f"tool {self.name!r} has unsupported permission")
        dangerous = bool(SENSITIVE_TOOL_WORDS.search(self.name + " " + self.description))
        if dangerous and not self.requires_approval:
            errors.append(f"tool {self.name!r} is consequential and requires approval")
        return errors


@dataclass(frozen=True)
class AgentBlueprint:
    name: str
    platform: str
    model: str
    instruction: str
    tools: tuple[ToolBlueprint, ...] = ()
    memory: str = "session"
    approval_mode: str = "consequential"
    secret_ref: str | None = None
    private_network_only: bool = True
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.name.strip():
            errors.append("agent name is required")
        if self.platform not in PLATFORMS:
            errors.append(f"unsupported platform: {self.platform}")
        if not self.model.strip():
            errors.append("model is required")
        if not self.instruction.strip():
            errors.append("instruction is required")
        if self.memory not in {"session", "long-term", "none", "local-rag"}:
            errors.append(f"unsupported memory mode: {self.memory}")
        if self.approval_mode not in {"never", "consequential", "always"}:
            errors.append(f"unsupported approval mode: {self.approval_mode}")
        if not self.secret_ref and self.platform in {"desktop-python", "android-kotlin", "hybrid"}:
            errors.append("secret_ref must point to a secret reference; plaintext credentials are forbidden")
        for tool in self.tools:
            errors.extend(tool.validate())
        raw = json.dumps(self.metadata, ensure_ascii=False)
        if SECRET_VALUE_WORDS.search(raw):
            errors.append("metadata appears to contain a plaintext secret")
        return errors

    def to_manifest(self) -> dict[str, Any]:
        errors = self.validate()
        if errors:
            raise ValueError("; ".join(errors))
        return {
            "schema_version": "1",
            "name": self.name,
            "platform": self.platform,
            "model": self.model,
            "instruction": self.instruction,
            "memory": self.memory,
            "approval_mode": self.approval_mode,
            "secret_ref": self.secret_ref,
            "private_network_only": self.private_network_only,
            "tools": [
                {
                    "name": t.name,
                    "description": t.description,
                    "permission": t.permission,
                    "requires_approval": t.requires_approval,
                }
                for t in self.tools
            ],
            "metadata": dict(self.metadata),
        }


def compile_blueprint(spec: AgentBlueprint) -> dict[str, str]:
    """Return portable builder artifacts after deterministic validation."""
    manifest = spec.to_manifest()
    name = re.sub(r"[^a-z0-9]+", "_", spec.name.lower()).strip("_") or "gemini_agent"

    adk_yaml = render_adk_yaml(spec)
    python_stub = render_python_scaffold(spec, name)
    kotlin_stub = render_kotlin_scaffold(spec, name)
    manifest_json = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    return {
        "manifest.json": manifest_json,
        "root_agent.yaml": adk_yaml,
        f"{name}_desktop.py": python_stub,
        f"{name}_android.kt": kotlin_stub,
    }


def render_adk_yaml(spec: AgentBlueprint) -> str:
    spec.to_manifest()
    tool_lines = "\n".join(
        f"  - name: {t.name}\n    description: {json.dumps(t.description, ensure_ascii=False)}"
        for t in spec.tools
    ) or "  []"
    instruction = spec.instruction.replace("\n", "\n  ")
    return (
        f"name: {spec.name.lower().replace(' ', '_')}\n"
        f"model: {spec.model}\n"
        f"description: {spec.name}\n"
        f"instruction: |\n  {instruction}\n"
        f"tools:\n{tool_lines}\n"
    )


def render_python_scaffold(spec: AgentBlueprint, module_name: str) -> str:
    spec.to_manifest()
    return f'''"""Generated Gemini desktop adapter for {spec.name}.

Execution is intentionally isolated from blueprint generation.
Provide credentials through the configured secret reference: {spec.secret_ref}.
"""
from __future__ import annotations

from google import genai

MODEL = {spec.model!r}
SECRET_REF = {spec.secret_ref!r}


def create_client() -> genai.Client:
    """Create a client using an environment/secret-manager adapter.

    Do not hard-code credentials here. Inject the credential outside source control.
    """
    return genai.Client()


def build_config() -> dict:
    return {{
        "model": MODEL,
        "memory": {spec.memory!r},
        "approval_mode": {spec.approval_mode!r},
        "private_network_only": {spec.private_network_only!r},
        "tools": {[t.name for t in spec.tools]!r},
    }}
'''


def render_kotlin_scaffold(spec: AgentBlueprint, class_name: str) -> str:
    spec.to_manifest()
    safe_class = "".join(part.capitalize() for part in re.split(r"[^A-Za-z0-9]+", class_name)) + "Agent"
    tool_names = ", ".join(json.dumps(t.name) for t in spec.tools)
    return f'''package generated.gemini

/**
 * Generated Android tool-selection boundary for {spec.name}.
 * Credentials must come from Android Keystore/approved secret handling.
 */
object {safe_class} {{
    const val MODEL = "{spec.model}"
    const val SECRET_REF = "{spec.secret_ref}"
    val ENABLED_TOOLS = listOf({tool_names})

    const val APPROVAL_MODE = "{spec.approval_mode}"
    const val MEMORY_MODE = "{spec.memory}"

    fun validateToolSelection(selected: Set<String>): Boolean =
        selected.all {{ it in ENABLED_TOOLS }}
}}
'''


def validate_untrusted_tool_code(source: str) -> list[str]:
    """Static tripwire for the dangerous pattern in editable builder code."""
    findings: list[str] = []
    if not source.strip():
        findings.append("tool source is empty")
    dangerous = [
        (r"(^|\n)\s*exec\s*\(", "dynamic exec"),
        (r"(^|\n)\s*eval\s*\(", "dynamic eval"),
        (r"os\.system\s*\(", "shell execution"),
        (r"subprocess\.(run|Popen|call)\s*\(", "subprocess execution"),
        (r'''open\([^)]*,\s*[\'\"]w''', "unbounded file write"),
    ]
    for pattern, label in dangerous:
        if re.search(pattern, source):
            findings.append(label)
    if SECRET_VALUE_WORDS.search(source):
        findings.append("possible plaintext secret")
    return findings
