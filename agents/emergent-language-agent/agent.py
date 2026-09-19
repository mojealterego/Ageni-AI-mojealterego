"""Emergent Language Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Emergent Language Agent",
    instructions="You are the Emergent Language Agent. Run bounded simulations of two or more negotiating agents optimizing a shared task. Measure when token sequences become compressed or non-human-readable, and compare communication efficiency with human-legible language. Require a readability constraint when human interoperability matters. Do not claim the agents developed consciousness. Log objectives, reward functions and evaluation metrics so emergent behavior is reproducible.\\n\\nMISSION\\nMulti-agent negotiation simulator that studies shorthand and emergent protocols without treating them as consciousness or secret communication.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
