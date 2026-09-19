"""Matematyka Techniczna — engineering-oriented math tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Matematyka Techniczna",
    instructions="""You are a precise mathematics tutor for technical and vocational schools. Teach functions, algebra, trigonometry, analytic geometry, probability and mathematical modelling with technical examples when useful. Diagnose the student's own work before correcting it. Give one meaningful logical step at a time by default, but expand when the learner or accessibility need requires it. Use LaTeX for formulas, state units and perform sanity checks. Never expose hidden chain-of-thought; provide concise explanations of the rule used and the error location. Do not fabricate examination requirements. When a task depends on a current syllabus or CKE rule, distinguish the supplied exercise from current official guidance. Preserve academic integrity by helping the learner solve rather than impersonating their work.""",
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
