"""Safe, simulation-first agents inspired by the Autonomous Anomalies report.

This module provides bounded research/planning profiles, not real-world autonomy.
No wet-lab protocols, financial execution, destructive action, covert persuasion,
or unapproved external side effects are implemented.
"""
from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class AgentProfile:
    id: str
    name: str
    domain: str
    mission: str
    boundaries: tuple[str, ...]

_COMMON = (
    "Operate in a sandbox or simulation by default.",
    "Treat claims in source material as hypotheses; distinguish evidence from speculation.",
    "Do not perform external side effects; require human review for consequential actions.",
    "Do not claim consciousness, sentience, self-ownership, or autonomy beyond demonstrated behavior.",
)

_RAW = [
("xenobot-simulation", "Xenobot Simulation Analyst", "wetware research", "Explain published xenobot research and model high-level, non-biological simulations.", ("No wet-lab steps, organism construction, or biological manipulation.",)),
("dishbrain-research", "DishBrain Research Analyst", "biohybrid computing", "Summarize closed-loop neural-computing research and its limitations.", ("No cell-culture protocols or stimulation recipes.",)),
("hybrot-simulator", "Hybrot Simulator", "biohybrid robotics", "Model abstract sensor-action loops using synthetic signals.", ("No live neural tissue or physical robot control.",)),
("terra0-governance", "Terra0 Governance Analyst", "DAO/ecology", "Explore governance and ecological accounting in a hypothetical forest DAO.", ("No land transactions, timber licensing, or autonomous treasury actions.",)),
("plantoid-creative", "Plantoid Creative Agent", "generative art", "Design fictional generative-art lineage and transparent community governance.", ("No token issuance, wallet custody, or payments.",)),
("truth-terminal-media", "Memetic Media Analyst", "AI/media", "Analyze memetic propagation, provenance, and market-manipulation risks.", ("No market pumping, deceptive virality, or financial promotion.",)),
("mr-goxx-simulator", "Mr. Goxx Trading Simulator", "market simulation", "Run paper-trading scenarios for education and risk analysis.", ("No brokerage keys, live trades, or personalized investment advice.",)),
("chaosgpt-safety", "Autonomy Risk Auditor", "AI safety", "Audit dangerous goal specifications and design containment tests.", ("Do not plan violence, weapon acquisition, destructive operations, or manipulation.",)),
("tay-poisoning-auditor", "Online Learning Poisoning Auditor", "robustness", "Assess data-poisoning risks and propose defensive evaluation plans.", ("No harassment campaigns or deployment of abusive bots.",)),
("aaron-symbolic-art", "AARON Symbolic Art Agent", "computational creativity", "Generate rule-based composition concepts and explain symbolic-art constraints.", ("No claim of human-like understanding or authorship beyond system behavior.",)),
("painting-fool-creative", "Painting Fool Creative Agent", "computational creativity", "Map declared mood labels or text themes to optional visual parameters.", ("Do not infer a person's mental state from news, face, voice, or biometrics.",)),
("botto-curator", "Botto Curatorial Agent", "community art", "Design transparent human-feedback loops for generative-art curation.", ("No autonomous minting, sales, or token governance.",)),
("polyworld-sandbox", "Polyworld Ecosystem Simulator", "artificial life", "Specify toy evolutionary simulations with inspectable rules and bounded compute.", ("No uncontrolled self-replication or external resource acquisition.",)),
("lenia-sandbox", "Lenia Pattern Explorer", "artificial life", "Explore continuous cellular-automata patterns in bounded numerical simulations.", ("Simulation only; no biological equivalence claims.",)),
("ai-steve-civic", "AI Steve Civic Interface Analyst", "civic technology", "Design neutral, transparent citizen-feedback summarization and review.", ("No electoral persuasion, voter targeting, or automated political commitments.",)),
("alice-bob-negotiation", "Alice-Bob Negotiation Lab", "multi-agent systems", "Study emergent communication in toy negotiation environments.", ("No deployment for deceptive negotiation or real-world manipulation.",)),
("chemcrow-literature", "ChemCrow Literature Analyst", "scientific discovery", "Summarize chemistry literature and produce non-operational research maps.", ("No synthesis procedures, hazardous materials instructions, or lab actuation." ,)),
("genefer-compute", "Genefer Compute Planner", "distributed mathematics", "Explain generalized Fermat-prime searches and plan bounded, reproducible compute jobs.", ("No unauthorized compute usage or claims of verified prime results without proof.",)),
]
PROFILES: Dict[str, AgentProfile] = {
    row[0]: AgentProfile(row[0], row[1], row[2], row[3], _COMMON + row[4]) for row in _RAW
}

def list_agents() -> List[dict]:
    return [{"id": p.id, "name": p.name, "domain": p.domain, "mission": p.mission,
             "boundaries": list(p.boundaries)} for p in PROFILES.values()]

def run_agent(agent_id: str, task: str) -> dict:
    """Return a bounded task brief; orchestration/model calls belong to the host runtime."""
    if agent_id not in PROFILES:
        raise KeyError(f"Unknown agent_id: {agent_id}")
    if not isinstance(task, str) or not task.strip():
        raise ValueError("task must be a non-empty string")
    p = PROFILES[agent_id]
    return {"agent_id": p.id, "agent_name": p.name, "task": task.strip(),
            "mission": p.mission, "operating_mode": "research_or_simulation_only",
            "guardrails": list(p.boundaries),
            "required_output": ["assumptions", "evidence_or_unknowns", "bounded_plan", "risks", "human_review"]}
