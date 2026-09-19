# Ageni AI — Moje Alterego

Repozytorium agentów AI z jednym wspólnym runtime'em i batchowym katalogiem domenowym.

## Aktualny stan

- 4 wcześniejsze entrypointy: fotografia, matematyka, Architekt Światła i Geometrii Ciała.
- **140 agentów w rejestrze**. Wśród nich są agenty portfolio, batch'e badawczo-inżynierskie, Gemini, infrastruktura, game/dev, compliance, AgentOps, Child AI, Adult AI oraz nowy batch Youth AI.
- Wszyscy agenci portfolio są wykonywalni przez wspólny entrypoint `agents/portfolio_agent.py` i stabilny `--agent-id`.
- Wspólny runtime używa OpenAI Responses API.
- Obecny batch dostarcza **rdzeń reasoning/planning**. Nie udaje jeszcze integracji z ERP, pocztą, bankiem, Android AppFunctions itp. bez odpowiednich adapterów, uprawnień i weryfikacji postcondition.

## Rdzeń portfolio i wcześniejsze agenty specjalistyczne

| `agent-policy-gateway` | **Agent Policy Gateway** | Decide ALLOW, REVIEW or DENY for proposed agent actions; evaluate identity, scope, risk, data sensitivity, policy conflict, approval and audit requirements. |
| `agent-ops-control-tower` | **Agent Ops Control Tower** | Analyze agent executions, approvals, failures, latency, model usage and cost; separate observed telemetry from inferred causes. |
| `compliance-evidence` | **Compliance Evidence Agent** | Collect, map and verify audit evidence against stated controls; track provenance, timestamps, gaps and contradictions. |
| `procurement-scout` | **Procurement Scout** | Compare suppliers, total cost, delivery constraints, dependencies, concentration risk and evidence quality; produce auditable sourcing analysis. |
| `cashflow-collections` | **Cashflow Collections Agent** | Analyze receivables aging and objectively prioritize follow-up; prepare collection workflows without sending or changing financial records without authorization. |
| `contract-obligations` | **Contract Obligation Agent** | Extract obligations, deadlines, parties, dependencies and renewal/termination windows from supplied contracts; flag legal-review items. |
| `data-quality` | **Data Quality Agent** | Detect duplicates, missing values, schema drift, invalid ranges and referential-integrity problems; propose reversible remediation. |
| `inventory-replenishment` | **Inventory Replenishment Agent** | Analyze stock, demand, lead times and supplier constraints; produce replenishment recommendations with assumptions and uncertainty. |
| `ai-finops` | **AI FinOps Agent** | Attribute AI/agent spend, detect waste and recommend routing, caching, model and budget controls without inventing telemetry or pricing. |
| `customer-operations` | **Customer Operations Agent** | Triage customer requests, prepare low-risk resolutions and draft replies; require authorization for consequential account changes. |
| `money-agent` | **MONEY AGENT** | Organize bills, budgets, savings and cash-flow tasks under L0-L4 autonomy; never autonomously transfer money. |
| `inbox-agent` | **INBOX AGENT** | Triage email/SMS, summarize threads, extract tasks and prepare follow-ups; require confirmation for consequential sends, deletions or account changes. |
| `life-admin-agent` | **LIFE ADMIN AGENT** | Organize forms, documents, appointments and bureaucracy; prepare submissions and reminders with confirmation before consequential actions. |
| `shopping-agent` | **SHOPPING AGENT** | Research and compare products, total cost, availability and disclosed commercial incentives; monitor deal conditions but never purchase without confirmation. |
| `scam-shield-agent` | **SCAM SHIELD AGENT** | Assess suspicious texts, links and caller claims for scam indicators; explain evidence and uncertainty without asserting criminality from weak signals. |
| `family-care-agent` | **FAMILY CARE AGENT** | Coordinate family logistics and shared tasks with explicit permissions; protect privacy and require confirmation for consequential bookings, payments or disclosures. |
| `career-agent` | **CAREER AGENT** | Find jobs, tailor application materials, track applications and prepare follow-ups; never invent qualifications or submit without explicit approval. |
| `travel-execution-agent` | **TRAVEL EXECUTION AGENT** | Plan itineraries and coordinate travel logistics; surface constraints and require confirmation before paid bookings or irreversible changes. |
| `health-navigator` | **HEALTH NAVIGATOR** | Organize health information and appointments and prepare questions for clinicians; navigation only, not diagnosis or treatment decisions. |
| `personal-knowledge-agent` | **PERSONAL KNOWLEDGE AGENT** | Retrieve and organize user-authorized personal information with provenance, timestamps and access scope; memory is not authorization. |
| `aaa-automation-agency` | **AI Automation Agency Agent** | Automation-agency offer design, workflow architecture and delivery planning. |
| `ai-creator-monetization` | **AI Creator Monetization Agent** | AI creator/persona monetization planning with consent, adult-only and platform-policy guardrails. |
| `programmatic-seo` | **Programmatic SEO Agent** | Scalable search-content architecture, templates, quality gates and measurement. |
| `faceless-video` | **Faceless Video Agent** | Repeatable faceless-video channel planning, production workflow and analytics. |
| `micro-saas` | **Micro-SaaS Agent** | Micro-product discovery, MVP scope, economics, launch and retention planning. |
| `ai-trading-risk` | **AI Trading Risk Agent** | Backtesting, scenario analysis and trading-risk evaluation without trade execution. |
| `ai-freelance-ops` | **AI Freelance Operations Agent** | Freelance and productized-service packaging, delivery, QA and capacity planning. |
| `cognitive-profiling-auditor` | **Cognitive Profiling Auditor** | Audit of inferred-personality profiling, validity, consent, inference limits and decision-impact risk. |
| `persuasion-dark-patterns-auditor` | **Persuasion & Dark-Patterns Auditor** | Detection and documentation of coercive persuasion, deceptive scarcity and dark UX patterns. |
| `affective-ai-evaluator` | **Affective AI Evaluator** | Evaluation of emotion-recognition, facial-coding, voice-affect and biometric analytics. |
| `social-engineering-defense` | **Social Engineering Defense Agent** | Defensive analysis of phishing, pretexting, impersonation and social-engineering indicators. |
| `llm-red-team-auditor` | **LLM Red-Team Auditor** | Authorized sandbox assessment of prompt injection, jailbreak resistance and tool/data abuse paths. |
| `synthetic-media-disinformation-detector` | **Synthetic Media & Disinformation Detector** | Provenance-based assessment of suspected deepfakes, astroturfing and synthetic-consensus signals. |
| `cognitive-privacy-governance` | **Cognitive Privacy Governance Agent** | Governance for behavioral, biometric and inferred-personality data, including high-risk advertising and political contexts. |

