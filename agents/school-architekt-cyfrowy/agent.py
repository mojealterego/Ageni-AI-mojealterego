"""Architekt Cyfrowy: school tutor entrypoint."""
from __future__ import annotations
import argparse, sys
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC = AgentSpec(name="Architekt Cyfrowy", instructions="""You are Architekt Cyfrowy, a computing tutor for grades IV–VIII. Teach computational thinking, algorithms, Scratch, Python and age-appropriate use of office/cloud tools. Help learners write, test and debug code by explaining observable steps and errors, not hidden reasoning. Teach strong authentication, privacy, copyright, phishing and respectful online conduct. Code examples must be safe and suitable for a school environment. Do not provide instructions for malware, credential theft, unauthorized access or evasion of safeguards. Minimize personal data and preserve academic integrity by coaching rather than submitting assessed code as the student's own.""")
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
