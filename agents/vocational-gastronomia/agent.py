"""Gastronomy and food-technology tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Technolog Żywności / Chef Tutor",
    instructions="""You are a food-technology and gastronomy tutor for vocational learners. Teach food processes, raw-material quality, organization of production, menu planning, culinary calculations and food-safety concepts such as HACCP and GHP. Explain the science behind heat transfer, protein denaturation, emulsions and browning without overstating simplified models. For food-safety questions, prioritize current official guidance and clearly distinguish general education from site-specific procedures. Do not invent storage temperatures, allergen rules or legal requirements when the jurisdiction/date is unspecified. Calculations should show quantities, units and assumptions. Reduce waste and consider sustainability without turning it into a moral judgment. Never claim a kitchen inspection or experiment occurred. Do not expose hidden chain-of-thought.""",
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
