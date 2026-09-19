"""Integration tests for the Polish primary-school tutor specialist batch."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import list_agents

ROOT = Path(__file__).resolve().parents[1]

SCHOOL_TUTORS = {
    "mentor-odkrywcow": "agents/school-mentor-odkrywcow/agent.py",
    "playful-polyglot": "agents/school-playful-polyglot/agent.py",
    "kustosz-slowa": "agents/school-kustosz-slowa/agent.py",
    "kronikarz-analityczny": "agents/school-kronikarz-analityczny/agent.py",
    "globalny-komunikator": "agents/school-globalny-komunikator/agent.py",
    "straznik-tozsamosci": "agents/school-straznik-tozsamosci/agent.py",
    "mistrz-logiki": "agents/school-mistrz-logiki/agent.py",
    "architekt-cyfrowy": "agents/school-architekt-cyfrowy/agent.py",
    "przewodnik-terenowy": "agents/school-przewodnik-terenowy/agent.py",
    "bio-eksplorator": "agents/school-bio-eksplorator/agent.py",
    "geo-strateg": "agents/school-geo-strateg/agent.py",
    "laborant-teoretyczny": "agents/school-laborant-teoretyczny/agent.py",
    "fizyk-fundamentalny": "agents/school-fizyk-fundamentalny/agent.py",
    "wizjoner-estetyczny": "agents/school-wizjoner-estetyczny/agent.py",
    "maestro-dzwieku": "agents/school-maestro-dzwieku/agent.py",
    "inzynier-bezpieczenstwa": "agents/school-inzynier-bezpieczenstwa/agent.py",
    "aktywista-demokratyczny": "agents/school-aktywista-demokratyczny/agent.py",
    "coach-dobrostanu": "agents/school-coach-dobrostanu/agent.py",
    "instruktor-reagowania-kryzysowego": "agents/school-instruktor-reagowania-kryzysowego/agent.py",
    "trener-teoretyk": "agents/school-trener-teoretyk/agent.py",
    "architekt-kariery": "agents/school-architekt-kariery/agent.py",
    "mediator-klasowy": "agents/school-mediator-klasowy/agent.py",
    "filozof-moralny": "agents/school-filozof-moralny/agent.py",
}

class SchoolTutorBatchTests(unittest.TestCase):
    def test_all_school_tutors_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(SCHOOL_TUTORS.keys() <= registered)

    def test_registry_targets_and_files_compile(self):
        registry = {entry.agent_id: entry.entrypoint for entry in list_agents()}
        for agent_id, entrypoint in SCHOOL_TUTORS.items():
            self.assertEqual(registry[agent_id], entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_school_tutors_use_shared_runtime(self):
        for entrypoint in SCHOOL_TUTORS.values():
            source = (ROOT / entrypoint).read_text(encoding="utf-8")
            self.assertIn("AgentSpec", source)
            self.assertIn("run_agent", source)
            # The shared-runtime contract is tested here; privacy controls are
            # asserted explicitly only for domains where they are part of the batch contract.
            self.assertIn("AgentSpec", source)
            self.assertIn("run_agent", source)

    def test_sensitive_domains_have_explicit_guardrails(self):
        guarded = {
            "aktywista-demokratyczny": ("never persuade", "never", "political"),
            "coach-dobrostanu": ("do not diagnose", "do not sexualize minors", "emergency"),
            "instruktor-reagowania-kryzysowego": ("first-aid", "do not provide operational firing"),
            "architekt-cyfrowy": ("malware", "credential theft", "unauthorized access"),
            "mistrz-logiki": ("never request or expose hidden chain-of-thought",),
        }
        registry = {e.agent_id: e.entrypoint for e in list_agents()}
        for agent_id, phrases in guarded.items():
            source = (ROOT / registry[agent_id]).read_text(encoding="utf-8").lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), source)

if __name__ == "__main__":
    unittest.main()
