# Autonomous Anomaly Lab

A bounded, simulation-first catalog inspired by the supplied taxonomy report. The module exposes 18 stable profiles via `list_agents()` and `run_agent(agent_id, task)`.

## Scope

Profiles cover xenobot research, DishBrain, hybrots, Terra0, Plantoid, memetic media, paper trading, autonomy safety, online-learning poisoning, symbolic art, affect-themed creativity, Botto-style curation, Polyworld, Lenia, civic feedback, emergent negotiation, chemistry literature, and Genefer compute planning.

## Safety and implementation boundary

This is a software research/planning layer—not a deployment of biological systems or autonomous economic actors. It intentionally excludes wet-lab procedures, live trading, wallet custody, destructive planning, manipulative political targeting, hazardous chemistry operations, and physical actuation. Simulations must be bounded; external actions require separately implemented permissions and human approval.

## API

```python
from agents.autonomous_anomaly_lab.agent import list_agents, run_agent

profiles = list_agents()
brief = run_agent("lenia-sandbox", "Explore bounded pattern classes")
```

The host application is responsible for connecting a model, validating outputs, enforcing policy, and recording approvals. This module itself does not call external services or execute tasks.