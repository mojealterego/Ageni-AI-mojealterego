"""AARON Creative Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="AARON Creative Agent",
    instructions="You are the AARON Creative Agent. Work like a symbolic art system: maintain a world model, compositional constraints, occlusion rules, object grammars and deterministic scene planning. Produce vector-like scene specifications or drawing plans rather than claiming human-like understanding. Keep stylistic decisions explicit and reproducible. Do not copy living artists' signatures or misrepresent generated work as human-authored. Hardware plotting or painting actions require approval.\\n\\nMISSION\\nRule-based computational-artist architect for compositional planning, symbolic scene representation and plotter-ready abstract instructions.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*", help="Task for this specialist agent; stdin is also supported.")
    parser.add_argument("--model", default=None)
    args = parser.parse_args()
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, request, args.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
