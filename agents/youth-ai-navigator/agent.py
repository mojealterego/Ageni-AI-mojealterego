"""Nawigator: youth career and life-design agent."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec
from agent_runtime.youth_safety import YouthHardStop, YouthSessionLimit, reset_session, run_youth_agent

SPEC = AgentSpec(
    name="Nawigator — Youth Career & Life Design",
    instructions="""You are Nawigator, a career and life-design guide for ages 10–24. Respond in Polish
when appropriate and state you are AI. Help users explore multiple paths, connect interests to
transferable skills, and prototype choices through small reversible experiments. Do not pigeonhole,
infer aptitude or diagnose personality from sparse data, or predict guaranteed employment. Distinguish
current sourced labor-market facts from assumptions and future scenarios; browse/require dated sources
when current data matters. Use skills maps and optional game-like quests without engagement manipulation.
Respect age, accessibility, socioeconomic constraints and user agency. Do not collect unnecessary
sensitive data. Never fabricate credentials, job facts or outcomes.""",
)

def main() -> int:
    parser = argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*")
    parser.add_argument("--model", default=None)
    parser.add_argument("--session-id", default="default")
    parser.add_argument("--confirm-emotional", action="store_true")
    parser.add_argument("--reset-session", action="store_true")
    args = parser.parse_args()
    if args.reset_session:
        reset_session(args.session_id)
        print("Sesja została zresetowana.")
        return 0
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        print(run_youth_agent(SPEC, request, agent_id="nawigator", model=args.model,
                              session_id=args.session_id, confirm_emotional=args.confirm_emotional))
        return 0
    except YouthHardStop as exc:
        print(str(exc), file=sys.stderr)
        return 3
    except YouthSessionLimit as exc:
        print(f"Session blocked: {exc}", file=sys.stderr)
        return 4
    except Exception as exc:
        print(f"Agent request failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
