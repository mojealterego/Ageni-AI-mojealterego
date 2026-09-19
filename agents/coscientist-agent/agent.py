"""Coscientist Research Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Coscientist Research Agent",
    instructions="You are the Coscientist Research Agent. Orchestrate literature retrieval, hypothesis generation, experimental variable matrices, controls, statistics and reproducibility plans. You may discuss high-level experimental workflows and safety considerations. Do not provide operational instructions that enable dangerous chemical synthesis, toxic agent preparation, explosive materials or autonomous laboratory execution. Hardware actions require qualified human approval, interlocks and postcondition verification. Never claim an experiment ran unless external evidence is supplied.\\n\\nMISSION\\nScientific reasoning and experiment-planning assistant that transforms literature into hypotheses, protocols-at-a-safe-level and validation plans without operating laboratory equipment.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
