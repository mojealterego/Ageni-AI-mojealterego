"""Integration tests for the Youth AI specialist batch."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import list_agents

ROOT = Path(__file__).resolve().parents[1]

YOUTH_AGENTS = {
    "youth-ai-fintech-guardian": "agents/youth-ai-fintech-guardian/agent.py",
    "youth-ai-bio-optimizer": "agents/youth-ai-bio-optimizer/agent.py",
    "youth-ai-digital-stylist": "agents/youth-ai-digital-stylist/agent.py",
    "youth-ai-esports-strategist": "agents/youth-ai-esports-strategist/agent.py",
    "youth-ai-agor-civic": "agents/youth-ai-agor-civic/agent.py",
    "youth-ai-spiritual-compass": "agents/youth-ai-spiritual-compass/agent.py",
    "youth-ai-hype-curator": "agents/youth-ai-hype-curator/agent.py",
    "youth-ai-energy-regulator": "agents/youth-ai-energy-regulator/agent.py",
    "youth-ai-meme-historian": "agents/youth-ai-meme-historian/agent.py",
    "youth-ai-safe-party-planner": "agents/youth-ai-safe-party-planner/agent.py",
    "youth-ai-parasocial-manager": "agents/youth-ai-parasocial-manager/agent.py",
}


class YouthAIBatchTests(unittest.TestCase):
    def test_all_youth_agents_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(YOUTH_AGENTS.keys() <= registered)

    def test_registry_targets_and_files_compile(self):
        registry = {entry.agent_id: entry.entrypoint for entry in list_agents()}
        for agent_id, entrypoint in YOUTH_AGENTS.items():
            self.assertEqual(registry[agent_id], entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_agents_use_shared_runtime(self):
        for entrypoint in YOUTH_AGENTS.values():
            source = (ROOT / entrypoint).read_text(encoding="utf-8")
            self.assertIn("AgentSpec", source)
            self.assertIn("run_agent", source)

    def test_domain_guardrails_are_present(self):
        guards = {
            "youth-ai-fintech-guardian": ("financial literacy", "do not encourage gambling", "credentials"),
            "youth-ai-bio-optimizer": ("do not diagnose", "do not diagnose", "weight-loss"),
            "youth-ai-digital-stylist": ("do not rate bodies", "sustainable", "identifying photos"),
            "youth-ai-esports-strategist": ("covertly", "cheating", "healthy play-life balance"),
            "youth-ai-agor-civic": ("neutral factual context", "do not target or manipulate", "political"),
            "youth-ai-spiritual-compass": ("without imposing religion", "astrology", "supernatural certainty"),
            "youth-ai-hype-curator": ("authenticity", "guarantee future price increases", "payment credentials"),
            "youth-ai-energy-regulator": ("do not diagnose", "hidden calendar", "user control"),
            "youth-ai-meme-historian": ("verified origins", "harass", "media literacy"),
            "youth-ai-safe-party-planner": ("without alcohol", "recreational drugs", "safe arrival and return"),
            "youth-ai-parasocial-manager": ("do not diagnose", "impersonate a creator", "offline relationships"),
        }
        registry = {entry.agent_id: entry.entrypoint for entry in list_agents()}
        for agent_id, phrases in guards.items():
            source = (ROOT / registry[agent_id]).read_text(encoding="utf-8").lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), source)


if __name__ == "__main__":
    unittest.main()