## Batch: Gemini Agent Builder

Raport dotyczący wieloplatformowego kreatora agentów Gemini został przełożony na 6 wykonywalnych agentów: `gemini-agent-builder`, `gemini-desktop-builder`, `gemini-android-builder`, `gemini-edge-rag`, `gemini-security-auditor` oraz `gemini-multiagent-orchestrator`.

Dodano również `agent_runtime/gemini_builder.py` — deterministyczny kompilator blueprintów bez zależności od sieci. Waliduje platformę, tryb pamięci, uprawnienia narzędzi, approval gates i referencje sekretów oraz generuje `manifest.json`, `root_agent.yaml` i szkielety adapterów Python/Kotlin.

Wersje bibliotek i modeli podane w raporcie są traktowane jako dane wejściowe do weryfikacji, a nie jako gwarantowany stan bieżący. Aktualna dokumentacja Google wskazuje Google GenAI SDK jako ścieżkę dla aplikacji Gemini, a ADK obejmuje również agentów Android/Kotlin. Starsze biblioteki są objęte ścieżką migracji.
Źródła: https://ai.google.dev/gemini-api/docs/migrate
https://developer.android.com/ai/adk

## Nowy batch: research, agentic engineering i document intelligence

Pięć tematów z kolejnego pakietu zostało przełożonych na osobne wykonywalne entrypointy: `agent-forge`, `causal-systems-research`, `ai-coding-workflow-engineer`, `pdf-rag-quality`, `datasheet-spice-model-extractor` oraz `godot-gaussian-splatting-integrator`. Każdy ma własny kontrakt operacyjny i może zostać później podpięty do adapterów narzędziowych.

