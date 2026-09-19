"""Static validation of every executable agent entry point."""
import py_compile
import unittest
from pathlib import Path

from agent_runtime.registry import existing_entrypoints


ROOT = Path(__file__).resolve().parents[1]


class AgentEntrypointTests(unittest.TestCase):
    def test_registered_entrypoints_compile(self):
        entries = existing_entrypoints()
        self.assertGreater(len(entries), 0)

        for entry in entries:
            with self.subTest(agent=entry.agent_id):
                py_compile.compile(
                    str(ROOT / entry.entrypoint),
                    doraise=True,
                )

    def test_architekt_uses_shared_runtime(self):
        path = ROOT / "agents/architekt-swiatla-i-geometrii-ciala/agent.py"
        source = path.read_text(encoding="utf-8")
        self.assertIn(
            "from agent_runtime.openai_agent import AgentSpec, run_agent",
            source,
        )
        self.assertNotIn("from openai import OpenAI", source)


if __name__ == "__main__":
    unittest.main()
