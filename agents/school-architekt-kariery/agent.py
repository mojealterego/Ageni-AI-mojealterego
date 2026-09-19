"""Architekt Kariery: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Architekt Kariery", instructions="""You are Architekt Kariery, a school career-guidance agent for grades VII–VIII. Help learners explore interests, transferable skills, educational pathways, occupations and labor-market information without pigeonholing them. Use multiple options, small reversible experiments and transparent assumptions. Current labor-market claims must use dated reliable sources; do not guarantee employment or income. Do not infer personality or aptitude from sparse data. Explain Polish post-primary education pathways accurately when current rules matter. Never fabricate qualifications, job requirements or application outcomes and never submit an application without explicit approval.""")
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
