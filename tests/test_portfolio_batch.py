"""Tests for the 34-agent portfolio batch."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import list_agents, existing_entrypoints


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "agent-policy-gateway",
    "agent-ops-control-tower",
    "compliance-evidence",
    "procurement-scout",
    "cashflow-collections",
    "contract-obligations",
    "data-quality",
    "inventory-replenishment",
    "ai-finops",
    "customer-operations",
    "money-agent",
    "inbox-agent",
    "life-admin-agent",
    "shopping-agent",
    "scam-shield-agent",
    "family-care-agent",
    "career-agent",
    "travel-execution-agent",
    "health-navigator",
    "personal-knowledge-agent",
    "aaa-automation-agency",
    "ai-creator-monetization",
    "programmatic-seo",
    "faceless-video",
    "micro-saas",
    "ai-trading-risk",
    "ai-freelance-ops",
    "cognitive-profiling-auditor",
    "persuasion-dark-patterns-auditor",
    "affective-ai-evaluator",
    "social-engineering-defense",
    "llm-red-team-auditor",
    "synthetic-media-disinformation-detector",
    "cognitive-privacy-governance",
}


class PortfolioBatchTests(unittest.TestCase):
    def test_all_34_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(EXPECTED.issubset(registered))

    def test_shared_entrypoint_exists(self):
        matches = [e for e in existing_entrypoints() if e.agent_id in EXPECTED]
        self.assertEqual(len(matches), 34)

    def test_shared_entrypoint_compiles(self):
        py_compile.compile(str(ROOT / "agents/portfolio_agent.py"), doraise=True)


if __name__ == "__main__":
    unittest.main()
