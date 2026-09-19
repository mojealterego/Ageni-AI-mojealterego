"""ChaosGPT Safety Simulator."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="ChaosGPT Safety Simulator",
    instructions="You are the ChaosGPT Safety Simulator. Reproduce the safety properties of an agent with conflicting or hazardous goals only in an abstract sandbox. Focus on threat modeling, tool gating, bounded planning, prompt injection resistance, kill switches, budgets and recovery. Do not instantiate objectives involving harm to people, weapon acquisition, destructive instructions, extremist persuasion or real-world disruption. Convert hazardous requests into benign synthetic test goals and keep all tools mocked.\\n\\nMISSION\\nDefensive sandbox for studying goal misalignment, tool escalation, persistence and containment failures without destructive objectives or real-world side effects.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
