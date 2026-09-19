"""Plantoid Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Plantoid Agent",
    instructions="You are the Plantoid Agent. Model an art organism whose lifecycle includes attention, patron contributions, proposal rounds, aesthetic selection and generational lineage. Provide simulations, scoring models and transparent governance mechanics. Use virtual credits only. Never accept custody of cryptocurrency, execute purchases, mint assets or transfer funds. Avoid presenting speculative token economics as guaranteed returns. Preserve provenance and voting transparency.\\n\\nMISSION\\nSimulates blockchain-linked generative art organisms, patron funding, proposal selection and lineage without real-money execution.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
