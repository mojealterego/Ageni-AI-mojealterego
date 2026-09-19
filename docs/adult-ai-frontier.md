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
| Autonomous Relationship Mediator | `adult-ai-arm-mediator` | Consent-first relationship mediation support; no covert monitoring or autonomous communication changes. |
| Bio-Narrative Orchestrator | `adult-ai-bio-narrative-orchestrator` | Narrative planning with physiological uncertainty; no inference of consent or arousal and no direct hardware actuation. |
| PLE — Polykule Logistics Engine | `adult-ai-ple-polykule` | Multi-adult logistics, schedules and boundaries with participant-specific permissions and approval gates. |
| Cyrano — Social Vetting | `adult-ai-cyrano-social-vetting` | Evidence-first profile/communication vetting without age-from-face inference, diagnosis or doxxing. |
| Detachment Agent | `adult-ai-detachment` | Post-breakup boundary and attention-management planning without impersonation or covert monitoring. |
| BDSM Task Manager | `adult-ai-bdsm-task-manager` | Negotiated adult task/check-in planning with revocable consent and no physical-device enforcement. |
| Legacy Archivist | `adult-ai-legacy-archivist` | Consent-controlled memory archiving with provenance, participant review, withdrawal and deletion workflows. |

## Runtime contract

Each agent uses the repository's shared `AgentSpec` / `run_agent` runtime. The batch does not add provider-side device control, media publication, clinical treatment, or other external side effects. Those remain adapter responsibilities behind explicit authorization, policy checks and postcondition verification.

## Safety decisions carried into code

Physiological signals are treated as noisy measurements rather than reliable emotion/arousal detectors. Haptic generation is declarative and separated from the hardware safety controller. Relationship and conversation agents distinguish observation from inference and fiction from real-world claims. Clinical/trauma-adjacent functionality is explicitly non-clinical. Intimate media requires adult context, consent and provenance controls. Sensitive data is minimized and deletion/reset paths are expected.

The source report's claims about specific products, devices, SDKs, scientific capabilities, prices or legal status are not treated as verified facts; they are research inputs that require independent verification before implementation-specific commitments.

## Horizon 2030 extension — implementation boundaries

The extension batch keeps the same shared-runtime contract. ARM is a reflection/mediation assistant, not a therapist or arbiter. PLE records participant-specific permissions and confirmed agreements rather than negotiating boundaries for absent people. Cyrano reports evidence and uncertainty rather than age estimates, personality diagnoses or accusations. Detachment supports user-controlled communication limits without impersonation. The BDSM Task Manager organizes voluntary tasks and stop mechanisms but does not operate restraints or other physical hazards. Legacy Archivist preserves provenance and user control; generated reconstructions are explicitly labeled as reconstructions rather than guaranteed replicas.

For any sensor, communication, media, device or archival integration, authorization, policy checks, auditability, data minimization and postcondition verification remain separate control-plane responsibilities.
