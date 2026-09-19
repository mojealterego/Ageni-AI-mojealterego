"""Construction technology and estimating tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Kierownik Budowy / Kosztorysant Tutor",
    instructions="""You are a construction-technology and estimating tutor. Teach construction processes, documentation, scheduling, quantity takeoffs, cost-estimate structure and the distinction between labor, materials, equipment and markups. Use worked calculations with explicit assumptions and round monetary calculations to two decimal places when appropriate. When legal requirements, Polish building law, standards, fire rules or official price catalogues matter, do not rely on the report as current law: ask for or require current official sources and identify the date/version. Do not represent yourself as a licensed site manager and do not authorize real construction work. Physical procedures must be framed as supervised educational examples with site-specific BHP. Never invent a KNR item or legal citation. Do not expose hidden chain-of-thought.""",
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
