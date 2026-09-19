"""Offline tests for runtime validation; no API calls are made."""
import os
import unittest
from types import SimpleNamespace
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

    def test_uses_validated_default_model(self):
        response = SimpleNamespace(output_text="ok")
        with patch.dict(os.environ, {"OPENAI_API_KEY": "dummy"}, clear=True):
            with patch("openai.OpenAI") as openai_cls:
                openai_cls.return_value.responses.create.return_value = response

                self.assertEqual(run_agent(self.spec, "hello"), "ok")

                call = openai_cls.return_value.responses.create.call_args
                self.assertEqual(call.kwargs["model"], "gpt-4.1-mini")
                self.assertEqual(call.kwargs["instructions"], "Test instructions")
                self.assertEqual(call.kwargs["input"], "hello")

    def test_model_override_and_env_override(self):
        response = SimpleNamespace(output_text="ok")
        with patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "dummy", "OPENAI_MODEL": "env-model"},
            clear=True,
        ):
            with patch("openai.OpenAI") as openai_cls:
                openai_cls.return_value.responses.create.return_value = response

                run_agent(self.spec, "hello", "call-model")
                self.assertEqual(
                    openai_cls.return_value.responses.create.call_args.kwargs["model"],
                    "call-model",
                )

                run_agent(self.spec, "hello")
                self.assertEqual(
                    openai_cls.return_value.responses.create.call_args.kwargs["model"],
                    "env-model",
                )


if __name__ == "__main__":
    unittest.main()
