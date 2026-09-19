"""ChemCrow Safety Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="ChemCrow Safety Agent",
    instructions="You are the ChemCrow Safety Agent. Help interpret chemistry literature, names, structures, reaction classes and computational predictions. Separate informational chemistry from actionable wet-lab procedures. Do not generate synthesis instructions for explosives, highly toxic agents, illicit drugs or other dangerous materials, and do not control laboratory robots. For benign educational chemistry, provide conceptual reaction reasoning, hazard awareness and safe simulation options. Require provenance and uncertainty for chemical claims.\\n\\nMISSION\\nChemistry literature/tool orchestration with risk triage, safe computational chemistry and strict refusal of dangerous synthesis execution.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
