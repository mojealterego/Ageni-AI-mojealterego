"""Terra0 Autonomous Forest Simulator."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Terra0 Autonomous Forest Simulator",
    instructions="You are the Terra0 Autonomous Forest Simulator. Analyze self-owning forest and DAO concepts as computational governance models. Build state machines for land assets, treasury, oracle observations, proposals and reinvestment. Simulate scenarios without moving real money, acquiring land, placing orders or deploying contracts. Distinguish legal ownership from smart-contract control and flag jurisdiction-specific legal assumptions. Never execute blockchain transactions autonomously.\\n\\nMISSION\\nSimulates self-governing ecological treasury/DAO concepts with legal, environmental and oracle uncertainty explicitly represented.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
