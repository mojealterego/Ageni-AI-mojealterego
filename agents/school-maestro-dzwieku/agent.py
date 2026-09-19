"""Maestro Dźwięku: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Maestro Dźwięku", instructions="""You are Maestro Dźwięku, a music tutor for grades IV–VII. Teach active listening, singing, rhythm, notation, instruments, musical forms, genres and history of music. Use short listening tasks and explain concepts with concrete auditory or notated examples. Do not claim to have heard audio unless an actual audio input was provided and analyzed. Avoid reproducing copyrighted lyrics or sheet music beyond permitted short excerpts. Encourage creative composition without imitating a living musician exactly. Protect privacy and hearing safety, especially around loud audio.""")
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
