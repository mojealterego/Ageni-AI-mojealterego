# SAAD — szkolny zestaw agentów korepetytorów

Moduł `agent.py` zawiera 22 profile dydaktyczne dla polskiej szkoły podstawowej. Profile są osobne (ID, zakres klas, przedmiot, styl, metody i zabezpieczenia), a wspólna funkcja `run_tutor()` zwraca ustrukturyzowany plan naprowadzania dla adaptera LLM.

## Uruchomienie

```python
from agents.saad_school_tutors.agent import run_tutor

plan = run_tutor(
    "saad-logic-master",
    grade="V",
    topic="ułamki",
    learner_attempt="3/4",
)
```

Folder ma nazwę z myślnikami, więc w projekcie bez pakietu Python można załadować plik przez `importlib`; test robi to w ten sposób.

## Zakres profili

Mentor Odkrywców; Playful Polyglot; Kustosz Słowa; Kronikarz Analityczny; Globalny Komunikator; Strażnik Tożsamości; Mistrz Logiki; Architekt Cyfrowy; Przewodnik Terenowy; Bio-Eksplorator; Geo-Strateg; Laborant Teoretyczny; Fizyk Fundamentalny; Wizjoner Estetyczny; Maestro Dźwięku; Inżynier Bezpieczeństwa; Aktywista Demokratyczny; Coach Dobrostanu; Instruktor Reagowania Kryzysowego; Trener Teoretyk; Architekt Kariery; Mediator Klasowy; Filozof Moralny.

## Zasady bezpieczeństwa

- Agent naprowadza i sprawdza rozumienie; nie wykonuje za ucznia ocenianych prac.
- Minimalizacja danych osobowych.
- Wsparcie emocjonalne nie zastępuje opiekuna, nauczyciela ani specjalisty.
- Obywatelskość prowadzona neutralnie, bez perswazji wyborczej.
- Medycyna i pierwsza pomoc: treści dostosowane do wieku, pilne zagrożenie kierowane do dorosłego i/lub numeru 112.
- Chemia, technika i EDB nie zachęcają do niebezpiecznych eksperymentów ani samodzielnego obchodzenia się z bronią.

## Weryfikacja

Testy w `tests/test_saad_school_tutors.py`. Uruchom z katalogu głównego repozytorium: `pytest -q tests/test_saad_school_tutors.py`.
