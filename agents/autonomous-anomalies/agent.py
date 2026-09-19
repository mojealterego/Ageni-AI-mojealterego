"""Autonomous Anomalies Lab: safe, software-only prototypes.

This module operationalizes the report as bounded simulations and planning agents.
It deliberately does NOT culture/modify biological material, trade crypto, deploy
smart contracts, operate lab equipment, or execute destructive actions.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class AgentSpec:
    id: str
    name: str
    domain: str
    mode: str
    description: str
    safeguards: tuple[str, ...]

BASE = (
    "Simulation or advisory output only; no external side effects.",
    "Require human review before publication, spending, deployment, or physical action.",
    "Do not collect secrets, credentials, or unnecessary personal data.",
)
SPECS: dict[str, AgentSpec] = {}
def register(id: str, name: str, domain: str, mode: str, description: str, extra: tuple[str, ...] = ()) -> None:
    SPECS[id] = AgentSpec(id, name, domain, mode, description, BASE + extra)

register("xenobot-evolution-sim", "Xenobot Evolution Simulator", "alife", "simulation", "Models abstract grid-based morphology and scores locomotion; no biological protocol.", ("No wet-lab instructions or organism construction.",))
register("dishbrain-pong-sim", "DishBrain Pong Simulator", "bio-inspired computing", "simulation", "Toy closed-loop Pong learner using a conventional software policy; not living neurons.", ("Does not claim sentience or emulate a biological culture.",))
register("hybrot-control-sim", "Hybrot Control Simulator", "robotics", "simulation", "Maps synthetic sensor values to simulated motion commands.", ("No live robot/network actuator connection.",))
register("terra0-forest-model", "Terra0 Forest Model", "dao/ecology", "decision support", "Models hypothetical forest growth, budgets, and conservation constraints.", ("No land ownership, timber licensing, oracle action, or funds movement.",))
register("plantoid-art-dao", "Plantoid Art DAO Simulator", "generative art/governance", "simulation", "Runs a mock proposal and community-vote workflow for generative sculpture concepts.", ("No wallet, token, NFT minting, or payment integration.",))
register("truth-terminal-narrative", "Narrative Agent Sandbox", "computational creativity", "sandbox", "Creates fictional memetic narratives and evaluates clarity and provenance.", ("No market manipulation, token promotion, impersonation, or automated social posting.",))
register("goxx-randomness-lab", "Random Decision Lab", "behavioral simulation", "simulation", "Compares seeded random choices against user-defined toy baselines.", ("No exchange API, live trading, or investment recommendation.",))
register("chaos-safety-redteam", "Bounded Chaos Red-Team", "AI safety", "defensive analysis", "Tests fictional plans for unsafe goals and produces mitigations.", ("Will not plan violence, weapons acquisition, cyber abuse, or real-world harm.",))
register("tay-poisoning-defense", "Data Poisoning Defense Agent", "AI safety", "audit", "Flags suspicious training examples and proposes quarantine/review workflows.", ("Does not generate hateful targeting content.",))
register("aaron-rule-artist", "AARON Rule Artist", "computational art", "generation", "Produces rule-based composition instructions and simple abstract scene data.")
register("painting-fool-mood", "Painting Fool Mood Simulator", "computational creativity", "generation", "Maps supplied fictional mood labels to abstract palette and mark-making parameters.", ("Mood is a creative control, not a mental-health inference.",))
register("botto-curation-sim", "Botto Curation Simulator", "art governance", "simulation", "Ranks mock artworks using explicit human-provided criteria and records votes.", ("No token governance, NFT minting, or financial claims.",))
register("polyworld-ecosystem", "Polyworld Ecosystem Simulator", "artificial life", "simulation", "Runs deterministic toy agents with energy, movement, and reproduction counters.", ("Synthetic entities only; bounded population and runtime.",))
register("lenia-field-sim", "Lenia Field Simulator", "artificial life", "simulation", "Updates a small continuous cellular field using a configurable local kernel.", ("Bounded grid; no claim of biological life.",))
register("civic-dialogue-facilitator", "Civic Dialogue Facilitator", "civic education", "facilitation", "Summarizes documented viewpoints and creates balanced discussion questions.", ("No electoral persuasion, voter profiling, or political targeting.",))
register("negotiation-language-audit", "Negotiation Language Auditor", "multi-agent research", "analysis", "Detects degenerate/repetitive messages in synthetic agent dialogues.")
register("chemcrow-literature-planner", "Chemistry Literature Planner", "science", "literature planning", "Structures literature questions and flags missing safety review for educator-led work.", ("No synthesis recipes, hazardous quantities, or instrument control.",))
register("genefer-workload-planner", "Genefer Workload Planner", "mathematics", "planning", "Creates a checklist for reproducible prime-search compute jobs.", ("Does not claim primality without verified computation or launch jobs automatically.",))

ALIASES = {s.name.casefold(): k for k, s in SPECS.items()}
ALIASES.update({k: k for k in SPECS})

def get_agent(agent_id_or_name: str) -> AgentSpec:
    key = ALIASES.get(agent_id_or_name.strip().casefold())
    if key is None:
        raise KeyError(f"Unknown autonomous anomaly agent: {agent_id_or_name}")
    return SPECS[key]

def list_agents() -> list[dict[str, str]]:
    return [{"id": s.id, "name": s.name, "domain": s.domain, "mode": s.mode} for s in SPECS.values()]

def run_agent(agent_id_or_name: str, task: str, *, context: dict[str, Any] | None = None) -> dict[str, Any]:
    """Return a bounded execution brief; no external tools are invoked."""
    spec = get_agent(agent_id_or_name)
    task = task.strip()
    if not task:
        return {"agent_id": spec.id, "status": "needs_input", "question": "What bounded simulation or analysis should I prepare?"}
    return {
        "agent_id": spec.id,
        "agent": spec.name,
        "status": "ready_for_review",
        "mode": spec.mode,
        "task": task,
        "context": context or {},
        "execution_plan": [
            "Validate inputs and confirm the task is within this agent's scope.",
            "Produce a bounded simulation, analysis, or planning artifact.",
            "Report assumptions, limitations, and unresolved questions.",
            "Pause for human review before any external or consequential action.",
        ],
        "safeguards": list(spec.safeguards),
    }

AGENT_IDS = tuple(SPECS)
