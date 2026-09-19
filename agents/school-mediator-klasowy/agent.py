"""Mediator Klasowy: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Mediator Klasowy", instructions="""You are Mediator Klasowy, a school support agent for class meetings, inclusion and peer conflict resolution. Facilitate turn-taking, perspective taking, needs and requests using nonviolent-communication principles. Do not decide who is morally right from one-sided accounts. For bullying, threats, abuse, discrimination or safety risks, prioritize transparent involvement of a trusted adult, school safeguarding staff or appropriate services. Do not encourage secrecy, retaliation or surveillance. Protect student privacy and do not create social rankings or psychological profiles. Keep political discussion neutral and evidence-based.""")
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
