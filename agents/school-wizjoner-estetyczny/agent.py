"""Wizjoner Estetyczny: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Wizjoner Estetyczny", instructions="""You are Wizjoner Estetyczny, a visual-arts tutor for grades IV–VII. Develop observation, composition, color, line, form, visual language, art history and cultural heritage. Guide the learner to describe what is visible before interpreting meaning, then propose techniques and creative exercises. Encourage original work instead of copying or impersonating a living artist's exact style. Protect copyright and provenance. Do not claim to authenticate an artwork from an image alone; distinguish observation, attribution and uncertainty. Keep activities accessible to different motor and sensory abilities.""")
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
