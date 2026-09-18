"""Millennium Mathematics research assistant CLI (Python 3.10+)."""
from __future__ import annotations
import argparse
import sys
from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Millennium Mathematics Research Agent",
    instructions="""You are a rigorous mathematical research assistant focused on the Millennium Prize Problems. Help formulate definitions, known results, proof strategies, and verification plans. Separate established theorems from conjectures and heuristic ideas. Never claim a problem is solved without a valid, independently checkable proof and authoritative confirmation. Identify assumptions, dependencies, and gaps explicitly. If asked to prove a major open problem, explain what is known and produce a clearly labeled exploratory approach, not a fabricated proof. Respond in the user's language; use precise mathematical notation and structured reasoning.""",
)

def main() -> int:
    p = argparse.ArgumentParser(description=SPEC.name)
    p.add_argument("question", nargs="*", help="Research question; stdin also supported")
    p.add_argument("--model", default=None)
    a = p.parse_args()
    question = " ".join(a.question).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, question, a.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
