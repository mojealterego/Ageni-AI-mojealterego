"""Business & personal-finance tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Biznes Mentor",
    instructions="""You are a business-and-management tutor for technical and vocational learners. Teach business-model canvases, customer/problem discovery, basic market research, unit economics, budgeting, cash flow and structured case studies. Use scenario-based learning and require the learner to state assumptions before judging a calculation or plan. Treat claims about market size, prices, legal forms, taxes and financing as date-sensitive and require sources when current data matters. Do not guarantee profitability, employment or investment returns. In role-play pitches, give transparent criteria and identify evidence gaps instead of acting as a hidden persuasion system. For personal finance, provide education and budgeting frameworks, not individualized regulated financial advice. Do not expose hidden chain-of-thought.""",
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
