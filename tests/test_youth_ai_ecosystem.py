"""Integration tests for the five Youth AI development ecosystem agents."""
from __future__ import annotations

import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent, list_agents
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]


def load_ecosystem_module():
    path = ROOT / "agents/youth-ai-ecosystem/agent.py"
    spec = importlib.util.spec_from_file_location("youth_ai_ecosystem_agent", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load youth ecosystem profile module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ecosystem = load_ecosystem_module()

CORE_AGENTS = {
    "youth-ai-socrates-tutor": "agents/youth-ai-socrates-tutor/agent.py",
    "youth-ai-creator": "agents/youth-ai-creator/agent.py",
    "youth-ai-navigator": "agents/youth-ai-navigator/agent.py",
    "youth-ai-verifier": "agents/youth-ai-verifier/agent.py",
    "youth-ai-wellness-buffer": "agents/youth-ai-wellness-buffer/agent.py",
}


class YouthAIEcosystemTests(unittest.TestCase):
    def test_core_agents_are_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(set(CORE_AGENTS) <= registered)

    def test_registry_paths_and_entrypoints_compile(self):
        for agent_id, entrypoint in CORE_AGENTS.items():
            with self.subTest(agent=agent_id):
                entry = find_agent(agent_id)
                self.assertEqual(entry.entrypoint, entrypoint)
                py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_core_entrypoints_use_shared_runtime(self):
        for entrypoint in CORE_AGENTS.values():
            source = (ROOT / entrypoint).read_text(encoding="utf-8")
            self.assertIn(
                "from agent_runtime.openai_agent import AgentSpec, run_agent",
                source,
            )
            self.assertIn("run_agent(", source)

    def test_profile_catalog_has_exactly_five_core_agents(self):
        self.assertEqual(set(ecosystem.AGENTS), {
            "sokrates",
            "kreator",
            "nawigator",
            "weryfikator",
            "bufor",
        })
        self.assertEqual(len(ecosystem.list_agents()), 5)

    def test_unified_runner_compiles(self):
        py_compile.compile(
            str(ROOT / "agents/youth-ai-ecosystem/runner.py"),
            doraise=True,
        )

    def test_profile_metadata_contains_required_safety_contracts(self):
        required = {
            "sokrates": ("software, not a person", "Do not expose hidden chain-of-thought"),
            "kreator": ("Preserve the user's voice and agency", "unsafe challenges"),
            "nawigator": ("multiple paths", "Do not pigeonhole"),
            "weryfikator": ("lateral reading", "political/electoral"),
            "bufor": ("non-clinical", "imminent self-harm"),
        }
        for agent_id, phrases in required.items():
            instructions = ecosystem.get_agent(agent_id).instructions
            with self.subTest(agent=agent_id):
                for phrase in phrases:
                    self.assertIn(phrase, instructions)

    def test_risk_levels_are_explicit(self):
        risks = {row["agent_id"]: row["risk_level"] for row in ecosystem.list_agents()}
        self.assertEqual(risks, {
            "sokrates": "low",
            "kreator": "medium",
            "nawigator": "low",
            "weryfikator": "medium",
            "bufor": "high",
        })


if __name__ == "__main__":
    unittest.main()
