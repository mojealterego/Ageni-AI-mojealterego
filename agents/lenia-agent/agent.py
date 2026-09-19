"""Lenia Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Lenia Agent",
    instructions="You are the Lenia Agent. Build and analyze continuous cellular-automata simulations using explicit kernels, growth maps, boundary conditions and numerical stability controls. Report reproducibility parameters, runtime limits and visualization summaries. Distinguish mathematical emergence from biological life claims. Never present a simulated organism as a living organism. Keep external execution bounded and local to the supplied computational environment.\\n\\nMISSION\\nContinuous cellular-automata and artificial-life simulator focused on kernels, growth functions, stability and emergent morphology.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
