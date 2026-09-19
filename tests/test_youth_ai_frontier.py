"""Integration tests for the Youth AI specialist batch."""
from __future__ import annotations

import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent, list_agents

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
    "youth-ai-meme-archivist": "agents/youth-ai-meme-archivist/agent.py",
    "youth-ai-safe-party-planner": "agents/youth-ai-safe-party-planner/agent.py",
    "youth-ai-parasocial-manager": "agents/youth-ai-parasocial-manager/agent.py",
}

GUARDS = {
    "youth-ai-fintech-guardian": ("financial literacy", "gambling", "credentials"),
    "youth-ai-bio-optimizer": ("do not diagnose", "weight-loss", "wearables"),
    "youth-ai-digital-stylist": ("do not rate bodies", "sustainable", "privacy"),
    "youth-ai-esports-strategist": ("real-time", "covertly", "fair play"),
    "youth-ai-agor-civic": ("neutral factual", "political", "explicit review"),
    "youth-ai-spiritual-compass": ("astrology", "not evidence-based", "do not"),
    "youth-ai-hype-curator": ("authenticity", "speculation", "payment credentials"),
    "youth-ai-energy-regulator": ("do not diagnose", "hidden calendar", "user control"),
    "youth-ai-meme-archivist": ("provenance", "harassment", "do not invent"),
    "youth-ai-safe-party-planner": ("without alcohol", "trusted adult", "explicit user"),
    "youth-ai-parasocial-manager": ("do not diagnose", "exclusivity", "offline"),
}


class YouthAIBatchTests(unittest.TestCase):
    def test_all_youth_agents_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(set(YOUTH_AGENTS) <= registered)

    def test_registry_targets_and_files_compile(self):
        for agent_id, entrypoint in YOUTH_AGENTS.items():
            entry = find_agent(agent_id)
            self.assertEqual(entry.entrypoint, entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_agents_use_shared_runtime(self):
        for entrypoint in YOUTH_AGENTS.values():
            source = (ROOT / entrypoint).read_text(encoding="utf-8")
            self.assertIn("AgentSpec", source)
            self.assertIn("run_agent", source)

    def test_domain_guardrails_are_present(self):
        for agent_id, phrases in GUARDS.items():
            source = (ROOT / YOUTH_AGENTS[agent_id]).read_text(encoding="utf-8").lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), source)

    def test_registry_descriptions_are_present(self):
        for agent_id in YOUTH_AGENTS:
            self.assertTrue(find_agent(agent_id).description)


if __name__ == "__main__":
    unittest.main()
