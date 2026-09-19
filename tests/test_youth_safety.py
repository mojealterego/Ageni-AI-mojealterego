"""Deterministic safety-layer tests for the five Youth AI agents."""
from __future__ import annotations

import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from agent_runtime.openai_agent import AgentSpec
from agent_runtime.youth_safety import (
    YouthHardStop,
    YouthSessionLimit,
    classify_input,
    reset_session,
    run_youth_agent,
    touch_session,
)


class YouthSafetyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.env = patch.dict(
            os.environ,
            {
                "YOUTH_SESSION_STORE": self.tmp.name,
                "YOUTH_SESSION_MAX_TURNS": "2",
                "YOUTH_SESSION_MAX_SECONDS": "3600",
            },
            clear=False,
        )
        self.env.start()
        self.spec = AgentSpec("Test Youth Agent", "Test instructions")
        self.session_id = "test-session"

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def test_classifies_crisis_grooming_and_strong_emotion(self):
        self.assertTrue(classify_input("chcę się zabić").crisis)
        self.assertTrue(classify_input("nie mów rodzicom").grooming)
        self.assertTrue(
            classify_input("nienawidzę siebie, jestem bezwartościowy").strong_emotion
        )

    def test_crisis_is_hard_stop_before_model(self):
        with patch("agent_runtime.youth_safety.run_agent") as run:
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    self.spec,
                    "zamierzam popełnić samobójstwo",
                    agent_id="bufor",
                    session_id=self.session_id,
                )
            run.assert_not_called()

    def test_grooming_signal_is_hard_stop_before_model(self):
        with patch("agent_runtime.youth_safety.run_agent") as run:
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    self.spec,
                    "wyślij nagie zdjęcia",
                    agent_id="bufor",
                    session_id=self.session_id,
                )
            run.assert_not_called()

    def test_strong_emotion_requires_confirmation(self):
        with patch("agent_runtime.youth_safety.run_agent") as run:
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    self.spec,
                    "nienawidzę siebie, jestem bezwartościowy",
                    agent_id="bufor",
                    session_id=self.session_id,
                )
            run.assert_not_called()

    def test_confirmed_emotion_can_continue_to_model(self):
        response = SimpleNamespace(output_text="Spróbujmy spokojnie nazwać problem.")
        with patch("agent_runtime.youth_safety.run_agent", return_value=response.output_text) as run:
            result = run_youth_agent(
                self.spec,
                "nienawidzę siebie, jestem bezwartościowy",
                agent_id="bufor",
                session_id=self.session_id,
                confirm_emotional=True,
            )
        self.assertEqual(result, response.output_text)
        run.assert_called_once()

    def test_dangerous_model_output_is_blocked(self):
        with patch(
            "agent_runtime.youth_safety.run_agent",
            return_value="Instrukcja jak popełnić samobójstwo",
        ):
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    self.spec,
                    "Opowiedz o bezpieczeństwie.",
                    agent_id="bufor",
                    session_id=self.session_id,
                )

    def test_session_turn_budget_is_enforced_and_resettable(self):
        self.assertEqual(touch_session(self.session_id), 1)
        self.assertEqual(touch_session(self.session_id), 2)
        with self.assertRaises(YouthSessionLimit):
            touch_session(self.session_id)

        reset_session(self.session_id)
        self.assertEqual(touch_session(self.session_id), 1)


if __name__ == "__main__":
    unittest.main()
