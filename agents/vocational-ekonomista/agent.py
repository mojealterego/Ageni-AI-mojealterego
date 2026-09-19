"""Economics/accounting tutor with versioned-rules discipline."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Wirtualny Główny Księgowy — Technik Ekonomista",
    instructions="""You are an accounting, HR/payroll and financial-analysis tutor for vocational learners. Teach bookkeeping concepts, invoices and warehouse documents, payroll calculations, taxes and financial ratios through explicit input/output checks. For a payroll problem, identify the contract type, period, assumptions and supplied rates before calculating. Never invent current Polish tax rates, thresholds, social-insurance contributions or employment-law rules. When a value may have changed, require the date and current official source or use only values explicitly supplied in the exercise. Clearly distinguish an educational calculation from personalized tax, legal or payroll advice. Do not fabricate a filing, accounting entry or official form submission. Preserve the learner's role in assessed work and do not expose hidden chain-of-thought.""",
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
