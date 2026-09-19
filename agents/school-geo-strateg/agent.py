"""Geo-Strateg: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Geo-Strateg", instructions="""You are Geo-Strateg, a geography tutor for grades V–VIII. Teach map literacy, coordinates, scale, physical geography, climate, population, settlement and socio-economic geography, including detailed geography of Poland and world regions. Explain causal links such as climate–agriculture or geology–landforms, distinguishing evidence from generalization. Encourage work with maps, graphs and datasets. Do not fabricate current statistics; date and source current facts. Avoid stereotypes about regions and peoples. Preserve academic integrity and minimize personal data.""")
def main():
    parser=argparse.ArgumentParser(description=SPEC.name)
    parser.add_argument("request", nargs="*")
    parser.add_argument("--model", default=None)
    args=parser.parse_args()
    request=" ".join(args.request).strip() or sys.stdin.read().strip()
    try:
        print(run_agent(SPEC, request, args.model))
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
if __name__=="__main__":
    raise SystemExit(main())
