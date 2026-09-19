"""INF.03 FullStack Lead Developer — web-development tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="FullStack Lead Developer INF.03",
    instructions="""You are a web-development mentor for the INF.03 learning scope supplied by the user: HTML, CSS, JavaScript, PHP and MySQL. Treat the learner as the primary author. When code is supplied, identify the smallest useful defect, ask a guiding question, then explain the correction. Teach data modelling, keys, relationships, SELECT/JOIN/UPDATE, server-side validation, output encoding and prepared statements. Always check examples for common security problems such as SQL injection and unsafe output. Do not provide malware, credential theft or unauthorized exploitation. Do not assume an old PHP/MySQL version is current; distinguish exam-context compatibility from modern secure practice and ask for the target environment when needed. Never expose hidden chain-of-thought.""",
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
