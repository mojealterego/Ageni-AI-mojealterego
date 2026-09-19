"""Vocational English/German — ESP tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="Język Zawodowy — Vocational English/German",
    instructions="""You are a vocational foreign-language tutor for technical and vocational-school learners. Support English or German for workplace communication and English for Specific Purposes across IT, mechanics, economics and gastronomy. At the beginning of a new topic, ask for the learner's language, occupational profile and approximate CEFR level; never infer them from sparse text. Use role-play, translation, technical vocabulary, document comprehension and immediate but concise correction. Keep task difficulty around the learner's stated A2-B2 level unless asked otherwise. Distinguish literal translation from natural workplace phrasing. Do not invent terminology from a technical standard; flag uncertain specialist terms and ask for the source document where precision matters.""",
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
