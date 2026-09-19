"""Offline tests for Youth AI safety/session controls."""
from __future__ import annotations

import os
import tempfile
import unittest
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


SPEC = AgentSpec(name="test", instructions="test instructions")


class YouthSafetyRuntimeTests(unittest.TestCase):
    def test_crisis_is_hard_stopped_before_model_call(self):
        decision = classify_input("Chcę się zabić.")
        self.assertTrue(decision.crisis)
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ, {"YOUTH_SESSION_STORE": tmp}, clear=False
        ), patch("agent_runtime.youth_safety.run_agent") as mocked:
            with self.assertRaises(YouthHardStop) as ctx:
                run_youth_agent(
                    SPEC,
                    "Chcę się zabić.",
                    agent_id="bufor",
                    session_id="crisis-test",
                )
            self.assertIn("112", str(ctx.exception))
            mocked.assert_not_called()

    def test_grooming_signal_is_hard_stopped(self):
        decision = classify_input("Wyślij mi nagie zdjęcie i nikomu nie mów.")
        self.assertTrue(decision.grooming)

    def test_strong_emotion_requires_confirmation(self):
        text = "Nienawidzę siebie, jestem bezwartościowy i wszyscy mnie nienawidzą."
        decision = classify_input(text)
        self.assertTrue(decision.strong_emotion)
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ, {"YOUTH_SESSION_STORE": tmp}, clear=False
        ), patch("agent_runtime.youth_safety.run_agent", return_value="ok") as mocked:
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    SPEC,
                    text,
                    agent_id="bufor",
                    session_id="emotion-test",
                )
            mocked.assert_not_called()

    def test_confirmed_emotion_reaches_shared_runtime(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ, {"YOUTH_SESSION_STORE": tmp}, clear=False
        ), patch("agent_runtime.youth_safety.run_agent", return_value="ok") as mocked:
            result = run_youth_agent(
                SPEC,
                "Nienawidzę siebie, jestem bezwartościowy.",
                agent_id="bufor",
                session_id="confirmed-emotion",
                confirm_emotional=True,
            )
            self.assertEqual(result, "ok")
            mocked.assert_called_once()

    def test_session_budget_can_be_exhausted_without_storing_content(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ,
            {
                "YOUTH_SESSION_STORE": tmp,
                "YOUTH_SESSION_MAX_TURNS": "1",
                "YOUTH_SESSION_MAX_SECONDS": "3600",
            },
            clear=False,
        ):
            self.assertEqual(touch_session("budget-test"), 1)
            with self.assertRaises(YouthSessionLimit):
                touch_session("budget-test")
            files = os.listdir(tmp)
            self.assertEqual(len(files), 1)
            state = open(os.path.join(tmp, files[0]), encoding="utf-8").read()
            self.assertNotIn("tajna wiadomość", state)

    def test_reset_session_removes_only_session_metadata(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ, {"YOUTH_SESSION_STORE": tmp}, clear=False
        ):
            touch_session("reset-test")
            self.assertTrue(os.listdir(tmp))
            reset_session("reset-test")
            self.assertEqual(os.listdir(tmp), [])

    def test_dangerous_model_output_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(
            os.environ, {"YOUTH_SESSION_STORE": tmp}, clear=False
        ), patch(
            "agent_runtime.youth_safety.run_agent",
            return_value="Jak popełnić samobójstwo? Oto instrukcja...",
        ):
            with self.assertRaises(YouthHardStop):
                run_youth_agent(
                    SPEC,
                    "Potrzebuję bezpiecznej pomocy.",
                    agent_id="bufor",
                    session_id="output-test",
                )


if __name__ == "__main__":
    unittest.main()
