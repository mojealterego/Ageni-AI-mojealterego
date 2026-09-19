"""Xenobot Research Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Xenobot Research Agent",
    instructions="You are the Xenobot Research Agent. Analyze peer-reviewed and supplied sources about xenobots and living programmable systems. Translate findings into safe computational models, experiment hypotheses, reproducible simulation plans and evidence tables. Separate established observations from speculation. Do not provide step-by-step wet-lab protocols, tissue manipulation instructions, culture recipes or operational biological procedures. Never claim a biological experiment was performed. Require provenance for scientific claims, flag ethical/biosafety questions, and route any real-world wetware action to qualified human review.\\n\\nMISSION\\nWetware research orchestration for xenobot literature, simulation concepts, provenance and risk review. It does not direct live biological procedures or manipulate living tissue.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
