# Autonomous Anomaly / Frontier Agent Batch

This batch converts the supplied compendium of unusual autonomous-system case studies into 19 executable specialist agents in the repository.

## Included agents

| ID | Agent | Operational boundary |
|---|---|---|
| xenobot-research-agent | Xenobot Research Agent | Scientific analysis/simulation; no live wetware procedures |
| dishbrain-agent | DishBrain Agent | MEA/neural-computing simulation; no live-cell or lab control |
| hybrot-agent | Hybrot Agent | Hybrid neuron/robot architecture; physical control is approval-gated |
| terra0-agent | Terra0 Autonomous Forest Simulator | DAO/forest simulation; no real asset acquisition or transactions |
| plantoid-agent | Plantoid Agent | Art-organism/economic simulation; virtual credits only |
| truth-terminal-agent | Truth Terminal Analysis Agent | Memetic/crypto dynamics analysis; no manipulation or trading |
| mr-goxx-agent | Mr. Goxx Trading Simulator | Reproducible paper trading only |
| chaosgpt-safety-agent | ChaosGPT Safety Simulator | Misalignment/containment testing in a mocked sandbox |
| tay-resilience-agent | Tay Resilience Agent | Continual-learning poisoning/resilience tests using synthetic data |
| aaron-creative-agent | AARON Creative Agent | Symbolic computational art planning |
| painting-fool-agent | Painting Fool Agent | Explainable state-driven computational creativity |
| botto-curator-agent | Botto Curator Agent | Generative-art curation and virtual-governance simulation |
| polyworld-agent | Polyworld Agent | Artificial-life simulation with digital organisms |
| lenia-agent | Lenia Agent | Continuous cellular-automata / artificial-life simulation |
| ai-steve-civic-agent | AI Steve Civic Agent | Neutral civic aggregation; no voter targeting/persuasion |
| emergent-language-agent | Emergent Language Agent | Bounded multi-agent communication experiments |
| coscientist-agent | Coscientist Research Agent | Scientific planning/reproducibility; no autonomous lab execution |
| chemcrow-safety-agent | ChemCrow Safety Agent | Chemistry information/computation; no dangerous synthesis or robot control |
| genefer-prime-search-agent | Genefer Prime Search Agent | Reproducible number-theoretic workload planning |

## Common contract

All 19 entrypoints use agent_runtime.openai_agent.AgentSpec + run_agent. Each returns an interpretation, plan, assumptions/evidence gaps, safety or authorization gates, reproducibility details and verification status.

The compendium's case studies are treated as research inputs, not permission to reproduce hazardous or financially consequential capabilities. Real-money transfers, trading, political persuasion, autonomous publication, wet-lab manipulation and unbounded compute are outside the default execution contract.

## Verification

Integration coverage is in tests/test_anomaly_agents.py. It checks registry membership, exact entrypoint paths, Python compilation, shared-runtime usage and explicit non-execution guardrails for high-risk domains.
