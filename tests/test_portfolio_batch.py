"""Tests for the 41-agent portfolio batch and its safety contract."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import list_agents, existing_entrypoints
from agents.portfolio_agent import CATALOG, build_instructions

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "agent-policy-gateway", "agent-ops-control-tower", "compliance-evidence", "procurement-scout",
    "cashflow-collections", "contract-obligations", "data-quality", "inventory-replenishment",
    "ai-finops", "customer-operations", "money-agent", "inbox-agent", "life-admin-agent",
    "shopping-agent", "scam-shield-agent", "family-care-agent", "career-agent",
    "travel-execution-agent", "health-navigator", "personal-knowledge-agent", "aaa-automation-agency",
    "ai-creator-monetization", "programmatic-seo", "faceless-video", "micro-saas", "ai-trading-risk",
    "ai-freelance-ops", "cognitive-profiling-auditor", "persuasion-dark-patterns-auditor",
    "affective-ai-evaluator", "social-engineering-defense", "llm-red-team-auditor",
    "synthetic-media-disinformation-detector", "cognitive-privacy-governance", "agent-forge",
    "causal-systems-research", "ai-coding-workflow-engineer", "pdf-rag-quality",
    "datasheet-spice-model-extractor", "godot-gaussian-splatting-integrator", "omnicore-forge",
}

class PortfolioBatchTests(unittest.TestCase):
    def test_all_41_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(EXPECTED.issubset(registered))

    def test_catalog_matches_registry(self):
        registered = {entry.agent_id for entry in list_agents() if entry.agent_id in EXPECTED}
        self.assertEqual(registered, EXPECTED)
        self.assertEqual(EXPECTED, set(CATALOG))

    def test_agent_forge_has_implementation_contract(self):
        instructions = build_instructions("agent-forge")
        for phrase in ("executable-agent", "code-level changes", "tests", "provenance", "promotion"):
            self.assertIn(phrase, instructions)

    def test_omnicore_agent_has_security_and_approval_contract(self):
        instructions = build_instructions("omnicore-forge")
        self.assertIn("human authorization", instructions)
        self.assertIn("never fabricate", instructions)

    def test_new_cognitive_safety_agents_have_guardrails(self):
        guarded = {"cognitive-profiling-auditor", "persuasion-dark-patterns-auditor", "affective-ai-evaluator", "social-engineering-defense", "llm-red-team-auditor", "synthetic-media-disinformation-detector", "cognitive-privacy-governance"}
        for agent_id in guarded:
            instructions = build_instructions(agent_id)
            self.assertIn("Consequential actions require explicit human authorization", instructions)
            self.assertIn("do not facilitate covert manipulation", instructions)

    def test_shared_entrypoint_exists(self):
        matches = [e for e in existing_entrypoints() if e.agent_id in EXPECTED]
        self.assertEqual(len(matches), 41)

    def test_shared_entrypoint_compiles(self):
        py_compile.compile(str(ROOT / "agents/portfolio_agent.py"), doraise=True)

    def test_specialized_entrypoints_compile_and_registry_targets_them(self):
        specialized = {
            "agent-forge": "agents/agent-forge/agent.py",
            "causal-systems-research": "agents/causal-systems-research/agent.py",
            "ai-coding-workflow-engineer": "agents/ai-coding-workflow-engineer/agent.py",
            "pdf-rag-quality": "agents/pdf-rag-quality/agent.py",
            "datasheet-spice-model-extractor": "agents/datasheet-spice-model-extractor/agent.py",
            "godot-gaussian-splatting-integrator": "agents/godot-gaussian-splatting-integrator/agent.py",
            "omnicore-forge": "agents/omnicore-forge/agent.py",
        }
        registry = {e.agent_id: e.entrypoint for e in list_agents()}
        for agent_id, entrypoint in specialized.items():
            self.assertEqual(registry[agent_id], entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

if __name__ == "__main__":
    unittest.main()
