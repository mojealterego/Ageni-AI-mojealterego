# Adult AI Frontier Specialist Batch

This batch turns nine concepts from the Horizon 2030 adult-intimacy / psychosexual-development report into executable repository agents.

## Agents

| Agent | Repository ID | Scope |
|---|---|---|
| Bio-Conductor | `adult-ai-bio-conductor` | Biofeedback + haptics architecture with explicit consent, biometric uncertainty and a deterministic safety controller. |
| Haptic Composer | `adult-ai-haptic-composer` | Declarative semantic-to-haptic pattern planning; no direct model-to-device actuation. |
| The Mirror | `adult-ai-the-mirror` | Transparent communication reflection; no covert "narcissism breaker", diagnosis or retaliation. |
| The Anchor | `adult-ai-the-anchor` | Non-clinical grounding/self-regulation; not trauma or PTSD treatment. |
| Poly-Dynamics Simulator | `adult-ai-poly-dynamics-simulator` | Fictional multi-adult relationship simulation with explicit per-person consent state. |
| Social Turing Tester | `adult-ai-social-turing-tester` | Difficult-conversation rehearsal with transparent simulation and anti-manipulation controls. |
| The Auteur | `adult-ai-the-auteur` | Adult-oriented AI video pipeline orchestration with consent, rights, provenance and publication gates. |
| Ludonarrative Weaver | `adult-ai-ludonarrative-weaver` | Stateful adult RPG / interactive-fiction design with explicit boundaries and reset controls. |
| Adult SRH Educator | `adult-ai-srh-educator` | Evidence-oriented sexual/reproductive health education for adults with clinical and jurisdictional boundaries. |

## Runtime contract

Each agent uses the repository's shared `AgentSpec` / `run_agent` runtime. The batch does not add provider-side device control, media publication, clinical treatment, or other external side effects. Those remain adapter responsibilities behind explicit authorization, policy checks and postcondition verification.

## Safety decisions carried into code

Physiological signals are treated as noisy measurements rather than reliable emotion/arousal detectors. Haptic generation is declarative and separated from the hardware safety controller. Relationship and conversation agents distinguish observation from inference and fiction from real-world claims. Clinical/trauma-adjacent functionality is explicitly non-clinical. Intimate media requires adult context, consent and provenance controls. Sensitive data is minimized and deletion/reset paths are expected.

The source report's claims about specific products, devices, SDKs, scientific capabilities, prices or legal status are not treated as verified facts; they are research inputs that require independent verification before implementation-specific commitments.
