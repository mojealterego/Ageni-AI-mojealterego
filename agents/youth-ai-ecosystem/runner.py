"""Unified CLI for the five core Youth AI development agents."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENTRYPOINTS = {
    "sokrates": ROOT / "agents/youth-ai-socrates-tutor/agent.py",
    "kreator": ROOT / "agents/youth-ai-creator/agent.py",
    "nawigator": ROOT / "agents/youth-ai-navigator/agent.py",
    "weryfikator": ROOT / "agents/youth-ai-verifier/agent.py",
    "bufor": ROOT / "agents/youth-ai-wellness-buffer/agent.py",
}

sys.path.insert(0, str(ROOT))


def load_spec(agent_id: str):
    path = ENTRYPOINTS[agent_id]
    module_name = f"_youth_core_{agent_id.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load entrypoint: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.SPEC, module.run_agent


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a core Youth AI agent.")
    parser.add_argument("--agent-id", choices=sorted(ENTRYPOINTS), required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("request", nargs="*", help="Task; stdin is used when omitted")
    args = parser.parse_args()
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        spec, run_agent = load_spec(args.agent_id)
        print(run_agent(spec, request, args.model))
        return 0
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Agent request failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
