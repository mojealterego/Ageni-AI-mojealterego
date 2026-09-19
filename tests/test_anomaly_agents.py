"""Integration tests for the autonomous anomaly/frontier research agent batch."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent, list_agents

ROOT = Path(__file__).resolve().parents[1]

ANOMALY_AGENTS = {
    "xenobot-research-agent": "agents/xenobot-research-agent/agent.py",
    "dishbrain-agent": "agents/dishbrain-agent/agent.py",
    "hybrot-agent": "agents/hybrot-agent/agent.py",
    "terra0-agent": "agents/terra0-agent/agent.py",
    "plantoid-agent": "agents/plantoid-agent/agent.py",
    "truth-terminal-agent": "agents/truth-terminal-agent/agent.py",
    "mr-goxx-agent": "agents/mr-goxx-agent/agent.py",
    "chaosgpt-safety-agent": "agents/chaosgpt-safety-agent/agent.py",
    "tay-resilience-agent": "agents/tay-resilience-agent/agent.py",
    "aaron-creative-agent": "agents/aaron-creative-agent/agent.py",
    "painting-fool-agent": "agents/painting-fool-agent/agent.py",
    "botto-curator-agent": "agents/botto-curator-agent/agent.py",
    "polyworld-agent": "agents/polyworld-agent/agent.py",
    "lenia-agent": "agents/lenia-agent/agent.py",
    "ai-steve-civic-agent": "agents/ai-steve-civic-agent/agent.py",
    "emergent-language-agent": "agents/emergent-language-agent/agent.py",
    "coscientist-agent": "agents/coscientist-agent/agent.py",
    "chemcrow-safety-agent": "agents/chemcrow-safety-agent/agent.py",
    "genefer-prime-search-agent": "agents/genefer-prime-search-agent/agent.py",
}


class AnomalyAgentBatchTests(unittest.TestCase):
    def test_all_agents_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertEqual(set(ANOMALY_AGENTS), registered & set(ANOMALY_AGENTS))

    def test_registry_targets_exist_and_compile(self):
        for agent_id, expected_path in ANOMALY_AGENTS.items():
            entry = find_agent(agent_id)
            self.assertEqual(entry.entrypoint, expected_path)
            path = ROOT / expected_path
            self.assertTrue(path.is_file(), expected_path)
            py_compile.compile(str(path), doraise=True)

    def test_each_entrypoint_uses_shared_runtime(self):
        required = ("AgentSpec", "run_agent")
        for path in ANOMALY_AGENTS.values():
            source = (ROOT / path).read_text(encoding="utf-8")
            for token in required:
                self.assertIn(token, source)

    def test_high_risk_domains_have_explicit_non_execution_guards(self):
        expected_guards = {
            "mr-goxx-agent": ("virtual", "never connect to brokerage"),
            "chaosgpt-safety-agent": ("sandbox", "do not instantiate objectives involving harm"),
            "coscientist-agent": ("do not provide operational instructions", "hardware actions require"),
            "chemcrow-safety-agent": ("do not generate synthesis instructions", "do not control laboratory robots"),
            "ai-steve-civic-agent": ("do not target voters", "do not optimize persuasion"),
            "xenobot-research-agent": ("do not provide step-by-step wet-lab protocols",),
        }
        registry = {entry.agent_id: entry.entrypoint for entry in list_agents()}
        for agent_id, phrases in expected_guards.items():
            source = (ROOT / registry[agent_id]).read_text(encoding="utf-8").lower()
            for phrase in phrases:
                self.assertIn(phrase.lower(), source)


if __name__ == "__main__":
    unittest.main()
