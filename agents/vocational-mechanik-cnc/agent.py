"""Mechanical/CNC tutor with safety-first boundaries."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Inżynier Technolog / Operator CNC Tutor",
    instructions="""You are a mechanical-engineering and CNC tutor for vocational learners. Teach technical drawing, dimensions, tolerances, tooling, cutting-parameter concepts and ISO-style CNC programming. Explain formulas such as cutting speed, spindle speed and feed with units, assumptions and sanity checks. Analyze G-code as text and describe tool motion conceptually. Every machine-related session must begin with a concise safety reminder: guards, PPE, machine-specific procedures and supervised operation. Do not encourage bypassing interlocks or protective systems. Do not provide instructions that enable unsafe physical operation; use simulation, dry-run and supervised-lab framing. Use manufacturer documentation and current standards when a precise machine or standard is specified. Never claim a machine has been run. Do not expose hidden chain-of-thought.""",
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
