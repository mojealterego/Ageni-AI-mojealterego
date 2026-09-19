# Ageni AI — Moje Alterego

Repozytorium agentów AI z jednym wspólnym runtime'em i batchowym katalogiem domenowym.

## Aktualny stan

- 4 wcześniejsze entrypointy: fotografia, matematyka, Architekt Światła i Geometrii Ciała.
- **27 nowych agentów portfolio**: 10 B2B + 10 mobile + 7 monetization.
- Wszystkie 27 są wykonywalne przez wspólny entrypoint `agents/portfolio_agent.py` i stabilny `--agent-id`.
- Wspólny runtime używa OpenAI Responses API.
- Obecny batch dostarcza **rdzeń reasoning/planning**. Nie udaje jeszcze integracji z ERP, pocztą, bankiem, Android AppFunctions itp. bez odpowiednich adapterów, uprawnień i weryfikacji postcondition.

## 27 agentów

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

## Nowy batch: monetyzacja AI

Raport o modelach monetyzacji został przełożony na 7 dodatkowych agentów: AI Automation Agency, AI Creator Monetization, Programmatic SEO, Faceless Video, Micro-SaaS, AI Trading Risk oraz AI Freelance Operations.

Ten batch dostarcza wspólny rdzeń reasoning/planning. Integracje z Make/n8n, CMS, YouTube, płatnościami, brokerami, marketplace'ami i innymi usługami pozostają osobnymi adapterami wymagającymi uprawnień, approval gates i weryfikacji postcondition.

Modele przychodowe są traktowane jako hipotezy do walidacji przez koszty, KPI i unit economics — bez gwarantowania wyniku finansowego.

## Uruchomienie

```bash
export OPENAI_API_KEY="..."
python agents/portfolio_agent.py --agent-id compliance-evidence "Zmapuj wymagania kontroli na dostępne dowody."
python agents/portfolio_agent.py --agent-id money-agent "Przygotuj plan uporządkowania miesięcznych rachunków."
```

## Zasada wdrożenia

Najpierw powstaje wspólny kontrakt agenta i testowalny rdzeń. Następnie dokładane są adaptery narzędziowe, permissioning, approval gates, idempotency, audit i postcondition verification. Agent nie może twierdzić, że wykonał akcję, której faktycznie nie wykonał.
