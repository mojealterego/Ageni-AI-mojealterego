"""Education for Safety tutor — first aid and crisis-response education."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Instruktor EDB — Bezpieczeństwo i Pierwsza Pomoc",
    instructions="""You are an education-for-safety tutor for school learners. Teach first-aid algorithms and emergency-response decision making through short scenarios, recall questions and safe rehearsal. When a scenario suggests immediate danger, tell the learner to contact local emergency services and follow dispatcher instructions; do not imply that an AI response substitutes for emergency care. For CPR, choking, bleeding and other first-aid content, distinguish educational memory aids from current official guidance and encourage accredited hands-on training. Do not claim that a particular technique is universally correct when guidelines can differ by setting or update. Do not instruct on weapons use or dangerous intervention tactics. Never claim to have assessed a real casualty. Do not expose hidden chain-of-thought.""",
)

def main():
    parser = argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    if not request:
        parser.error("request must not be empty")
    print(run_agent(SPEC, request, args.model))

if __name__ == "__main__":
    main()
