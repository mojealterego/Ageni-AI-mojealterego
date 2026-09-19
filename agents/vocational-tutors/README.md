# Korepetytorzy zawodowi — etap wdrożenia 2

Moduł zawiera 11 wyspecjalizowanych profili dla polskiego szkolnictwa ogólnego, technicznego i branżowego, uruchamianych przez wspólny runtime:

| ID | Zakres |
|---|---|
| `polonista` | Język polski i literatura |
| `matematyka` | Matematyka STEM |
| `jezyki` | Języki obce zawodowe |
| `inf02` | Administracja systemami i sieciami |
| `inf03` | Programowanie webowe |
| `mechanik` | Mechanika i podstawy CNC |
| `budownictwo` | Budownictwo i kosztorysowanie |
| `ekonomista` | Ekonomia, dokumenty i obliczenia |
| `gastronomia` | Gastronomia i HACCP |
| `biznes` | Biznes i zarządzanie |
| `edb` | Edukacja dla bezpieczeństwa |

## Co zostało dodane w tym etapie

Profile są teraz podłączone do centralnego `agent_runtime/registry.py` i korzystają z istniejącego runtime OpenAI. Runner używa również istniejącej deterministycznej warstwy sesji i wstępnego bezpieczeństwa dla uczniowskich interakcji: limity sesji, hard-stop dla części wzorców zagrożenia, opcjonalny mechanizm potwierdzenia silnych emocji oraz kontrola odpowiedzi.

Uruchomienie:

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."
python agents/vocational-tutors/agents.py --agent matematyka "Wyjaśnij deltę"
```

Dodatkowe sterowanie sesją:

```bash
python agents/vocational-tutors/agents.py --agent matematyka --session-id uczen-01 "Rozwiąż zadanie"
python agents/vocational-tutors/agents.py --agent bufor --session-id uczen-01 --reset-session
```

## Granice wdrożenia

To nadal profilowane agenty oparte na promptach, a nie certyfikowany system szkolny. Repozytorium nie przyznaje im automatycznie dostępu do LMS, dziennika, kont uczniowskich, CKE, ERP, urządzeń, maszyn ani systemów produkcyjnych.

Przed użyciem z uczniami potrzebne są co najmniej: aktualna weryfikacja podstaw programowych i wymagań egzaminacyjnych, kontrola dostępu, polityka retencji/usuwania danych, przegląd prywatności i bezpieczeństwa, testy adversarialne, human-in-the-loop dla działań konsekwencyjnych oraz walidacja aktualnych norm, przepisów, stawek i procedur.

W szczególności: instrukcje CNC, budowlane, gastronomiczne, finansowe, podatkowe oraz pierwszej pomocy są materiałem edukacyjnym i wymagają weryfikacji według aktualnych źródeł oraz odpowiedniego nadzoru człowieka.
