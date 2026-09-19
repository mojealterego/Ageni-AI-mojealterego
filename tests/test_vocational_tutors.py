"""Offline integration tests for the 11 vocational tutor profiles."""
from __future__ import annotations

import importlib.util
import py_compile
import sys
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent, list_agents

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "agents/vocational-tutors/agents.py"

EXPECTED = {
    "polonista": "Wirtualny Polonista",
    "matematyka": "Tutor Matematyki STEM",
    "jezyki": "Tutor Języków Zawodowych",
    "inf02": "SysAdmin Mentor INF.02",
    "inf03": "Full-Stack Mentor INF.03",
    "mechanik": "Mentor Mechanik i CNC",
    "budownictwo": "Mentor Budownictwa i Kosztorysowania",
    "ekonomista": "Tutor Ekonomista EKA",
    "gastronomia": "Tutor Gastronomii HGT",
    "biznes": "Biznes Mentor",
    "edb": "Instruktor EDB",
}


def load_module():
    spec = importlib.util.spec_from_file_location("vocational_tutors_test", RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vocational tutor runner")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


vocational = load_module()


class VocationalTutorIntegrationTests(unittest.TestCase):
    def test_profiles_are_exactly_the_report_suite(self):
        self.assertEqual(set(vocational.PROFILES), set(EXPECTED))
        self.assertEqual(len(vocational.PROFILES), 11)
        for agent_id, label in EXPECTED.items():
            with self.subTest(agent=agent_id):
                self.assertEqual(vocational.PROFILES[agent_id].name, label)

    def test_central_registry_contains_all_profiles(self):
        registered = {entry.agent_id: entry for entry in list_agents()}
        for agent_id in EXPECTED:
            with self.subTest(agent=agent_id):
                self.assertIn(agent_id, registered)
                self.assertEqual(
                    registered[agent_id].entrypoint,
                    "agents/vocational-tutors/agents.py",
                )

    def test_runner_uses_student_safety_session_layer(self):
        source = RUNNER.read_text(encoding="utf-8")
        self.assertIn("run_youth_agent(", source)
        self.assertIn("--session-id", source)
        self.assertIn("--confirm-emotional", source)
        self.assertIn("YouthHardStop", source)

    def test_core_safety_contracts_are_present(self):
        combined = "\n".join(
            spec.instructions for spec in vocational.PROFILES.values()
        )
        for phrase in (
            "not a human teacher",
            "Never invent sources",
            "Never reveal hidden chain-of-thought",
            "Minimize personal data",
            "Consequential external actions require explicit authorization",
        ):
            self.assertIn(phrase, combined)

    def test_domain_guardrails_are_present(self):
        expected_phrases = {
            "inf02": "credential theft",
            "inf03": "parameterized SQL",
            "mechanik": "Never bypass interlocks",
            "budownictwo": "current Polish law",
            "ekonomista": "current tax",
            "gastronomia": "HACCP/GHP",
            "edb": "emergency services",
        }
        for agent_id, phrase in expected_phrases.items():
            with self.subTest(agent=agent_id):
                self.assertIn(phrase, vocational.PROFILES[agent_id].instructions)

    def test_runner_compiles(self):
        py_compile.compile(str(RUNNER), doraise=True)

    def test_registry_entrypoints_compile(self):
        for agent_id in EXPECTED:
            with self.subTest(agent=agent_id):
                entry = find_agent(agent_id)
                self.assertEqual(entry.entrypoint, str(Path("agents/vocational-tutors/agents.py")))
                py_compile.compile(str(ROOT / entry.entrypoint), doraise=True)


if __name__ == "__main__":
    unittest.main()
