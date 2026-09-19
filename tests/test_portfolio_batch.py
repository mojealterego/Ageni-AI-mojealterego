"""Tests for the portfolio agent catalog and its safety contract."""
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

    "gemini-agent-builder", "gemini-desktop-builder", "gemini-android-builder",
    "gemini-edge-rag", "gemini-security-auditor", "gemini-multiagent-orchestrator",
}

class PortfolioBatchTests(unittest.TestCase):
    def test_all_portfolio_and_gemini_registered(self):
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
        self.assertEqual(len(matches), 47)

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

            "gemini-agent-builder": "agents/gemini-agent-builder/agent.py",
            "gemini-desktop-builder": "agents/gemini-desktop-builder/agent.py",
            "gemini-android-builder": "agents/gemini-android-builder/agent.py",
            "gemini-edge-rag": "agents/gemini-edge-rag/agent.py",
            "gemini-security-auditor": "agents/gemini-security-auditor/agent.py",
            "gemini-multiagent-orchestrator": "agents/gemini-multiagent-orchestrator/agent.py",
            "system-kernel-engineer": "agents/system-kernel-engineer/agent.py",
            "gamedev-engineer": "agents/gamedev-engineer/agent.py",
            "creative-writing-room": "agents/creative-writing-room/agent.py",
            "comic-visual-continuity": "agents/comic-visual-continuity/agent.py",
            "boardgame-ludology": "agents/boardgame-ludology/agent.py",
            "quality-diversity-engineer": "agents/quality-diversity-engineer/agent.py",
            "frontend-design-to-code": "agents/frontend-design-to-code/agent.py",
            "legal-compliance-agent": "agents/legal-compliance-agent/agent.py",
            "scientific-experiment-agent": "agents/scientific-experiment-agent/agent.py",
            "cross-saas-orchestrator": "agents/cross-saas-orchestrator/agent.py",
            "agent-supervisor-killswitch": "agents/agent-supervisor-killswitch/agent.py",
            "realtime-crisis-manager": "agents/realtime-crisis-manager/agent.py",
            "agent-evaluation-ops": "agents/agent-evaluation-ops/agent.py",
        }
        registry = {e.agent_id: e.entrypoint for e in list_agents()}
        for agent_id, entrypoint in specialized.items():
            self.assertEqual(registry[agent_id], entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_all_registered_entrypoints_exist(self):
        missing = [
            (entry.agent_id, entry.entrypoint)
            for entry in list_agents()
            if not (ROOT / entry.entrypoint).is_file()
        ]
        self.assertEqual(missing, [])

    def test_report_specialists_keep_domain_contracts(self):
        required = {
            "gamedev-engineer": ("bounded", "deterministic", "benchmark"),
            "creative-writing-room": ("canon", "continuity", "provenance"),
            "comic-visual-continuity": ("continuity", "reference", "acceptance"),
            "boardgame-ludology": ("self-play", "MCTS", "MAP-Elites"),
            "quality-diversity-engineer": ("MAP-Elites", "Novelty Search", "reproducibility"),
            "frontend-design-to-code": ("responsive", "accessibility", "validation"),
            "system-kernel-engineer": ("unsafe", "FFI", "verification"),
            "kernel-systems-engineer": ("nested virtualization", "rollback", "RAG"),
            "legal-compliance-agent": ("citation", "claim", "provenance"),
            "scientific-experiment-agent": ("hardware-in-the-loop", "calibration", "abort"),
            "cross-saas-orchestrator": ("idempotency", "OAuth", "compensation"),
            "agent-supervisor-killswitch": ("kill switch", "budget", "circuit"),
            "realtime-crisis-manager": ("latency", "speed path", "fail-safe"),
            "agent-evaluation-ops": ("golden", "drift", "circuit-breaker"),
        }
        registry = {e.agent_id: e.entrypoint for e in list_agents()}
        for agent_id, phrases in required.items():
            self.assertIn(agent_id, registry)
            source = (ROOT / registry[agent_id]).read_text(encoding='utf-8')
            for phrase in phrases:
                self.assertIn(phrase.lower(), source.lower())

if __name__ == "__main__":
    unittest.main()
