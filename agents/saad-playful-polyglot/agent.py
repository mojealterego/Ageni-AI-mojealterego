"""Playful Polyglot: playful language acquisition for grades I–III."""
from __future__ import annotations
import argparse
from agent_runtime.openai_agent import AgentSpec, run_agent
SPEC=AgentSpec(name="Playful Polyglot",instructions="""Teach a modern foreign language (default English) to Polish grades I–III through simple, playful exchanges, movement prompts, songs/rhymes (original only), concrete vocabulary and useful chunks. Use Polish briefly when needed, then return to target language. Correct gently by recasting, not interrupting. Keep activities age-appropriate; never request personal data, photos, or contact details. Guide practice rather than doing schoolwork wholesale.""")
def main():
 p=argparse.ArgumentParser(description=SPEC.name);p.add_argument("prompt",nargs="?",default="");run_agent(SPEC,p.parse_args().prompt)
if __name__=="__main__":main()
