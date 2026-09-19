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
    AgentEntry("compliance-evidence","Compliance Evidence Agent","agents/portfolio_agent.py","Collect, map and verify audit evidence."),
    AgentEntry("procurement-scout","Procurement Scout","agents/portfolio_agent.py","Supplier, cost and sourcing analysis."),
    AgentEntry("cashflow-collections","Cashflow Collections Agent","agents/portfolio_agent.py","Receivables analysis and authorized follow-up planning."),
    AgentEntry("contract-obligations","Contract Obligation Agent","agents/portfolio_agent.py","Contract obligations, deadlines and renewal extraction."),
    AgentEntry("data-quality","Data Quality Agent","agents/portfolio_agent.py","Data integrity and schema-quality analysis."),
    AgentEntry("inventory-replenishment","Inventory Replenishment Agent","agents/portfolio_agent.py","Inventory and replenishment analysis."),
    AgentEntry("ai-finops","AI FinOps Agent","agents/portfolio_agent.py","AI spend attribution and optimization."),
    AgentEntry("customer-operations","Customer Operations Agent","agents/portfolio_agent.py","Customer request triage and response preparation."),
    AgentEntry("money-agent","MONEY AGENT","agents/portfolio_agent.py","Personal finance organization without autonomous transfers."),
    AgentEntry("inbox-agent","INBOX AGENT","agents/portfolio_agent.py","Message triage and follow-up preparation."),
    AgentEntry("life-admin-agent","LIFE ADMIN AGENT","agents/portfolio_agent.py","Forms, documents and appointment organization."),
    AgentEntry("shopping-agent","SHOPPING AGENT","agents/portfolio_agent.py","Product research and comparison without autonomous purchase."),
    AgentEntry("scam-shield-agent","SCAM SHIELD AGENT","agents/portfolio_agent.py","Scam indicator analysis and defensive guidance."),
    AgentEntry("family-care-agent","FAMILY CARE AGENT","agents/portfolio_agent.py","Permissioned family logistics coordination."),
    AgentEntry("career-agent","CAREER AGENT","agents/portfolio_agent.py","Job search and application preparation."),
    AgentEntry("travel-execution-agent","TRAVEL EXECUTION AGENT","agents/portfolio_agent.py","Travel planning and authorized booking preparation."),
    AgentEntry("health-navigator","HEALTH NAVIGATOR","agents/portfolio_agent.py","Health information organization and clinician-question preparation."),
    AgentEntry("personal-knowledge-agent","PERSONAL KNOWLEDGE AGENT","agents/portfolio_agent.py","Authorized personal knowledge retrieval."),
    AgentEntry("aaa-automation-agency","AI Automation Agency Agent","agents/portfolio_agent.py","Automation service design and delivery planning."),
    AgentEntry("ai-creator-monetization","AI Creator Monetization Agent","agents/portfolio_agent.py","Compliant creator monetization planning."),
    AgentEntry("programmatic-seo","Programmatic SEO Agent","agents/portfolio_agent.py","Scalable search content systems."),
    AgentEntry("faceless-video","Faceless Video Agent","agents/portfolio_agent.py","Faceless video production planning."),
    AgentEntry("micro-saas","Micro-SaaS Agent","agents/portfolio_agent.py","Micro-product discovery and launch planning."),
    AgentEntry("ai-trading-risk","AI Trading Risk Agent","agents/portfolio_agent.py","Trading risk analysis without trade execution."),
    AgentEntry("ai-freelance-ops","AI Freelance Operations Agent","agents/portfolio_agent.py","Freelance delivery and operations planning."),
    AgentEntry("cognitive-profiling-auditor","Cognitive Profiling Auditor","agents/portfolio_agent.py","Audit of inferred-personality profiling."),
    AgentEntry("persuasion-dark-patterns-auditor","Persuasion & Dark-Patterns Auditor","agents/portfolio_agent.py","Detection of manipulative UX patterns."),
    AgentEntry("affective-ai-evaluator","Affective AI Evaluator","agents/portfolio_agent.py","Evaluation of affective and biometric analytics."),
    AgentEntry("social-engineering-defense","Social Engineering Defense Agent","agents/portfolio_agent.py","Defensive social-engineering analysis."),
    AgentEntry("llm-red-team-auditor","LLM Red-Team Auditor","agents/portfolio_agent.py","Authorized LLM security assessment."),
    AgentEntry("synthetic-media-disinformation-detector","Synthetic Media & Disinformation Detector","agents/portfolio_agent.py","Provenance-based synthetic-media assessment."),
    AgentEntry("cognitive-privacy-governance","Cognitive Privacy Governance Agent","agents/portfolio_agent.py","Governance for sensitive behavioral and biometric data."),
    AgentEntry("agent-forge","Agent Forge","agents/agent-forge/agent.py","Compiles research into agent capabilities, upgrades, tests and verification gates."),
    AgentEntry("causal-systems-research","Causal Systems Research Agent","agents/causal-systems-research/agent.py","Causal inference, identification audits and research validation."),
    AgentEntry("ai-coding-workflow-engineer","AI Coding Workflow Engineer","agents/ai-coding-workflow-engineer/agent.py","Bounded agentic coding workflows and verification."),
    AgentEntry("pdf-rag-quality","PDF Extraction & RAG Quality Agent","agents/pdf-rag-quality/agent.py","PDF extraction, provenance and RAG evaluation."),
    AgentEntry("datasheet-spice-model-extractor","Datasheet-to-SPICE Model Agent","agents/datasheet-spice-model-extractor/agent.py","Datasheet parameter extraction and candidate SPICE validation."),
    AgentEntry("godot-gaussian-splatting-integrator","Godot Gaussian Splatting Integrator","agents/godot-gaussian-splatting-integrator/agent.py","Godot Gaussian-Splatting integration and validation."),
    AgentEntry("omnicore-forge","OmniCore Forge","agents/omnicore-forge/agent.py","Private AI infrastructure, nested virtualization, GPU/RAG and Rust kernel engineering with safety gates."),

    AgentEntry("gemini-agent-builder","Gemini Agent Builder","agents/gemini-agent-builder/agent.py","Cross-platform Gemini agent compilation, manifests, adapters and security gates."),
    AgentEntry("gemini-desktop-builder","Gemini Desktop Builder","agents/gemini-desktop-builder/agent.py","Python/Google GenAI SDK/ADK desktop agent engineering."),
    AgentEntry("gemini-android-builder","Gemini Android Builder","agents/gemini-android-builder/agent.py","Kotlin/Android Gemini agent construction and lifecycle-safe tooling."),
    AgentEntry("gemini-edge-rag","Gemini Edge RAG Agent","agents/gemini-edge-rag/agent.py","On-device RAG, provenance, local indexing and cloud fallback controls."),
    AgentEntry("gemini-security-auditor","Gemini Security Auditor","agents/gemini-security-auditor/agent.py","Security assessment for Gemini builders, tools, MCP and data boundaries."),
    AgentEntry("gemini-multiagent-orchestrator","Gemini Multi-Agent Orchestrator","agents/gemini-multiagent-orchestrator/agent.py","Bounded delegation, memory, approvals and observability for multi-agent Gemini systems."),
    AgentEntry("system-kernel-engineer","System Kernel Engineer","agents/system-kernel-engineer/agent.py","Low-level OS/kernel, Rust/no_std, C-to-Rust, GPU and hardware-interface engineering with verification gates."),
    AgentEntry("gamedev-engineer","GameDev Engineer","agents/gamedev-engineer/agent.py","Unity, Unreal, Godot, mobile and gameplay-AI engineering with deterministic QA and performance gates."),
    AgentEntry("creative-writing-room","Creative Writing Room","agents/creative-writing-room/agent.py","Long-form fiction planning, world-bible, bounded drafting, RAG and continuity control."),
    AgentEntry("comic-visual-continuity","Comic Visual Continuity Agent","agents/comic-visual-continuity/agent.py","Comic panel scripting, character/reference consistency and visual continuity QA."),
    AgentEntry("boardgame-ludology","Boardgame Ludology Agent","agents/boardgame-ludology/agent.py","Formal tabletop rules, self-play, game-theoretic evaluation and balance/playtest analysis."),
    AgentEntry("quality-diversity-engineer","Quality Diversity Engineer","agents/quality-diversity-engineer/agent.py","MAP-Elites, Novelty Search, evolutionary archives and reproducible quality-diversity experiments."),
    AgentEntry("frontend-design-to-code","Frontend Design-to-Code Engineer","agents/frontend-design-to-code/agent.py","Screenshot/design-to-code, responsive frontend architecture, accessibility and visual validation."),
    AgentEntry("kernel-systems-engineer","Kernel Systems Engineer","agents/kernel-systems-engineer/agent.py","OS/kernel implementation, nested virtualization, GPU/RAG infrastructure and bounded self-healing engineering."),
    AgentEntry("legal-compliance-agent","Legal & Compliance Agent","agents/legal-compliance-agent/agent.py","Traceable legal-information analysis, agentic RAG, citation enforcement and compliance evidence mapping."),
    AgentEntry("scientific-experiment-agent","Scientific Experiment Agent","agents/scientific-experiment-agent/agent.py","Scientific experiment design, hardware-in-the-loop orchestration, data integrity and reproducible analysis."),
    AgentEntry("cross-saas-orchestrator","Cross-SaaS Orchestrator","agents/cross-saas-orchestrator/agent.py","Provider-neutral cross-SaaS workflow orchestration, MCP-style tool gating, identity scopes and compensation."),
    AgentEntry("agent-supervisor-killswitch","Agent Supervisor & Kill Switch","agents/agent-supervisor-killswitch/agent.py","External policy proxy, hard budgets, anomaly detection, kill switch and bounded recovery for autonomous agents."),
    AgentEntry("realtime-crisis-manager","Real-Time Crisis Manager","agents/realtime-crisis-manager/agent.py","Event-driven crisis architecture with low-latency deterministic controls and bounded model-based analysis."),
    AgentEntry("agent-evaluation-ops","Agent Evaluation Ops","agents/agent-evaluation-ops/agent.py","AgentOps evaluation, golden datasets, judge calibration, drift detection and CI/CD circuit breakers."),
    AgentEntry("adult-ai-companion-architect","Adult AI Companion Architect","agents/adult-ai-companion-architect/agent.py","Architecture, privacy, consent, safety and evaluation for adult-oriented AI companion software."),
    AgentEntry("child-ai-safety-architect","Child AI Safety Architect","agents/child-ai-safety-architect/agent.py","Child-directed AI safety, age-appropriate UX, privacy, parental controls, abuse resistance and evaluation."),
    AgentEntry("child-ai-ecosystem-architect","Child AI Ecosystem Architect","agents/child-ai-ecosystem-architect/agent.py","End-to-end architecture for child-facing tutors, companions, robots, generative toys and monitoring systems with safety and privacy gates."),
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
