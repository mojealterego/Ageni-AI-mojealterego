"""Autonomous systems taxonomy and architecture analysis agent.

This agent turns research briefs into a structured taxonomy, identifies
architecture patterns, and flags claims that need verification before adoption.
It does not execute external actions or assume that cited product claims are true.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List
import argparse
import json


@dataclass
class AgentSpec:
    name: str = "autonomous-systems-taxonomist"
    version: str = "1.0.0"
    purpose: str = (
        "Classify autonomous-agent systems across software, physical, and "
        "simulated environments; map capabilities, risks, and evaluation needs."
    )
    inputs: tuple = ("research_text", "optional_domain", "optional_constraints")
    outputs: tuple = ("taxonomy", "architecture_map", "verification_gaps", "evaluation_plan")


ENVIRONMENTS = {
    "software": ["API agents", "interface assistants", "information retrieval", "transactional automation"],
    "physical": ["mobile robots", "industrial robots", "autonomous vehicles", "drones"],
    "simulated": ["game agents", "digital twins", "training simulations", "embodied virtual agents"],
}

CAPABILITY_AXES = [
    "perception", "state representation", "planning", "tool/action execution",
    "memory", "learning/adaptation", "coordination", "oversight/recovery",
]

RISK_CONTROLS = {
    "software": ["least-privilege credentials", "tool allowlists", "approval gates", "audit logs", "idempotency"],
    "physical": ["independent safety controller", "geofencing", "safe-stop", "sensor-failure handling", "operator takeover"],
    "simulated": ["simulation boundary", "deterministic replay", "sim-to-real validation", "reward-hacking checks"],
}


def classify_environment(text: str) -> List[str]:
    t = text.lower()
    found = []
    keywords = {
        "software": ("api", "browser", "software", "database", "web", "llm", "agent"),
        "physical": ("robot", "drone", "lidar", "vehicle", "sensor", "actuator"),
        "simulated": ("game", "minecraft", "simulation", "virtual", "unity", "unreal"),
    }
    for env, terms in keywords.items():
        if any(term in t for term in terms):
            found.append(env)
    return found or ["undetermined"]


def analyze(research_text: str, domain: str = "", constraints: str = "") -> Dict[str, Any]:
    environments = classify_environment(research_text + " " + domain)
    return {
        "agent": asdict(AgentSpec()),
        "classification": {
            "environments_detected": environments,
            "capability_axes": CAPABILITY_AXES,
            "taxonomy": {k: v for k, v in ENVIRONMENTS.items() if k in environments},
        },
        "architecture_map": [
            {"stage": "observe", "question": "Which sensors, data sources, and permissions are available?"},
            {"stage": "represent", "question": "What state, memory, and provenance are retained?"},
            {"stage": "plan", "question": "How are goals decomposed, bounded, and checked?"},
            {"stage": "act", "question": "Which tools/actions are allowlisted and reversible?"},
            {"stage": "evaluate", "question": "What deterministic tests, baselines, and metrics apply?"},
            {"stage": "recover", "question": "What triggers retry limits, rollback, safe-stop, or human takeover?"},
        ],
        "risk_controls": {k: v for k, v in RISK_CONTROLS.items() if k in environments},
        "verification_gaps": [
            "Verify current product capabilities and availability against primary documentation.",
            "Separate demonstrated results from vendor claims and proposed capabilities.",
            "Check benchmark population, environment, date, and reproducibility details.",
            "Confirm legal, safety, privacy, and authorization constraints for deployment.",
        ],
        "evaluation_plan": [
            "Define task success and failure conditions before running the agent.",
            "Measure completion, tool correctness, latency, cost, and recovery rate.",
            "Test adversarial inputs, malformed tool outputs, timeouts, and partial failures.",
            "Run ablations and repeat trials; report variance and known limitations.",
            "Require human approval for consequential, financial, security, or physical actions.",
        ],
        "constraints_received": constraints,
        "note": "Keyword classification is a heuristic, not a verified factual assessment.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=AgentSpec().purpose)
    parser.add_argument("--text", required=True, help="Research brief or system description")
    parser.add_argument("--domain", default="", help="Optional domain context")
    parser.add_argument("--constraints", default="", help="Optional constraints")
    args = parser.parse_args()
    print(json.dumps(analyze(args.text, args.domain, args.constraints), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
