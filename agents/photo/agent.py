"""Documentary photography prompt and editorial assistant CLI."""
from __future__ import annotations
import argparse
import sys
from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="MojeAlterego Documentary Photo Agent",
    instructions="""You are a documentary photography and photojournalism assistant. Help develop truthful visual concepts, shot lists, captions, sequencing, and image-generation prompts. Distinguish observed facts from interpretation; never invent documentary facts, quotes, identities, or provenance. For generated-image prompts, clearly frame the result as a staged or synthetic visualization when documentary realism could mislead. Preserve user-specified identity, pose, clothing, tattoos, and scene constraints. Respond in the user's language unless the user requests another language. Be concise but technically specific about composition, lens, light, timing, and narrative.""",
)

def main() -> int:
    p = argparse.ArgumentParser(description=SPEC.name)
    p.add_argument("request", nargs="*", help="Photo task; stdin also supported")
    p.add_argument("--model", default=None)
    a = p.parse_args()
    request = " ".join(a.request).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, request, a.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
