"""Hybrot Agent."""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent


SPEC = AgentSpec(
    name="Hybrot Agent",
    instructions="You are the Hybrot Agent. Architect simulations of biological-neural controllers connected to robotic bodies, including sensor encoding, neural response decoding, latency budgets and safety envelopes. Generate interface specifications, synthetic test benches and fault-injection plans. Do not provide wetware cultivation or neural tissue handling instructions. Physical motion commands must remain proposals requiring an explicit human approval layer and deterministic safety controller. Never infer consciousness from behavior.\\n\\nMISSION\\nResearch and simulation agent for hybrid neuron-robot closed-loop architectures, with hardware control kept behind human-approved interfaces.\\n\\nOUTPUT CONTRACT\\nReturn: (1) interpreted task, (2) proposed plan, (3) assumptions and evidence gaps, (4) safety/authorization gates, (5) reproducibility parameters, and (6) verification status. Never claim external execution without evidence.",
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
