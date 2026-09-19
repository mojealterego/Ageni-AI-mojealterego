"""Offline tests for the deterministic Gemini blueprint compiler."""
import unittest

from agent_runtime.gemini_builder import (
    AgentBlueprint,
    ToolBlueprint,
    compile_blueprint,
    validate_untrusted_tool_code,
)


class GeminiBuilderTests(unittest.TestCase):
    def valid_spec(self) -> AgentBlueprint:
        return AgentBlueprint(
            name="Demo Gemini Agent",
            platform="hybrid",
            model="gemini-current",
            instruction="Use approved tools and cite provenance.",
            tools=(
                ToolBlueprint(
                    "get_status",
                    "Read local status.",
                    permission="read",
                ),
                ToolBlueprint(
                    "send_message",
                    "Send a message.",
                    permission="external-write",
                    requires_approval=True,
                ),
            ),
            memory="local-rag",
            approval_mode="consequential",
            secret_ref="ENV_GEMINI_API_KEY",
        )

    def test_valid_blueprint_compiles_all_artifacts(self):
        artifacts = compile_blueprint(self.valid_spec())
        self.assertIn("manifest.json", artifacts)
        self.assertIn("root_agent.yaml", artifacts)
        self.assertTrue(any(name.endswith("_desktop.py") for name in artifacts))
        self.assertTrue(any(name.endswith("_android.kt") for name in artifacts))

    def test_dangerous_tool_requires_approval(self):
        spec = self.valid_spec()
        invalid = AgentBlueprint(
            name=spec.name,
            platform=spec.platform,
            model=spec.model,
            instruction=spec.instruction,
            tools=(
                ToolBlueprint(
                    "sendSMS",
                    "Send SMS to a recipient.",
                    permission="external-write",
                ),
            ),
            memory=spec.memory,
            approval_mode=spec.approval_mode,
            secret_ref=spec.secret_ref,
            private_network_only=spec.private_network_only,
            metadata=spec.metadata,
        )
        with self.assertRaisesRegex(ValueError, "requires approval"):
            invalid.to_manifest()

    def test_plaintext_secret_is_rejected(self):
        spec = self.valid_spec()
        invalid = AgentBlueprint(
            name=spec.name,
            platform=spec.platform,
            model=spec.model,
            instruction=spec.instruction,
            tools=spec.tools,
            memory=spec.memory,
            approval_mode=spec.approval_mode,
            secret_ref=spec.secret_ref,
            private_network_only=spec.private_network_only,
            metadata={"api_key": "AIzaFAKE"},
        )
        with self.assertRaisesRegex(ValueError, "plaintext secret"):
            invalid.to_manifest()

    def test_untrusted_code_tripwires(self):
        findings = validate_untrusted_tool_code(
            'import os\nos.system("curl https://example.invalid")',
        )
        self.assertIn("shell execution", findings)

    def test_eval_and_exec_tripwires(self):
        findings = validate_untrusted_tool_code("exec(user_input)\neval(user_input)")
        self.assertIn("dynamic exec", findings)
        self.assertIn("dynamic eval", findings)

    def test_local_rag_defaults_to_private_network(self):
        spec = self.valid_spec()
        self.assertEqual(spec.memory, "local-rag")
        self.assertTrue(spec.private_network_only)


if __name__ == "__main__":
    unittest.main()
