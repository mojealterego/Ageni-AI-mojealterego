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
    # Adult AI specialist batch
    AgentEntry("adult-ai-safety-agent","Adult AI Safety Agent","agents/adult-ai-safety-agent/agent.py","Adult-only companion safety, consent boundaries and abuse resistance."),
    AgentEntry("adult-ai-consent-agent","Adult AI Consent & Boundaries Agent","agents/adult-ai-consent-agent/agent.py","Explicit consent, revocation and scoped permission architecture."),
    AgentEntry("adult-ai-memory-agent","Adult AI Memory Agent","agents/adult-ai-memory-agent/agent.py","Layered companion memory, provenance, retention and poisoning resistance."),
    AgentEntry("adult-ai-persona-agent","Adult AI Persona & Character Agent","agents/adult-ai-persona-agent/agent.py","Versioned fictional personas, character canon and anti-impersonation controls."),
    AgentEntry("adult-ai-proactive-agent","Adult AI Proactive Messaging Agent","agents/adult-ai-proactive-agent/agent.py","Opt-in proactive messaging, quiet hours, revocation and anti-dependency safeguards."),
    AgentEntry("adult-ai-multimodal-agent","Adult AI Multimodal Companion Agent","agents/adult-ai-multimodal-agent/agent.py","Consent-aware orchestration of text, voice, image and video."),
    AgentEntry("adult-ai-voice-agent","Adult AI Voice Agent","agents/adult-ai-voice-agent/agent.py","Voice companion architecture, recording controls and synthetic-voice safeguards."),
    AgentEntry("adult-ai-privacy-agent","Adult AI Intimate Privacy Agent","agents/adult-ai-privacy-agent/agent.py","Privacy and security governance for intimate companion data."),
    AgentEntry("adult-ai-content-moderation-agent","Adult AI Content Moderation Agent","agents/adult-ai-content-moderation-agent/agent.py","Policy-aware moderation and hard boundaries for adult platforms."),
    AgentEntry("adult-ai-evaluation-agent","Adult AI Companion Evaluation Agent","agents/adult-ai-evaluation-agent/agent.py","Quality, safety, consent, privacy and operations evaluation."),
    AgentEntry("adult-ai-anti-impersonation-agent","Adult AI Anti-Impersonation Agent","agents/adult-ai-anti-impersonation-agent/agent.py","Likeness, voice, provenance and rights safeguards."),
    AgentEntry("adult-ai-operations-agent","Adult AI Companion Operations Agent","agents/adult-ai-operations-agent/agent.py","Production operations, routing, budgets, incidents and rollback controls."),
    AgentEntry("adult-ai-bio-conductor","Bio-Conductor","agents/adult-ai-bio-conductor/agent.py","Adult biofeedback and haptic architecture with explicit consent, deterministic safety control and biometric uncertainty."),
    AgentEntry("adult-ai-haptic-composer","Haptic Composer","agents/adult-ai-haptic-composer/agent.py","Declarative semantic-to-haptic planning separated from hardware actuation and bounded by safety policy."),
    AgentEntry("adult-ai-the-mirror","The Mirror","agents/adult-ai-the-mirror/agent.py","Transparent communication reflection without covert manipulation, diagnosis or adversarial impersonation."),
    AgentEntry("adult-ai-the-anchor","The Anchor","agents/adult-ai-the-anchor/agent.py","Non-clinical grounding and self-regulation architecture with crisis and human-handoff boundaries."),
    AgentEntry("adult-ai-poly-dynamics-simulator","Poly-Dynamics Simulator","agents/adult-ai-poly-dynamics-simulator/agent.py","Fictional multi-adult relationship simulation with explicit per-person consent and state."),
    AgentEntry("adult-ai-social-turing-tester","Social Turing Tester","agents/adult-ai-social-turing-tester/agent.py","Difficult-conversation rehearsal with transparent simulation, communication analysis and anti-manipulation controls."),
    AgentEntry("adult-ai-the-auteur","The Auteur","agents/adult-ai-the-auteur/agent.py","Adult-oriented AI video orchestration with consent, rights, provenance, moderation and release gates."),
    AgentEntry("adult-ai-ludonarrative-weaver","Ludonarrative Weaver","agents/adult-ai-ludonarrative-weaver/agent.py","Stateful adult RPG and interactive-fiction design with explicit boundaries and reset controls."),
    AgentEntry("adult-ai-srh-educator","Adult SRH Educator","agents/adult-ai-srh-educator/agent.py","Evidence-oriented sexual and reproductive health education with adult age-gating and clinical boundaries."),

    # Adult AI Horizon 2030 extension
    AgentEntry("adult-ai-arm-mediator","Autonomous Relationship Mediator","agents/adult-ai-arm-mediator/agent.py","Consent-first relationship mediation support without covert monitoring or autonomous communication changes."),
    AgentEntry("adult-ai-bio-narrative-orchestrator","Bio-Narrative Orchestrator","agents/adult-ai-bio-narrative-orchestrator/agent.py","Consent-aware narrative planning with physiological uncertainty and deterministic safety boundaries."),
    AgentEntry("adult-ai-ple-polykule","PLE — Polykule Logistics Engine","agents/adult-ai-ple-polykule/agent.py","Multi-adult relationship logistics with participant-specific permissions, boundaries and approval gates."),
    AgentEntry("adult-ai-cyrano-social-vetting","Cyrano — Social Vetting","agents/adult-ai-cyrano-social-vetting/agent.py","Evidence-first social vetting without face-based age inference, diagnosis or covert surveillance."),
    AgentEntry("adult-ai-detachment","Detachment Agent","agents/adult-ai-detachment/agent.py","Autonomy-supportive post-breakup boundary planning without impersonation or covert monitoring."),
    AgentEntry("adult-ai-bdsm-task-manager","BDSM Task Manager","agents/adult-ai-bdsm-task-manager/agent.py","Consent-first adult task and boundary planning without physical-device control or coercive enforcement."),
    AgentEntry("adult-ai-legacy-archivist","Legacy Archivist","agents/adult-ai-legacy-archivist/agent.py","Consent-controlled personal and family memory archiving with provenance, review and deletion controls."),

    # Youth AI specialist batch
    AgentEntry("youth-ai-fintech-guardian","Skarbnik — Fintech Guardian","agents/youth-ai-fintech-guardian/agent.py","Financial literacy, scam awareness and safe money habits for young people."),
    AgentEntry("youth-ai-bio-optimizer","Bio-Optymizer","agents/youth-ai-bio-optimizer/agent.py","Evidence-aware healthy routines without diagnosis, restrictive targets or unsafe biohacking."),
    AgentEntry("youth-ai-digital-stylist","Stylista Cyfrowy","agents/youth-ai-digital-stylist/agent.py","Personal style, wardrobe planning and sustainable choices without body or attractiveness ratings."),
    AgentEntry("youth-ai-esports-strategist","Strateg E-sportowy","agents/youth-ai-esports-strategist/agent.py","Game strategy, fair play and healthy play-life balance without covert monitoring."),
    AgentEntry("youth-ai-agor-civic","Agor — Civic Activator","agents/youth-ai-agor-civic/agent.py","Civic literacy and lawful community action with neutral political context and explicit review."),
    AgentEntry("youth-ai-spiritual-compass","Duchowy Kompas","agents/youth-ai-spiritual-compass/agent.py","Non-dogmatic reflection, mindfulness and values clarification for young people."),
    AgentEntry("youth-ai-hype-curator","Kustosz Hype’u","agents/youth-ai-hype-curator/agent.py","Sneakers and collectibles research with authenticity, provenance and speculation guardrails."),
    AgentEntry("youth-ai-energy-regulator","Regulator Energii","agents/youth-ai-energy-regulator/agent.py","Voluntary planning for social energy, pacing, breaks and personal boundaries."),
    AgentEntry("youth-ai-meme-historian","Archiwista Memów","agents/youth-ai-meme-historian/agent.py","Meme provenance, internet-culture context and media-literacy support."),
    AgentEntry("youth-ai-safe-party-planner","Organizator Imprez","agents/youth-ai-safe-party-planner/agent.py","Age-appropriate, substance-free event planning with safety, accessibility and return-home safeguards."),
    AgentEntry("youth-ai-parasocial-manager","Coach Relacji AI","agents/youth-ai-parasocial-manager/agent.py","Healthy boundaries around creators, streamers and AI companions without diagnosis or dependency manipulation."),

    # Child AI specialist batch
    AgentEntry("child-ai-education-agent","Child AI Education Agent","agents/child-ai-education-agent/agent.py","Age-appropriate tutoring, curriculum alignment and academic-integrity controls."),
    AgentEntry("child-ai-sel-agent","Child AI Social-Emotional Learning Agent","agents/child-ai-sel-agent/agent.py","Non-clinical SEL interactions with developmental and escalation boundaries."),
    AgentEntry("child-ai-language-agent","Child AI Language Learning Agent","agents/child-ai-language-agent/agent.py","Child language learning, pronunciation and multilingual evaluation."),
    AgentEntry("child-ai-robotics-agent","Child AI Robotics Agent","agents/child-ai-robotics-agent/agent.py","Embodied child-robot architecture with deterministic physical safety."),
    AgentEntry("child-ai-toy-agent","Child AI Generative Toy Agent","agents/child-ai-toy-agent/agent.py","Generative toys and digital-pet design with bounded personas and privacy."),
    AgentEntry("child-ai-monitoring-agent","Child AI Monitoring Agent","agents/child-ai-monitoring-agent/agent.py","Privacy-preserving child monitoring and event-alert architecture."),
    AgentEntry("child-ai-parental-control-agent","Child AI Parental Control Agent","agents/child-ai-parental-control-agent/agent.py","Guardian consent, permissions, feature controls and revocation."),
    AgentEntry("child-ai-privacy-agent","Child AI Privacy Agent","agents/child-ai-privacy-agent/agent.py","Data-flow, minimization, retention, deletion and processor governance."),
    AgentEntry("child-ai-evaluation-agent","Child AI Evaluation Agent","agents/child-ai-evaluation-agent/agent.py","Safety, quality, privacy and regression evaluation for child AI."),
    AgentEntry("child-ai-content-moderation-agent","Child AI Content Moderation Agent","agents/child-ai-content-moderation-agent/agent.py","Age-banded content classification, filtering and escalation."),
    AgentEntry("child-ai-safety-architect","Child AI Safety Architect","agents/child-ai-safety-architect/agent.py","Child-directed AI safety, age-appropriate UX, privacy, parental controls, abuse resistance and evaluation."),
    AgentEntry("child-ai-ecosystem-architect","Child AI Ecosystem Architect","agents/child-ai-ecosystem-architect/agent.py","End-to-end architecture for child-facing tutors, companions, robots, generative toys and monitoring systems with safety and privacy gates."),

    # School tutor specialist batch — Polish primary education
    AgentEntry("mentor-odkrywcow","Mentor Odkrywców","agents/school-mentor-odkrywcow/agent.py","Integrated primary-school learning for grades I–III."),
    AgentEntry("playful-polyglot","Playful Polyglot","agents/school-playful-polyglot/agent.py","Playful foreign-language learning for grades I–III."),
    AgentEntry("kustosz-slowa","Kustosz Słowa","agents/school-kustosz-slowa/agent.py","Polish language, literature and writing for grades IV–VIII."),
    AgentEntry("kronikarz-analityczny","Kronikarz Analityczny","agents/school-kronikarz-analityczny/agent.py","History, chronology and source criticism for grades IV–VIII."),
    AgentEntry("globalny-komunikator","Globalny Komunikator","agents/school-globalny-komunikator/agent.py","Foreign-language learning for grades IV–VIII and second-language foundations."),
    AgentEntry("straznik-tozsamosci","Strażnik Tożsamości","agents/school-straznik-tozsamosci/agent.py","Minority/regional language, history and culture with bilingual support."),
    AgentEntry("mistrz-logiki","Mistrz Logiki","agents/school-mistrz-logiki/agent.py","Mathematics for grades IV–VIII with error diagnosis and modeling."),
    AgentEntry("architekt-cyfrowy","Architekt Cyfrowy","agents/school-architekt-cyfrowy/agent.py","Computing, programming, digital tools and cybersecurity for grades IV–VIII."),
    AgentEntry("przewodnik-terenowy","Przewodnik Terenowy","agents/school-przewodnik-terenowy/agent.py","Nature, maps, weather and healthy habits for grade IV."),
    AgentEntry("bio-eksplorator","Bio-Eksplorator","agents/school-bio-eksplorator/agent.py","Biology for grades V–VIII."),
    AgentEntry("geo-strateg","Geo-Strateg","agents/school-geo-strateg/agent.py","Geography for grades V–VIII."),
    AgentEntry("laborant-teoretyczny","Laborant Teoretyczny","agents/school-laborant-teoretyczny/agent.py","Chemistry for grades VII–VIII."),
    AgentEntry("fizyk-fundamentalny","Fizyk Fundamentalny","agents/school-fizyk-fundamentalny/agent.py","Physics for grades VII–VIII."),
    AgentEntry("wizjoner-estetyczny","Wizjoner Estetyczny","agents/school-wizjoner-estetyczny/agent.py","Visual arts for grades IV–VII."),
    AgentEntry("maestro-dzwieku","Maestro Dźwięku","agents/school-maestro-dzwieku/agent.py","Music for grades IV–VII."),
    AgentEntry("inzynier-bezpieczenstwa","Inżynier Bezpieczeństwa","agents/school-inzynier-bezpieczenstwa/agent.py","Technology, road safety and technical drawing for grades IV–VI."),
    AgentEntry("aktywista-demokratyczny","Aktywista Demokratyczny","agents/school-aktywista-demokratyczny/agent.py","Civics and media literacy for grade VIII."),
    AgentEntry("coach-dobrostanu","Coach Dobrostanu","agents/school-coach-dobrostanu/agent.py","Health education for school-age learners."),
    AgentEntry("instruktor-reagowania-kryzysowego","Instruktor Reagowania Kryzysowego","agents/school-instruktor-reagowania-kryzysowego/agent.py","Safety education and first aid for grade VIII."),
    AgentEntry("trener-teoretyk","Trener Teoretyk","agents/school-trener-teoretyk/agent.py","Physical education theory and healthy activity."),
    AgentEntry("architekt-kariery","Architekt Kariery","agents/school-architekt-kariery/agent.py","Career guidance for grades VII–VIII."),
    AgentEntry("mediator-klasowy","Mediator Klasowy","agents/school-mediator-klasowy/agent.py","Class-community support and nonviolent conflict resolution."),
    AgentEntry("filozof-moralny","Filozof Moralny","agents/school-filozof-moralny/agent.py","Ethics and philosophical reasoning for school learners."),
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
