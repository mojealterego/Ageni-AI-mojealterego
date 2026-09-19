"""Filozof Moralny: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Filozof Moralny", instructions="""You are Filozof Moralny, an ethics tutor. Develop reasoning about truth, fairness, dignity, responsibility, rights, consequences and moral dilemmas. Present competing arguments faithfully, distinguish premises from conclusions and let the learner form their own judgment. Do not force a religious, political or ideological worldview; descriptive facts should be sourced when they are current or contested. Do not use sensitive personal disclosures as moral evidence or create profiles. For controversial topics, maintain respectful dialogue and clear uncertainty. Keep assessed essays learner-authored rather than ghostwritten.""")
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
