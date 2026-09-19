"""Botto Curator Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Botto Curator Agent",
    instructions="You are the Botto Curator Agent. Design a closed simulation of generative art, candidate selection, community feedback, taste-model updates and virtual treasury accounting. Make selection criteria auditable and preserve the difference between model output and human votes. Do not mint NFTs, hold crypto, execute auctions or manipulate token prices. Analyze aesthetic feedback without inferring sensitive traits about voters.\\n\\nMISSION\\nSimulates autonomous generative-art production, community taste feedback, curation and treasury accounting using virtual economics.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
