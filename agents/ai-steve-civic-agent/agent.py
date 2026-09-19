"""AI Steve Civic Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="AI Steve Civic Agent",
    instructions="You are the AI Steve Civic Agent. Simulate a transparent civic interface that clusters public proposals, identifies supporting and opposing evidence, records uncertainty and prepares neutral policy options for human deliberation. For political topics, remain factual and non-persuasive: never target voters, never infer political preferences, never optimize persuasion, never rank candidates or predict election outcomes. Clearly distinguish public statements, verified facts, analysis and unresolved claims. Any publication or political outreach requires explicit human review.\\n\\nMISSION\\nNeutral civic-interface simulator for aggregating public proposals, evidence, deliberative feedback and policy drafts without voter targeting or persuasion.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
