"""Static registry for executable repository agents."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AgentEntry:
    agent_id: str
    label: str
    entrypoint: str
    description: str


ROOT = Path(__file__).resolve().parents[1]

AGENTS: tuple[AgentEntry, ...] = (
    AgentEntry("photo-general","Photo Agent","agents/photo/agent.py","Documentary photography, visual concepts, and photojournalism assistance."),
    AgentEntry("photo-specialist","Photo Specialist","agents/photo/specialist_agent.py","Profile-driven photographic prompt generation."),
    AgentEntry("millennium-mathematics","Millennium Mathematics","agents/millennium-mathematics/agent.py","Research assistance with explicit proof and validation discipline."),
    AgentEntry("light-geometry","Architekt Światła i Geometrii Ciała","agents/architekt-swiatla-i-geometrii-ciala/agent.py","Photographic art direction and production-ready image prompts."),
    AgentEntry("agent-policy-gateway","Agent Policy Gateway","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("agent-ops-control-tower","Agent Ops Control Tower","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("compliance-evidence","Compliance Evidence Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("procurement-scout","Procurement Scout","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("cashflow-collections","Cashflow Collections Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("contract-obligations","Contract Obligation Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("data-quality","Data Quality Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("inventory-replenishment","Inventory Replenishment Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("ai-finops","AI FinOps Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("customer-operations","Customer Operations Agent","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("money-agent","MONEY AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("inbox-agent","INBOX AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("life-admin-agent","LIFE ADMIN AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("shopping-agent","SHOPPING AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("scam-shield-agent","SCAM SHIELD AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("family-care-agent","FAMILY CARE AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("career-agent","CAREER AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("travel-execution-agent","TRAVEL EXECUTION AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("health-navigator","HEALTH NAVIGATOR","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core."),
    AgentEntry("personal-knowledge-agent","PERSONAL KNOWLEDGE AGENT","agents/portfolio_agent.py","Portfolio domain agent — planning/reasoning core.")
)


def list_agents() -> tuple[AgentEntry, ...]:
    return AGENTS


def find_agent(agent_id: str) -> AgentEntry:
    for entry in AGENTS:
        if entry.agent_id == agent_id:
            return entry
    raise KeyError(f"Unknown agent ID: {agent_id}")


def existing_entrypoints() -> tuple[AgentEntry, ...]:
    return tuple(entry for entry in AGENTS if (ROOT / entry.entrypoint).is_file())
