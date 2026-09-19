# Youth AI Ecosystem (2025–2030)

Five inspectable agent profiles are defined in `agent.py`:

| ID | Role | Risk tier |
|---|---|---|
| `sokrates` | Socratic learning tutor | low |
| `kreator` | Creative mentor | medium |
| `nawigator` | Career exploration | low |
| `weryfikator` | Information literacy | medium |
| `bufor` | Non-clinical emotional support | high |

## Safety and scope

This package currently provides prompt/profile metadata only. It is **not** a production safety system and does not itself run classifiers, enforce session limits, implement deletion, manage parental dashboards, browse laterally, or contact emergency services. Those require explicit application/runtime integrations and tests.

Before deployment with minors, implement and independently validate: age-appropriate onboarding and consent; deterministic input/output safety layers; crisis escalation UX and locally verified resources; data minimization, retention/deletion and access controls; abuse/grooming defenses; human oversight; and evaluation with youth-safety specialists. Do not expose private conversation content to parents/educators by default.

The report's claims about adolescent neurobiology and population prevalence are not treated as established implementation facts by this code. Product decisions should be grounded in current, high-quality evidence and reviewed by qualified specialists.
