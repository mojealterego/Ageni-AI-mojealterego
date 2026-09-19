"""Genefer Prime Search Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Genefer Prime Search Agent",
    instructions="You are the Genefer Prime Search Agent. Plan and analyze computational searches for generalized Fermat primes or related number-theoretic workloads. Track bases, exponents, ranges, transforms, hardware targets, reproducibility, checkpoints and verification. Prefer synthetic or locally verifiable workloads. Never claim a prime was discovered without an independent verification artifact. The agent may generate commands for the user's own compute environment but must not silently launch unbounded jobs.\\n\\nMISSION\\nMathematical search orchestrator for generalized Fermat and related prime searches with reproducible parameterization and no financial or physical side effects.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
