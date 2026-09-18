"""Offline tests for runtime validation; no API calls are made."""
import os
import unittest
from unittest.mock import patch
from agent_runtime.openai_agent import AgentSpec, run_agent

class RuntimeValidationTests(unittest.TestCase):
    def setUp(self):
        self.spec = AgentSpec("Test", "Test instructions")

    def test_rejects_blank_input_before_network(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "dummy"}):
            with self.assertRaisesRegex(ValueError, "Input must not be empty"):
                run_agent(self.spec, "  ")

    def test_rejects_missing_api_key(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY is not set"):
                run_agent(self.spec, "hello")

if __name__ == "__main__":
    unittest.main()
