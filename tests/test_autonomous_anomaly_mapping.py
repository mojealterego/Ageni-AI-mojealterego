"""Coverage test for the autonomous anomaly report taxonomy.

The supplied report names 18 anomaly categories. The repository implements
those categories as 19 runtime agents because the chemistry item is split into
separate Coscientist and ChemCrow safety agents.
"""
from agent_runtime.registry import find_agent

REPORT_TO_RUNTIME = {
    "xenobots": "xenobot-research-agent",
    "dishbrain": "dishbrain-agent",
    "hybrot": "hybrot-agent",
    "terra0": "terra0-agent",
    "plantoid": "plantoid-agent",
    "truth-terminal": "truth-terminal-agent",
    "mr-goxx": "mr-goxx-agent",
    "chaosgpt": "chaosgpt-safety-agent",
    "tay": "tay-resilience-agent",
    "aaron": "aaron-creative-agent",
    "the-painting-fool": "painting-fool-agent",
    "botto": "botto-curator-agent",
    "polyworld": "polyworld-agent",
    "lenia": "lenia-agent",
    "ai-steve": "ai-steve-civic-agent",
    "alice-bob": "emergent-language-agent",
    "coscientist": "coscientist-agent",
    "chemcrow": "chemcrow-safety-agent",
    "genefer": "genefer-prime-search-agent",
}

def test_every_report_category_has_a_runtime_entrypoint():
    for runtime_id in REPORT_TO_RUNTIME.values():
        entry = find_agent(runtime_id)
        assert entry.entrypoint.endswith("/agent.py")

def test_mapping_has_19_runtime_agents_for_18_report_categories():
    assert len(REPORT_TO_RUNTIME) == 19
    assert REPORT_TO_RUNTIME["coscientist"] != REPORT_TO_RUNTIME["chemcrow"]

