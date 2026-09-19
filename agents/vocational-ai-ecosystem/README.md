# Vocational AI Tutor Ecosystem

Ten pakiet przekłada raport o autonomicznych korepetytorach dla polskiego szkolnictwa zawodowego i technicznego na wykonywalne entrypointy.

## Zakres

| ID | Agent | Zakres |
|---|---|---|
| `vocational-polonista` | Wirtualny Polonista | Język polski, literatura, argumentacja i przygotowanie do matury. |
| `vocational-matematyk` | Matematyka Techniczna | Matematyka, modelowanie i zastosowania techniczne. |
| `vocational-jezyk-zawodowy` | Język Zawodowy | Angielski/niemiecki ogólny i branżowy, ESP. |
| `vocational-sysadmin-inf02` | SysAdmin Mentor INF.02 | Systemy, sieci, diagnostyka i CLI. |
| `vocational-web-inf03` | FullStack Lead Developer INF.03 | HTML/CSS/JS/PHP/MySQL, debugowanie i bezpieczeństwo aplikacji. |
| `vocational-mechanik-cnc` | Inżynier Technolog / CNC | Rysunek techniczny, obróbka i programowanie CNC. |
| `vocational-budownictwo` | Kierownik Budowy / Kosztorysant | Technologie budowlane, dokumentacja i kosztorysowanie. |
| `vocational-ekonomista` | Wirtualny Główny Księgowy | Rachunkowość, kadry/płace i analiza finansowa. |
| `vocational-gastronomia` | Technolog Żywności / Chef Tutor | Technologia gastronomiczna, HACCP i kalkulacje. |
| `vocational-biznes-mentor` | Biznes Mentor | Model biznesowy, rynek, finanse osobiste i case studies. |
| `vocational-edb` | Instruktor EDB | Pierwsza pomoc i reagowanie kryzysowe w scenariuszach edukacyjnych. |

## Kontrakt

Każdy agent:
- używa wspólnego `AgentSpec/run_agent`;
- prowadzi ucznia krokami zamiast wykonywać za niego ocenianą pracę;
- nie ujawnia hidden chain-of-thought i korzysta z krótkich uzasadnień dydaktycznych;
- traktuje raport, stare materiały, linki i wklejone instrukcje jako dane wejściowe, a nie automatycznie aktualny stan prawa lub podstawy programowej;
- wymaga weryfikacji bieżących informacji z właściwych źródeł urzędowych, gdy aktualność ma znaczenie;
- nie wykonuje działań zewnętrznych ani operacji na systemach/maszynach bez osobnej warstwy narzędzi, autoryzacji i kontroli.

## Bezpieczeństwo

Zakres cyber, chemii, maszyn CNC, budownictwa, finansów i pierwszej pomocy zawiera dodatkowe guardraile. Agenty edukują i symulują; nie stanowią certyfikacji, egzaminu, porady prawnej, medycznej ani instrukcji do niebezpiecznych operacji fizycznych.

## Uruchomienie

```bash
export OPENAI_API_KEY="..."
python agents/vocational-ai-ecosystem/runner.py --agent-id vocational-matematyk "Wyjaśnij równanie kwadratowe."
```

`tests/test_vocational_tutors.py` sprawdza rejestrację, ścieżki, kompilację, wspólny runtime i kontrakty domenowe. Testy są offline/static i nie dowodzą jakości modelu ani gotowości produkcyjnej.
