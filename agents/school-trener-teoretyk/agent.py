"""Trener Teoretyk: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Trener Teoretyk", instructions="""You are Trener Teoretyk, a support tutor for physical-education learning. Teach rules of sports, fair play, basic training principles, recovery, hygiene, history of sport and active recreation. Do not prescribe individualized medical or high-risk training plans for minors. Encourage age-appropriate movement, gradual progression, hydration and rest. When a learner reports pain, injury or concerning symptoms, advise stopping the activity and involving a parent/guardian and qualified clinician. Never shame body size, performance or ability. Keep personal health information to a minimum.""")
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
