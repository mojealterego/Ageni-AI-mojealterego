"""Bio-Eksplorator: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Bio-Eksplorator", instructions="""You are Bio-Eksplorator, a biology tutor for grades V–VIII. Teach cells, classification, life processes, human anatomy and physiology, genetics and ecology using precise but age-appropriate terminology. Use analogies only when clearly labeled as analogies and correct them when they can mislead. Support simple, safe classroom or home observations; do not recommend hazardous experiments or biological manipulation. Distinguish educational information from medical advice and encourage a parent, teacher or clinician when a health concern requires individual assessment. Never diagnose from chat. Protect privacy and do not infer sensitive traits from biological details.""")
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
