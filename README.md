# Ageni AI — Moje Alterego

Repozytorium kataloguje agentów AI, ich specyfikacje, architekturę, implementacje, testy i status wdrożenia.

## Katalog agentów

| Agent | Do czego służy | Zakres | Status | Dokumentacja |
|---|---|---|---|---|
| Agent Matematycznych Problemów Milenijnych (TRS) | Analizuje argumenty i materiały matematyczne związane z problemami milenijnymi; formalizuje hipotezy TRS i kontroluje rygor dowodowy. | Specyfikacja badawcza, protokół weryfikacji, architektura i plan implementacji. | **Specyfikacja zapisana; implementacja i walidacja matematyczna nieukończone.** | [Dokumentacja](agents/millennium-mathematics/README.md) |
| Henri Cartier-Bresson — Decydujący Moment | Tworzy anglojęzyczne prompty street photography oparte na geometrii, synchronizacji ruchu i naturalnym świetle. | Śląsk 2026, dalmierzowy look, 50 mm, monochromatycznie, bez cropu po wykonaniu zdjęcia. | **Specyfikacja zapisana; prompt-agent, bez kodu wykonawczego.** | [Dokumentacja](agents/photo/README.md#1-henri-cartier-bresson) |
| Vivian Maier — Rain on Concrete | Tworzy intymne, uważne prompty uliczne z perspektywy aparatu trzymanego na wysokości talii. | Śląsk 2026, estetyka Rolleiflex, odbicia, autoportrety, kwadrat 1:1. | **Specyfikacja zapisana; prompt-agent, bez kodu wykonawczego.** | [Dokumentacja](agents/photo/README.md#2-vivian-maier) |
| Grand Press Photo — Reportaż społeczny | Tworzy etyczne, realistyczne prompty reportażowe o problemach społecznych i przemianach Śląska. | Samotność, izolacja, klimat, nierówności, odpowiedzialność dokumentalisty. | **Specyfikacja zapisana; prompt-agent, bez kodu wykonawczego.** | [Dokumentacja](agents/photo/README.md#3-grand-press-photo) |
| Leica Street Photography — Teatr ulicy | Tworzy wieloplanowe, dynamiczne prompty z kolorem, napięciem przestrzennym i absurdem codzienności. | Śląsk 2026, agresywna kompozycja, humor obserwacyjny, współczesna technologia. | **Specyfikacja zapisana; prompt-agent, bez kodu wykonawczego.** | [Dokumentacja](agents/photo/README.md#4-leica-street-photography) |
| Piękny Umysł Street Photography | Łączy cztery powyższe podejścia w jeden prompt: geometrię, intymność, reportażową empatię i uliczną ironię. | Agent-synteza do złożonych, narracyjnych promptów fotograficznych. | **Specyfikacja zapisana; prompt-agent, bez kodu wykonawczego.** | [Dokumentacja](agents/photo/README.md#5-piękny-umysł-street-photography) |

## Zasady repozytorium

- Każdy agent otrzymuje własny katalog w `agents/`.
- Statusy rozróżniają projekt, implementację, testy i walidację.
- Hipotezy, twierdzenia warunkowe i dowody muszą być jawnie odróżnione.
- Nie oznaczamy funkcji jako działających, dopóki nie istnieje implementacja i weryfikowalny test.
- Nazwiska twórców i konkursów w opisach agentów oznaczają inspiracje/paradygmaty, nie afiliację ani autoryzację.

## Status projektu

Repozytorium jest katalogiem rozwijanych agentów. Wpisy w tabeli odzwierciedlają stan faktycznie zapisanych artefaktów, nie deklarację gotowości produkcyjnej.