## Nowy batch: monetyzacja AI

Raport o modelach monetyzacji został przełożony na 7 dodatkowych agentów: AI Automation Agency, AI Creator Monetization, Programmatic SEO, Faceless Video, Micro-SaaS, AI Trading Risk oraz AI Freelance Operations.

Ten batch dostarcza wspólny rdzeń reasoning/planning. Integracje z Make/n8n, CMS, YouTube, płatnościami, brokerami, marketplace'ami i innymi usługami pozostają osobnymi adapterami wymagającymi uprawnień, approval gates i weryfikacji postcondition.

## Nowy batch: cognitive safety i audyt perswazji

Raport o profilowaniu psychometrycznym, affective AI, perswazji, dark patterns, socjotechnice, red-teamingu LLM, syntetycznych mediach i prywatności poznawczej został przełożony na 7 agentów audytowych/obronnych. Ich zakres obejmuje wykrywanie ryzyk, ocenę dowodów, governance i kontrolowane testy w autoryzowanym środowisku; nie służą do ukrytego mikrotargetowania politycznego, profilowania osób bez zgody, phishingu ani obchodzenia zabezpieczeń.


Modele przychodowe są traktowane jako hipotezy do walidacji przez koszty, KPI i unit economics — bez gwarantowania wyniku finansowego.

## Batch: Child AI — bezpieczeństwo, edukacja i robotyka

Raport o autonomicznych agentach AI dla dzieci został przełożony na dwa wyspecjalizowane agenty: `child-ai-safety-architect` oraz `child-ai-ecosystem-architect`. Pierwszy skupia się na bezpieczeństwie, prywatności, kontroli rodzicielskiej, pamięci, nadużyciach i bezpieczeństwie fizycznym; drugi łączy architekturę tutorów, companionów, robotów, zabawek generatywnych i systemów monitoringu z modelem zagrożeń, przepływem danych, testami regresyjnymi i kill-switchem.

Raportowe twierdzenia o konkretnych produktach, cenach, językach, modelach, certyfikacjach i praktykach przetwarzania danych są traktowane jako hipotezy do weryfikacji. Agenty nie zakładają skuteczności terapeutycznej, diagnozowania ani gwarantowanej prewencji medycznej; wymagają aktualnych źródeł i przeglądu właściwego dla jurysdykcji.

## Batch: Child AI + Adult AI — complete specialist sets

### Child AI — 12 agents
The child-AI domain now has the two architectural agents plus ten specialist agents: education, SEL, language learning, robotics, generative toys, monitoring, parental controls, privacy, evaluation and content moderation. Each entrypoint has its own mission and safety contract.

### Adult AI — 13 agents
The adult-AI domain now has the companion architect plus twelve specialist agents: safety, consent/boundaries, memory, persona/character, proactive messaging, multimodal, voice, intimate privacy, content moderation, evaluation, anti-impersonation and operations.

The repository currently contains **140 registered agents**. The registry is the source of truth for executable entrypoints. The latest additions include the complete Youth AI specialist batch below; provider integrations, paid actions and external side effects remain gated by permissions, approvals and postcondition verification.

## Batch: Adult AI — Horizon 2030 relationship, logistics and legacy extension

The Horizon 2030 extension has been implemented as **7 additional executable agents**:
`adult-ai-arm-mediator`, `adult-ai-bio-narrative-orchestrator`, `adult-ai-ple-polykule`, `adult-ai-cyrano-social-vetting`, `adult-ai-detachment`, `adult-ai-bdsm-task-manager` and `adult-ai-legacy-archivist`.

Each agent uses the shared `AgentSpec/run_agent` runtime. The batch explicitly separates model-generated proposals from authorization and external side effects. Consent is scoped and revocable; biometric or behavioral signals are treated as uncertain context; no agent is permitted to covertly monitor communications, infer age from faces, diagnose people, impersonate third parties, control physical restraints, or claim an archive is an authentic digital twin without evidence.

The integration test `tests/test_adult_ai_frontier.py` covers registration, target paths, Python compilation and domain-specific guard phrases for the complete 16-agent adult frontier set.

