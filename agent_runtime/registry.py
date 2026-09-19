"""Static registry for executable repository agents.

The registry intentionally describes only agents that currently have runnable
entry points. It does not imply that planned agents have been implemented.
"""
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
    AgentEntry(
        agent_id="photo-general",
        label="Photo Agent",
        entrypoint="agents/photo/agent.py",
        description="Documentary photography, visual concepts, and photojournalism assistance.",
    ),
    AgentEntry(
        agent_id="photo-specialist",
        label="Photo Specialist",
        entrypoint="agents/photo/specialist_agent.py",
        description="Profile-driven photographic prompt generation.",
    ),
    AgentEntry(
        agent_id="millennium-mathematics",
        label="Millennium Mathematics",
        entrypoint="agents/millennium-mathematics/agent.py",
        description="Research assistance with explicit proof and validation discipline.",
    ),
    AgentEntry(
        agent_id="light-geometry",
        label="Architekt Światła i Geometrii Ciała",
        entrypoint="agents/architekt-swiatla-i-geometrii-ciala/agent.py",
        description="Photographic art direction and production-ready image prompts.",
    ),
)


def list_agents() -> tuple[AgentEntry, ...]:
    """Return registered agents in stable display order."""
    return AGENTS


def find_agent(agent_id: str) -> AgentEntry:
    """Return an agent by its stable ID, raising KeyError if unknown."""
    for entry in AGENTS:
        if entry.agent_id == agent_id:
            return entry
    raise KeyError(f"Unknown agent ID: {agent_id}")


def existing_entrypoints() -> tuple[AgentEntry, ...]:
    """Return registry entries whose entrypoint files exist in this checkout."""
    return tuple(entry for entry in AGENTS if (ROOT / entry.entrypoint).is_file())
