"""Offline tests for the 2025–2026 strategic occupational AI batch."""
import runpy
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "agents" / "occupational-ai" / "agent.py"

EXPECTED_IDS = (
    "investment-research",
    "aml-compliance",
    "fpa-budgeting",
    "devops-sre",
    "qa-testing",
    "legacy-migration",
    "contract-review",
    "regulatory-watch",
    "supply-chain",
    "procurement",
    "sdr-sales",
    "social-media",
    "customer-support",
    "talent-recruiter",
    "employee-experience",
    "medical-coding",
)


class OccupationalAgentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = runpy.run_path(str(MODULE_PATH), run_name="occupational_ai_test")

    def test_catalog_contains_exactly_16_profiles(self):
        agents = self.module["AGENTS"]
        self.assertEqual(tuple(agents.keys()), EXPECTED_IDS)
        self.assertEqual(len(agents), 16)

    def test_all_profiles_are_registered_and_resolve_to_dispatcher(self):
        for agent_id in EXPECTED_IDS:
            with self.subTest(agent_id=agent_id):
                entry = find_agent(agent_id)
                self.assertEqual(
                    entry.entrypoint,
                    "agents/occupational-ai/agent.py",
                )

    def test_each_profile_builds_an_agent_spec(self):
        build_spec = self.module["build_spec"]
        instructions_for = self.module["instructions_for"]
        for agent_id in EXPECTED_IDS:
            with self.subTest(agent_id=agent_id):
                spec = build_spec(agent_id)
                self.assertTrue(spec.name)
                self.assertIn(spec.name, instructions_for(agent_id))
                self.assertEqual(
                    instructions_for(agent_id).count(
                        "Distinguish source facts, assumptions, estimates and recommendations."
                    ),
                    1,
                )
                self.assertIn("explicit human approval", instructions_for(agent_id))

    def test_unknown_profile_is_rejected(self):
        with self.assertRaisesRegex(KeyError, "Unknown occupational agent ID"):
            self.module["get_agent"]("not-a-real-occupational-agent")


if __name__ == "__main__":
    unittest.main()
