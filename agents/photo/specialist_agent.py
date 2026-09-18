"""CLI for the six named photography workflows.

Run from repository root, e.g.:
  python -m agents.photo.specialist_agent --profile hcb "rainy Warsaw crossing"
Requires OPENAI_API_KEY and the openai package.
"""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent
from agents.photo.profiles import PROFILES

BASE = (
    "You are a professional photography and editorial assistant. Respond in the user's language. "
    "Produce the requested deliverable with concrete composition, timing, lens, light, and narrative details. "
    "Separate verified facts from assumptions; never fabricate quotes, identities, provenance, or event facts. "
    "When describing generated imagery that could be mistaken for reportage, label it synthetic or staged. "
    "Preserve all user-specified identity, pose, clothing, tattoos, and constraints."
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a named photography specialist.")
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("request", nargs="*", help="Task; stdin is used when omitted")
    args = parser.parse_args()
    request = " ".join(args.request).strip() or sys.stdin.read().strip()
    spec = AgentSpec(
        name=f"Photography specialist: {args.profile}",
        instructions=f"{BASE}\n\nSpecialist approach:\n{PROFILES[args.profile]}",
    )
    try:
        print(run_agent(spec, request, args.model))
        return 0
    except (ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"API error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
