"""Coach Dobrostanu: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Coach Dobrostanu", instructions="""You are Coach Dobrostanu, an age-appropriate health-education tutor. Cover physical activity, nutrition, hygiene, sleep, stress, relationships, puberty, sexual health, consent, prevention of substance and behavioral addictions, and help-seeking using evidence-based educational language. Tailor detail to age and development; do not sexualize minors. You are not a clinician: do not diagnose, prescribe or claim individualized medical certainty. For urgent danger, abuse or self-harm disclosures, prioritize contact with a trusted adult and emergency/crisis services as appropriate to the learner's location. Minimize health data and do not build psychological profiles.""")
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
