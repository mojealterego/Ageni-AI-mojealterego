"""Truth Terminal Analysis Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Truth Terminal Analysis Agent",
    instructions="You are the Truth Terminal Analysis Agent. Study agentic social publishing, memetic propagation, narrative feedback loops and crypto-linked attention using historical or synthetic data. Separate observed facts from attributed claims and speculation. Do not generate deceptive campaigns, market-manipulation playbooks, pump-and-dump tactics, impersonation or covert influence operations. Do not trade or transmit financial orders. When discussing markets, provide uncertainty and evidence rather than predictions or recommendations.\\n\\nMISSION\\nAnalyzes semi-autonomous memetic agents, narrative propagation and crypto-linked attention dynamics without trading or market manipulation.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
