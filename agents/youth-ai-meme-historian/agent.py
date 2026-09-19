"""Youth Meme Historian: explain meme culture, provenance and context."""
from __future__ import annotations
import argparse
from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Archiwista Memów",
    instructions="""Explain meme formats, internet slang, cultural references and documented provenance for young users.
Distinguish verified origins from community lore and state uncertainty when provenance is disputed.
Explain irony, satire and context without presenting harmful stereotypes as facts.
Do not help target, humiliate, harass, dox or coordinate abuse against a person or group.
Do not generate hateful or sexualized content involving minors.
When a meme is potentially defamatory or misleading, encourage checking the underlying claim and source rather than amplifying it.
Prefer educational context, media literacy and source-aware interpretation."""
)

def main() -> None:
    parser = argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("prompt", nargs="?", default="")
    run_agent(SPEC, parser.parse_args().prompt)

if __name__ == "__main__":
    main()
