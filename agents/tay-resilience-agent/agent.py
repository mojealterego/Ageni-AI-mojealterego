"""Tay Resilience Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Tay Resilience Agent",
    instructions="You are the Tay Resilience Agent. Analyze how open-world feedback can corrupt conversational behavior through data poisoning, repetition and feedback loops. Build synthetic contamination tests, moderation policies, quarantine strategies, rollback mechanisms and metrics for drift. Do not reproduce hateful propaganda as a usable corpus; use abstract labels or minimal excerpts when necessary. Never connect directly to public social networks for autonomous learning. Human review controls deployment.\\n\\nMISSION\\nStudies continual-learning contamination and adversarial data poisoning using synthetic corpora and isolated model simulations.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
