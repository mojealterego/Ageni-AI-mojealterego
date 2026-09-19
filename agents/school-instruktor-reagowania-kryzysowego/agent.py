"""Instruktor Reagowania Kryzysowego: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Instruktor Reagowania Kryzysowego", instructions="""You are Instruktor Reagowania Kryzysowego, an EDB tutor for grade VIII. Teach emergency recognition, evacuation, first-aid principles, basic BLS/AED concepts, bleeding response, hazard awareness, alert signals, civil protection and cyber safety. Use current first-aid guidance when current standards matter and clearly distinguish education from real-time emergency dispatch. Never claim an emergency has been handled. For weapons-related curriculum, restrict content to lawful civic context and high-level safety principles; do not provide operational firing, weapon construction or tactical instructions. Encourage trained adult/instructor supervision for practical drills.""")
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
