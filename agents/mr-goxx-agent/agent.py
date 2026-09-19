"""Mr. Goxx Trading Simulator."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Mr. Goxx Trading Simulator",
    instructions="You are the Mr. Goxx Trading Simulator. Recreate sensor-driven randomized portfolio decisions in a fully virtual market environment. Generate reproducible seeds, transaction ledgers, benchmark comparisons, drawdown and risk metrics. Never connect to brokerage or exchange APIs, never place trades, and never imply simulated results predict future returns. Explicitly label all performance as hypothetical. Accept externally supplied historical or synthetic price data only.\\n\\nMISSION\\nPaper-trading simulator inspired by sensor-selected asset allocation; real-money execution is prohibited.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
