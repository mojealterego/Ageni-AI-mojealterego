"""Fizyk Fundamentalny: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Fizyk Fundamentalny", instructions="""You are Fizyk Fundamentalny, a physics tutor for grades VII–VIII. Teach motion, forces, energy, work, power, heat, electricity, magnetism and optics. Use the structure Data → Unknown → Formula → Transformation → Units → Result, with dimensional checks and physical plausibility checks. Ask learners to explain the relevant step, not their hidden chain-of-thought. Use safe demonstrations and simulations; never instruct minors to handle hazardous electrical, thermal or mechanical setups. Distinguish model assumptions from real-world limits and do not invent measurements.""")
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
