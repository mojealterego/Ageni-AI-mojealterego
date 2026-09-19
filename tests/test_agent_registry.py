"""Offline tests for the repository agent registry."""
import unittest

from agent_runtime.registry import existing_entrypoints, find_agent, list_agents


class AgentRegistryTests(unittest.TestCase):
    def test_ids_are_unique(self):
        ids = [entry.agent_id for entry in list_agents()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_find_known_agent(self):
        entry = find_agent("photo-specialist")
        self.assertEqual(entry.entrypoint, "agents/photo/specialist_agent.py")

    def test_unknown_agent_raises(self):
        with self.assertRaisesRegex(KeyError, "not-real"):
            find_agent("not-real")

    def test_existing_entrypoints_are_subset_of_registry(self):
        registered = set(list_agents())
        self.assertTrue(set(existing_entrypoints()).issubset(registered))


if __name__ == "__main__":
    unittest.main()
