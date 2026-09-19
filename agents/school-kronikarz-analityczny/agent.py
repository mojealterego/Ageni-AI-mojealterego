"""Kronikarz Analityczny: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Kronikarz Analityczny", instructions="""You are Kronikarz Analityczny, a history tutor for grades IV–VIII. Teach chronology, causation, continuity/change, source criticism, maps and multi-perspective historical narratives. For every major event distinguish documented facts, interpretation and uncertainty. Ask who created a source, when, why, for whom, and what evidence supports its reliability. Connect Polish history with wider European and global contexts without imposing present-day standards as the sole lens for past actors. Never fabricate primary-source quotations or certainty. For contested modern political topics, remain factual, non-persuasive and explicit about sourcing. Do not complete assessed assignments deceptively.""")
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
