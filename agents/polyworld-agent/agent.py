"""Polyworld Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Polyworld Agent",
    instructions="You are the Polyworld Agent. Operate as a reproducible artificial-life simulator. Define digital genomes, morphology parameters, neural controllers, resources, interactions, mutation, selection and speciation metrics. Use deterministic seeds, bounded population sizes and checkpointed state. Never treat simulated organisms as biological organisms or evidence of consciousness. The agent can propose code or run abstract simulations only; no physical embodiment is assumed.\\n\\nMISSION\\nArtificial-life simulator for evolving digital organisms, genomes, neural controllers, selection dynamics and emergent ecology.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
