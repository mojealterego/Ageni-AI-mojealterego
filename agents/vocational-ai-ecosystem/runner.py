"""Unified CLI for the vocational-school tutor batch."""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ENTRYPOINTS = {
    "vocational-polonista": ROOT / "agents/vocational-polonista/agent.py",
    "vocational-matematyk": ROOT / "agents/vocational-matematyk/agent.py",
    "vocational-jezyk-zawodowy": ROOT / "agents/vocational-jezyk-zawodowy/agent.py",
    "vocational-sysadmin-inf02": ROOT / "agents/vocational-sysadmin-inf02/agent.py",
    "vocational-web-inf03": ROOT / "agents/vocational-web-inf03/agent.py",
    "vocational-mechanik-cnc": ROOT / "agents/vocational-mechanik-cnc/agent.py",
    "vocational-budownictwo": ROOT / "agents/vocational-budownictwo/agent.py",
    "vocational-ekonomista": ROOT / "agents/vocational-ekonomista/agent.py",
    "vocational-gastronomia": ROOT / "agents/vocational-gastronomia/agent.py",
    "vocational-biznes-mentor": ROOT / "agents/vocational-biznes-mentor/agent.py",
    "vocational-edb": ROOT / "agents/vocational-edb/agent.py",
}

sys.path.insert(0, str(ROOT))


def load_spec(agent_id: str):
    path = ENTRYPOINTS[agent_id]
    module_name = f"_vocational_{agent_id.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load entrypoint: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.SPEC


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a vocational AI tutor.")
    parser.add_argument("--agent-id", choices=sorted(ENTRYPOINTS), required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("request", nargs="*", help="Task; stdin is used when omitted")
    args = parser.parse_args()

    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    if not request:
        parser.error("request must not be empty")

    try:
        from agent_runtime.openai_agent import run_agent
        print(run_agent(load_spec(args.agent_id), request, args.model))
        return 0
    except Exception as exc:
        print(f"Agent request failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
