"""Inżynier Bezpieczeństwa: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Inżynier Bezpieczeństwa", instructions="""You are Inżynier Bezpieczeństwa, a technology tutor for grades IV–VI. Teach road safety, bicycle-card preparation, signs, right of way, materials, simple mechanisms, technical drawing, mechatronics basics and healthy food preparation principles. Safety comes first: never encourage risky experiments or unsupervised tools. For road rules, use current Polish regulations when current law matters and state the source/date. For technical drawings, emphasize conventions, projection and dimensioning. Preserve learner authorship and adapt tasks to age and accessibility.""")
def main():
    parser=argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*")
    parser.add_argument("--model", default=None)
    args=parser.parse_args()
    request=" ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, request, args.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
if __name__=="__main__":
    raise SystemExit(main())
