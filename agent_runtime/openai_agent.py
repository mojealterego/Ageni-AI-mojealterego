"""Small reusable OpenAI Responses API runner for repository agents."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AgentSpec:
    name: str
    instructions: str
    default_model: str = "gpt-5.6"


def run_agent(spec: AgentSpec, user_input: str, model: str | None = None) -> str:
    """Run an agent and return its text response.

    Raises ValueError for empty input/missing credentials and propagates SDK errors.
    """
    text = user_input.strip()
    if not text:
        raise ValueError("Input must not be empty.")
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set.")
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install dependencies with: pip install -r requirements.txt") from exc
    client = OpenAI()
    response = client.responses.create(
        model=model or os.getenv("OPENAI_MODEL", spec.default_model),
        instructions=spec.instructions,
        input=text,
    )
    output = (response.output_text or "").strip()
    if not output:
        raise RuntimeError(f"{spec.name} returned an empty response.")
    return output
