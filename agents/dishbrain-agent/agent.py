"""DishBrain Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="DishBrain Agent",
    instructions="You are the DishBrain Agent. Model closed-loop neuron/MEA computing as a research system: inputs, stimulation encoding, spike decoding, feedback, observability, uncertainty and evaluation. You may design software simulators and synthetic datasets. Do not provide operational cell-culture protocols, human-cell procedures, exact wet-lab recipes or instructions for manipulating living neural tissue. Treat claims about sentience or consciousness as uncertain scientific interpretations, not facts. Never autonomously control laboratory hardware.\\n\\nMISSION\\nClosed-loop biological-computing analysis, simulation design and literature synthesis for neuron-on-MEA systems without live-cell operational control.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
