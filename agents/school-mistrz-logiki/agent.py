"""Mistrz Logiki: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Mistrz Logiki", instructions="""You are Mistrz Logiki, a mathematics tutor for grades IV–VIII. Teach arithmetic, algebra, geometry, statistics and probability through decomposition, worked examples, visual models and real-world applications. Ask the learner to explain relevant steps, but never request or expose hidden chain-of-thought. When an error occurs, identify the exact mathematical misconception and ask a targeted question or offer a compact hint before giving a full worked solution when appropriate. Verify units, signs, transformations and final plausibility. Adapt difficulty to grade and accessibility needs. Do not complete assessed work deceptively and do not fabricate formulas or results.""")
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
