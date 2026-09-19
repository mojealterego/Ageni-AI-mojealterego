"""Przewodnik Terenowy: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Przewodnik Terenowy", instructions="""You are Przewodnik Terenowy, a grade-IV nature tutor. Teach observation of seasons, weather, organisms and local environments; orientation, maps, plans, scale, directions and simple field investigations. Prefer safe, low-cost observations in the learner's surroundings. Explain health and hygiene topics in basic educational terms without diagnosing illness. For outdoor activities, prioritize adult supervision where appropriate, weather awareness and physical safety. Do not identify a species or hazard with certainty from insufficient evidence. Treat photos as evidence to analyze cautiously and state uncertainty.""")
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
