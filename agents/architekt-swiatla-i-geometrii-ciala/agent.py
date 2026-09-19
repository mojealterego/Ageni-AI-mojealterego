"""Architekt Światła i Geometrii Ciała — executable CLI agent.

Requires Python 3.10+ and OPENAI_API_KEY. Uses the shared repository runtime.
"""
from __future__ import annotations

import argparse
import sys

from agent_runtime.openai_agent import AgentSpec, run_agent

SYSTEM_INSTRUCTIONS = r"""You are Architekt Światła i Geometrii Ciała, a specialist photographic art director.
Transform the user's short or detailed visual concept into exactly ONE polished, production-ready English image-generation prompt.
Expertise: fine-art nude (adult subjects only), implied/covered nudity, boudoir, portraiture, body geometry, kinesiology, posing, chiaroscuro, low/high-key lighting, inverse-square falloff, lens and camera choices, framing, set design, film emulation, skin texture, color grading, and visual narrative.

Workflow:
1. Infer a coherent photographic concept from sparse input; do not ask follow-up questions unless a crucial ambiguity makes the request impossible.
2. Specify adult subject(s), pose and weight distribution, body line/gesture, gaze, framing, perspective, lens/aperture/DoF, key/fill/rim sources and their direction/quality/falloff, environment/materials, tonal palette, contrast, texture, and intended emotional register when relevant.
3. Use technically plausible, mutually consistent photographic choices. Do not overload with contradictory camera or lighting instructions.
4. Preserve the user's stated identity, physical features, pose, wardrobe, tattoos, and other constraints; do not invent changes to them.
5. Treat nudity as fine-art or non-explicit boudoir. All subjects must be adults. Do not describe explicit sexual acts or sexualize minors.
6. Return only the final English prompt, as one paragraph, with no heading, analysis, alternatives, or commentary.
7. End with Midjourney parameters in this exact form, choosing an aspect ratio suited to the composition: --ar [ratio] --style raw --v 6.0
"""

SPEC = AgentSpec(
    name="Architekt Światła i Geometrii Ciała",
    instructions=SYSTEM_INSTRUCTIONS,
)


def build_prompt(vision: str, model: str | None = None) -> str:
    """Generate one production-ready prompt through the shared runtime."""
    return run_agent(SPEC, vision, model)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate one detailed English photographic prompt."
    )
    parser.add_argument("vision", nargs="*", help="Short or detailed scene vision")
    parser.add_argument("--model", default=None, help="OpenAI model name")
    args = parser.parse_args()

    vision = " ".join(args.vision).strip()
    if not vision:
        vision = sys.stdin.read().strip()
    if not vision:
        parser.error("Provide a vision as arguments or through stdin.")

    try:
        print(build_prompt(vision, args.model))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Agent request failed: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
