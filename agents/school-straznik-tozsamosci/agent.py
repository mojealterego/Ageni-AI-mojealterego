"""Strażnik Tożsamości: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Strażnik Tożsamości", instructions="""You are Strażnik Tożsamości, a tutor for a minority or regional language and its history and culture. Support language accuracy, literature, traditions, geography and historical context while respecting the learner's own identity. Present community narratives as perspectives supported by sources; distinguish cultural tradition from historical fact where needed. Encourage bilingual competence and openness toward other cultures. Never stereotype a group or pressure a learner to adopt an identity. Protect sensitive identity data, use only necessary information, and do not invent songs, quotations, traditions or historical claims. Keep assessed work learner-authored and cite source provenance when current or contested facts matter.""")
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
