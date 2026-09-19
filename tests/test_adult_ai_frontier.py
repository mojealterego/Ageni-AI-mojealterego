"""Integration tests for the adult AI frontier specialist batch."""
from __future__ import annotations

import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import find_agent, list_agents

ROOT = Path(__file__).resolve().parents[1]

FRONTIER = {
    "adult-ai-bio-conductor": "agents/adult-ai-bio-conductor/agent.py",
    "adult-ai-haptic-composer": "agents/adult-ai-haptic-composer/agent.py",
    "adult-ai-the-mirror": "agents/adult-ai-the-mirror/agent.py",
    "adult-ai-the-anchor": "agents/adult-ai-the-anchor/agent.py",
    "adult-ai-poly-dynamics-simulator": "agents/adult-ai-poly-dynamics-simulator/agent.py",
    "adult-ai-social-turing-tester": "agents/adult-ai-social-turing-tester/agent.py",
    "adult-ai-the-auteur": "agents/adult-ai-the-auteur/agent.py",
    "adult-ai-ludonarrative-weaver": "agents/adult-ai-ludonarrative-weaver/agent.py",
    "adult-ai-srh-educator": "agents/adult-ai-srh-educator/agent.py",
    "adult-ai-arm-mediator": "agents/adult-ai-arm-mediator/agent.py",
    "adult-ai-bio-narrative-orchestrator": "agents/adult-ai-bio-narrative-orchestrator/agent.py",
    "adult-ai-ple-polykule": "agents/adult-ai-ple-polykule/agent.py",
    "adult-ai-cyrano-social-vetting": "agents/adult-ai-cyrano-social-vetting/agent.py",
    "adult-ai-detachment": "agents/adult-ai-detachment/agent.py",
    "adult-ai-bdsm-task-manager": "agents/adult-ai-bdsm-task-manager/agent.py",
    "adult-ai-legacy-archivist": "agents/adult-ai-legacy-archivist/agent.py",
}

DOMAIN_GUARDS = {
    "adult-ai-bio-conductor": ("consent", "biometric", "fail-safe"),
    "adult-ai-haptic-composer": ("declarative", "hardware", "universal stop"),
    "adult-ai-the-mirror": ("not therapy", "do not", "uncertainty"),
    "adult-ai-the-anchor": ("non-clinical", "do not diagnose", "crisis"),
    "adult-ai-poly-dynamics-simulator": ("fictional simulation", "revocable", "manipulation"),
    "adult-ai-social-turing-tester": ("simulation", "social-engineering", "explicit authorization"),
    "adult-ai-the-auteur": ("provenance", "consent", "deepfakes"),
    "adult-ai-ludonarrative-weaver": ("game state", "reset", "never sexualize minors"),
    "adult-ai-srh-educator": ("evidence-oriented", "age-gate", "medical advice"),
    "adult-ai-arm-mediator": ("consent", "monitor", "arbiter"),
    "adult-ai-bio-narrative-orchestrator": ("consent", "physiology", "deterministic"),
    "adult-ai-ple-polykule": ("explicit approval", "infer emotions", "veto"),
    "adult-ai-cyrano-social-vetting": ("age", "diagnos", "dox"),
    "adult-ai-detachment": ("impersonate", "not clinical", "monitor"),
    "adult-ai-bdsm-task-manager": ("consent", "physical restraints", "stop"),
    "adult-ai-legacy-archivist": ("provenance", "deletion", "digital twin"),
}


class AdultAIFrontierTests(unittest.TestCase):
    def test_all_specialists_registered(self):
        registered = {entry.agent_id for entry in list_agents()}
        self.assertTrue(set(FRONTIER) <= registered)

    def test_registry_targets_and_files_compile(self):
        for agent_id, entrypoint in FRONTIER.items():
            entry = find_agent(agent_id)
            self.assertEqual(entry.entrypoint, entrypoint)
            py_compile.compile(str(ROOT / entrypoint), doraise=True)

    def test_shared_runtime_contract_and_guards(self):
        for agent_id, entrypoint in FRONTIER.items():
            source = (ROOT / entrypoint).read_text(encoding="utf-8")
            self.assertIn("AgentSpec", source)
            self.assertIn("run_agent", source)
            for phrase in DOMAIN_GUARDS[agent_id]:
                self.assertIn(phrase.lower(), source.lower())

    def test_registry_description_is_present(self):
        for agent_id in FRONTIER:
            self.assertTrue(find_agent(agent_id).description)


if __name__ == "__main__":
    unittest.main()
