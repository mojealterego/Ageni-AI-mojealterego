"""Small reusable OpenAI Responses API runner for repository agents."""
from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_MODEL = "gpt-4.1-mini"


@dataclass(frozen=True)
class AgentSpec:
    name: str
    instructions: str
    default_model: str = DEFAULT_MODEL


def run_agent(spec: AgentSpec, user_input: str, model: str | None = None) -> str:
    """Run an agent and return its text response.

    Raises ValueError for empty input/missing credentials and propagates SDK
    errors. The validated default model can be overridden per call or by the
    OPENAI_MODEL environment variable.
    """
    text = user_input.strip()
    if not text:
        raise ValueError("Input must not be empty.")

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "Install dependencies with: pip install -r requirements.txt"
        ) from exc

    client = OpenAI(api_key=api_key, timeout=60.0, max_retries=2)
    response = client.responses.create(
        model=model or os.getenv("OPENAI_MODEL", spec.default_model),
        instructions=spec.instructions,
        input=text,
    )
    output = (response.output_text or "").strip()
    if not output:
        raise RuntimeError(f"{spec.name} returned an empty response.")
    return output
