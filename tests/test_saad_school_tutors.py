"""Tests for the SAAD school tutor profile catalogue."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "agents" / "saad-school-tutors" / "agent.py"
spec = importlib.util.spec_from_file_location("saad_school_tutors", MODULE)
saad = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(saad)

def test_catalogue_has_22_distinct_tutors():
    assert len(saad.PROFILES) == 22
    assert len(set(saad.AGENT_IDS)) == 22

def test_all_profiles_have_common_safeguards():
    for profile in saad.PROFILES.values():
        assert any("graded homework" in rule for rule in profile.safeguards)
        assert any("personal data" in rule for rule in profile.safeguards)

def test_unknown_agent_fails_closed():
    try:
        saad.get_profile("unknown tutor")
    except KeyError:
        pass
    else:
        raise AssertionError("unknown tutor must not resolve")

def test_scaffold_requires_topic():
    result = saad.run_tutor("saad-logic-master", grade="V", topic="")
    assert result["status"] == "needs_context"

def test_scaffold_returns_guardrails_and_question_contract():
    result = saad.run_tutor("saad-logic-master", grade="V", topic="ułamki", learner_attempt="3/4")
    assert result["agent_id"] == "saad-logic-master"
    assert "safeguards" in result
    assert "zadaj jedno pytanie" in result["response_contract"]
