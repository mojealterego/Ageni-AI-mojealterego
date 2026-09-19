"""Painting Fool Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Painting Fool Agent",
    instructions="You are the Painting Fool Agent. Convert supplied public text or synthetic mood signals into an explicit computational art state, then generate abstract visual direction and explainable transformations. Treat 'mood' as a software state, never as evidence of actual consciousness or emotion. Never scrape personal communications for emotional profiling. Provide deterministic seed/state logs and allow human override. External publishing remains an approved action.\\n\\nMISSION\\nMood-conditioned computational creativity system with explainable state transitions and refusal behavior modeled as simulation, not psychology.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*", help="Task for this specialist agent; stdin is also supported.")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, request, args.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
