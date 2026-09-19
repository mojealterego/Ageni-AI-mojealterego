# Korepetytorzy zawodowi — zestaw agentów

Moduł zawiera 11 profili promptowych uruchamianych przez wspólny runner `agents/vocational-tutors/agents.py`:

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

## Uruchomienie

Z katalogu głównego repozytorium:

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."
python agents/vocational-tutors/agents.py --agent matematyka "Wyjaśnij deltę"
```

Można podać `--model`; bez niego używany jest domyślny model runtime. Zamiast argumentu tekstowego można przekazać treść przez stdin.

## Zakres wdrożenia i ograniczenia

To działające na poziomie kodu profile instrukcji korzystające z istniejącego `AgentSpec`/`run_agent`. Nie są jeszcze podłączone do centralnego routera, aplikacji użytkownika, LMS ani szkolnego systemu kont. Nie mają niezależnych narzędzi do przeglądania źródeł, oceniania, pamięci ucznia ani integracji z CKE.

To nie jest produkcyjny system bezpieczeństwa dla nieletnich ani certyfikowany nauczyciel. Przed użyciem w szkole wymagane są m.in. testy, przegląd bezpieczeństwa i prywatności, polityka retencji, kontrola dostępu, procedury kryzysowe oraz weryfikacja aktualnych podstaw programowych, kwalifikacji i przepisów. Wygenerowane instrukcje CNC, budowlane, gastronomiczne, finansowe i pierwszej pomocy wymagają odpowiedniej weryfikacji przez człowieka.

Profile celowo nie wymagają ujawniania ukrytego chain-of-thought; proszą o zwięzłe, sprawdzalne wyjaśnienia.