# Ageni AI — Moje Alterego

Repozytorium kataloguje agentów AI, ich specyfikacje, architekturę, implementacje, testy i status wdrożenia.

## Stan wykonawczy

Główna warstwa wykonawcza korzysta ze wspólnego runtime'u OpenAI Responses API. Wszystkie agenty wpisane do rejestru mają sprawdzalne pliki wejściowe, a CI wykonuje kompilację entrypointów i testy offline przy każdym push/PR. Dostęp do OpenAI jest testowany osobnym, ręcznie uruchamianym smoke testem.

**Status implementacji: gotowy do użycia po ustawieniu `OPENAI_API_KEY`.**

## Katalog agentów

| Agent | Do czego służy | Zakres | Status | Dokumentacja |
|---|---|---|---|---|
| Agent Matematycznych Problemów Milenijnych (TRS) | Analizuje argumenty i materiały matematyczne związane z problemami milenijnymi; formalizuje hipotezy TRS i kontroluje rygor dowodowy. | Specyfikacja badawcza, protokół weryfikacji, architektura i plan implementacji. | **Implementacja CLI + wspólny runtime.** | [Dokumentacja](agents/millennium-mathematics/README.md) |
| Henri Cartier-Bresson — Decydujący Moment | Tworzy anglojęzyczne prompty street photography oparte na geometrii, synchronizacji ruchu i naturalnym świetle. | Śląsk 2026, dalmierzowy look, 50 mm, monochromatycznie, bez cropu po wykonaniu zdjęcia. | **Profil w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/README.md#1-henri-cartier-bresson) |
| Vivian Maier — Rain on Concrete | Tworzy intymne, uważne prompty uliczne z perspektywy aparatu trzymanego na wysokości talii. | Śląsk 2026, estetyka Rolleiflex, odbicia, autoportrety, kwadrat 1:1. | **Profil w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/README.md#2-vivian-maier) |
| Grand Press Photo — Reportaż społeczny | Tworzy etyczne, realistyczne prompty reportażowe o problemach społecznych i przemianach Śląska. | Samotność, izolacja, klimat, nierówności, odpowiedzialność dokumentalisty. | **Profil w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/README.md#3-grand-press-photo) |
| Leica Street Photography — Teatr ulicy | Tworzy wieloplanowe, dynamiczne prompty z kolorem, napięciem przestrzennym i absurdem codzienności. | Śląsk 2026, agresywna kompozycja, humor obserwacyjny, współczesna technologia. | **Profil w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/README.md#4-leica-street-photography) |
| Piękny Umysł Street Photography | Łączy cztery powyższe podejścia w jeden prompt: geometrię, intymność, reportażową empatię i uliczną ironię. | Agent-synteza do złożonych, narracyjnych promptów. | **Profil w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/README.md#5-piękny-umysł-street-photography) |
| Robert Capa — Cieszyn Humanist Photojournalism | Tworzy anglojęzyczne prompty inspirowane bliskością reporterską, dynamiką chwili i humanistycznym dokumentem. | Cieszyn i Český Těšín; 35/50 mm; monochromatyczna faktura analogowa; etyka i jawne oznaczanie rekonstrukcji. | **Profil + scenariusze w działającym Photo Specialist Agent.** | [Dokumentacja](agents/photo/robert-capa-cieszyn.md) |
| Architekt Światła i Geometrii Ciała | Tworzy production-ready prompty fotograficzne z kontrolą światła, geometrii ciała i parametrów obrazu. | Fine-art, portrait, boudoir, body geometry, światło i grading. | **Implementacja CLI + wspólny runtime.** | [System prompt](agents/architekt-swiatla-i-geometrii-ciala/SYSTEM_PROMPT.md) |

## Uruchamianie

Z katalogu głównego:

```bash
export OPENAI_API_KEY="..."
python agents/photo/agent.py "Stwórz koncepcję reportażu o pustoszejącej ulicy."
python agents/photo/specialist_agent.py --profile hcb "Rainy crossing in Cieszyn."
python agents/millennium-mathematics/agent.py "Wyjaśnij aktualny status problemu P vs NP."
python agents/architekt-swiatla-i-geometrii-ciala/agent.py "Portret w bocznym świetle przez żaluzje."
```

Model można zmienić per wywołanie przez `--model` albo globalnie przez `OPENAI_MODEL`. Domyślnie runtime używa `gpt-4.1-mini`, modelu zweryfikowanego przez repozytoryjny smoke test.

## Walidacja

Testy offline:

```bash
python -m unittest discover -s tests -v
python -m compileall -q agent_runtime agents scripts
```

Live smoke test OpenAI jest uruchamiany ręcznie z workflow GitHub Actions, aby nie wykonywać płatnych wywołań API przy każdym pushu.

## Zasady repozytorium

- Każdy agent otrzymuje własny katalog w `agents/`.
- Statusy rozróżniają projekt, implementację, testy i walidację.
- Hipotezy, twierdzenia warunkowe i dowody muszą być jawnie odróżnione.
- Nie oznaczamy funkcji jako działających, dopóki nie istnieje implementacja i weryfikowalny test.
- Nazwiska twórców i konkursów w opisach agentów oznaczają inspiracje/paradygmaty, nie afiliację ani autoryzację.

## CI

Workflow `.github/workflows/python-tests.yml`:
1. instaluje zależności,
2. kompiluje entrypointy,
3. uruchamia testy jednostkowe,
4. opcjonalnie wykonuje live OpenAI smoke test.

Repozytorium nie przechowuje klucza API; workflow używa sekretu `OPEN_API_KEY` mapowanego na `OPENAI_API_KEY`.