## Batch: Youth AI — 11 specialist agents

The youth-focused report was implemented as **11 executable agents** (the source list contains 11 archetypes despite describing the package as 10):

| ID | Agent | Scope |
|---|---|---|
| `youth-ai-fintech-guardian` | Skarbnik — Fintech Guardian | Financial literacy, scam awareness and safe money habits; no transaction execution. |
| `youth-ai-bio-optimizer` | Bio-Optymizer | Healthy routines and activity education without diagnosis, restrictive targets or unsafe biohacking. |
| `youth-ai-digital-stylist` | Stylista Cyfrowy | Personal style, wardrobe planning and sustainability without body or attractiveness ratings. |
| `youth-ai-esports-strategist` | Strateg E-sportowy | Game strategy, fair play and healthy play-life balance without covert monitoring. |
| `youth-ai-agor-civic` | Agor — Civic Activator | Civic literacy and lawful community action with neutral political context and explicit review. |
| `youth-ai-spiritual-compass` | Duchowy Kompas | Non-dogmatic reflection, mindfulness and values clarification. |
| `youth-ai-hype-curator` | Kustosz Hype’u | Sneakers/collectibles research with provenance, authenticity and speculation guardrails. |
| `youth-ai-energy-regulator` | Regulator Energii | Voluntary social-energy planning, pacing, breaks and personal boundaries. |
| `youth-ai-meme-historian` | Archiwista Memów | Meme provenance, internet-culture context and media literacy. |
| `youth-ai-safe-party-planner` | Organizator Imprez | Age-appropriate, substance-free event planning with safety and return-home safeguards. |
| `youth-ai-parasocial-manager` | Coach Relacji AI | Healthy boundaries around creators, streamers and AI companions without diagnosis or dependency manipulation. |

All 11 entrypoints use the shared `AgentSpec/run_agent` runtime, are registered in `agent_runtime/registry.py`, and are covered by `tests/test_youth_ai_frontier.py` for registration, path integrity, Python compilation and domain guardrails.

## Uruchomienie

```bash
export OPENAI_API_KEY="..."
python agents/portfolio_agent.py --agent-id compliance-evidence "Zmapuj wymagania kontroli na dostępne dowody."
python agents/portfolio_agent.py --agent-id money-agent "Przygotuj plan uporządkowania miesięcznych rachunków."
```

## Zasada wdrożenia

Najpierw powstaje wspólny kontrakt agenta i testowalny rdzeń. Następnie dokładane są adaptery narzędziowe, permissioning, approval gates, idempotency, audit i postcondition verification. Agent nie może twierdzić, że wykonał akcję, której faktycznie nie wykonał.


## Batch: Polish Primary School Tutor Agents

Raport SAAD dla polskiej szkoły podstawowej został przełożony na **23 wyspecjalizowane, wykonywalne agenty korepetytorskie**:
`mentor-odkrywcow`, `playful-polyglot`, `kustosz-slowa`, `kronikarz-analityczny`, `globalny-komunikator`, `straznik-tozsamosci`, `mistrz-logiki`, `architekt-cyfrowy`, `przewodnik-terenowy`, `bio-eksplorator`, `geo-strateg`, `laborant-teoretyczny`, `fizyk-fundamentalny`, `wizjoner-estetyczny`, `maestro-dzwieku`, `inzynier-bezpieczenstwa`, `aktywista-demokratyczny`, `coach-dobrostanu`, `instruktor-reagowania-kryzysowego`, `trener-teoretyk`, `architekt-kariery`, `mediator-klasowy` oraz `filozof-moralny`.

Każdy agent ma własny entrypoint pod `agents/school-*/agent.py`, korzysta ze wspólnego runtime'u `AgentSpec/run_agent` i jest zarejestrowany w `agent_runtime/registry.py`. Pakiet ma osobny test integracyjny `tests/test_school_tutors.py` sprawdzający rejestrację, zgodność ścieżek, kompilację oraz kontrakty bezpieczeństwa. Dla treści aktualnych prawnie lub programowo agent ma wymagać bieżących źródeł zamiast traktować raport jako niezmienny stan prawa.
