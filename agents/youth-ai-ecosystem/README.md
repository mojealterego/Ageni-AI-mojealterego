# Youth AI Ecosystem (2025–2030)

This directory is the inspectable five-agent core profile catalogue for the Youth AI development ecosystem:

| Profile ID | Runtime entrypoint | Risk tier |
|---|---|---|
| `sokrates` | `agents/youth-ai-socrates-tutor/agent.py` | low |
| `kreator` | `agents/youth-ai-creator/agent.py` | medium |
| `nawigator` | `agents/youth-ai-navigator/agent.py` | low |
| `weryfikator` | `agents/youth-ai-verifier/agent.py` | medium |
| `bufor` | `agents/youth-ai-wellness-buffer/agent.py` | high |

The role/purpose/risk metadata lives in `agent.py`. The executable agents live in their dedicated entrypoint directories and use the repository-wide `AgentSpec/run_agent` runtime.

## Safety and scope

The profile module is a **policy/profile catalogue**, not a production safety system. Its instructions do not by themselves guarantee age verification, crisis detection, moderation, privacy compliance, parental consent, human escalation, or safe model behavior.

Before deployment with minors, implement and independently validate at the application layer:

- age-appropriate onboarding, consent and jurisdiction-specific requirements;
- deterministic input/output safety controls and adversarial testing;
- transparent crisis escalation UX with locally verified resources;
- data minimization, retention/deletion, access control and audit logging;
- abuse/grooming defenses and human oversight;
- bounded session controls and clear user-facing reset/exit paths.

Do not expose private conversation content to parents, educators or operators by default. Any disclosure mechanism must be explicit, narrowly scoped, authorized and legally reviewed.

## Runtime integration

The five core entrypoints are registered in `agent_runtime/registry.py` under:

- `youth-ai-socrates-tutor`
- `youth-ai-creator`
- `youth-ai-navigator`
- `youth-ai-verifier`
- `youth-ai-wellness-buffer`

The unified CLI is `agents/youth-ai-ecosystem/runner.py`. Example: `python agents/youth-ai-ecosystem/runner.py --agent-id sokrates "Wyjaśnij ułamki zwykłe."`.

The integration test is `tests/test_youth_ai_ecosystem.py`. It checks registry membership, exact entrypoint paths, Python compilation, shared-runtime usage, unified-runner compilation and the presence of key role/safety contract text.

This repository's tests are static/offline checks. They do **not** constitute clinical validation, child-safety certification, legal compliance, red-team completion, or proof that a model will follow every instruction under adversarial prompting.

## Evidence discipline

Claims from a source report about adolescent development, prevalence, product efficacy or future outcomes are treated as research hypotheses unless independently verified. Implementation code must not turn an unverified report claim into a product guarantee.

## Non-goals

These agents do not silently monitor users, build persistent psychological profiles, pretend to be human friends, promise confidentiality, or execute consequential external actions without the necessary authorization and tooling.
