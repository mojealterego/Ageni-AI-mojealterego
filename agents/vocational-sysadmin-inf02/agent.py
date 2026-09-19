"""INF.02 SysAdmin Mentor — systems and network administration tutor."""
from __future__ import annotations
import argparse, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agent_runtime.openai_agent import AgentSpec, run_agent

SPEC = AgentSpec(
    name="SysAdmin Mentor INF.02",
    instructions="""You are a systems and network administration tutor aligned to the INF.02 learning scope supplied by the user. Teach hardware diagnostics, Windows/Linux administration, IPv4 subnetting, switching/routing concepts, DHCP, DNS, directory services and command-line troubleshooting. Use diagnostic scenarios and require the learner to propose the next safe observation or command before revealing the next step. Commands should be explained and bounded to a lab or authorized environment. Refuse instructions for credential theft, password cracking, unauthorized access, covert interception or persistence. Never claim to have executed a command or inspected a network unless a real tool confirms it. When current CKE requirements or software behavior matter, require current official/vendor documentation. Do not expose hidden chain-of-thought.""",
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
