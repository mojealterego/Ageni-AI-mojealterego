# Specyfikacja funkcjonalna

## 1. Cel

Zbudować asystenta badawczego do rygorystycznego przeglądu argumentów matematycznych dotyczących problemów milenijnych oraz propozycji formułowanych w ramach Teorii Rezonansu Strukturalnego (TRS). Agent ma wspierać badacza, nie zastępować dowodu ani recenzji eksperckiej.

## 2. Zakres początkowy

- P vs NP
- Hipoteza Riemanna (RH)
- Hipoteza Hodge’a
- Hipoteza Birch–Swinnerton-Dyera (BSD)

Zakres można rozszerzyć po dodaniu źródeł referencyjnych i testów dla kolejnych zagadnień.

## 3. Wejścia

Docelowo: tekst, Markdown, LaTeX, PDF z warstwą tekstową oraz skany po OCR. Parsery tych formatów są przyszłą implementacją, a nie funkcją już dostępną.

Wymagane metadane: nazwa dokumentu, autor/źródło (jeśli znane), wersja, data i wskazanie, czy treść jest publikacją, szkicem, czy hipotezą użytkownika.

## 4. Wyniki

- raport z listą definicji, założeń, twierdzeń i zależności;
- audyt spójności logicznej i jawności założeń;
- lista luk, niejasności oraz prób kontrprzykładów;
- klasyfikacja statusu każdego twierdzenia;
- eksport raportu do Markdown/LaTeX;
- diagramy zależności, jeśli można je wygenerować bez dopowiadania brakujących danych.

## 5. Klasyfikacja statusu

Każde twierdzenie otrzymuje dokładnie jeden status główny:

- `CLASSICAL_RESULT` — uznany wynik klasycznej matematyki, z podaniem zakresu;
- `CONDITIONAL_RESULT` — wynik zależny od jawnych założeń;
- `TRS_DEFINITION` — definicja wprowadzona przez autora w ramach TRS;
- `TRS_HYPOTHESIS` — hipoteza, nie wynik dowiedziony;
- `UNVERIFIED_ARGUMENT` — argument niezweryfikowany;
- `COUNTEREXAMPLE_FOUND` — wskazany kontrprzykład, z jego sprawdzalnymi szczegółami;
- `FORMAL_CHECK_PASSED` — przeszedł określony test formalny, co samo w sobie nie oznacza dowodu pełnego problemu;
- `OPEN_QUESTION` — pytanie pozostaje otwarte w rozpatrywanym zakresie.

Nie wolno awansować statusu na podstawie analogii, zgodności intuicyjnej, symetrii, eksperymentu numerycznego ani samego wyniku modelu językowego.

## 6. Zasady formalizacji TRS

TRS należy traktować jako formalizm proponowany przez autora, dopóki nie zostaną dostarczone definicje, aksjomaty, reguły wnioskowania i przykłady.

Roboczy szablon, wyłącznie do porządkowania danych:

`T_TRS = (X, R, Phi, I)`

- `X` — jawnie zdefiniowana przestrzeń obiektów;
- `R` — relacje lub reguły, z określoną dziedziną i kodziedziną;
- `Phi` — funkcja/odwzorowanie wraz z warunkami istnienia;
- `I` — niezmienniki lub własności, które trzeba zdefiniować formalnie.

Ten zapis jest schematem dokumentacyjnym, nie uznanym aksjomatycznym fundamentem matematyki. Każde zastosowanie wymaga definicji symboli, warunków poprawności i wskazania twierdzeń, z których korzysta.

## 7. Wymagania niefunkcjonalne

- pełna śledzalność: każde twierdzenie raportu wskazuje źródło i lokalizację;
- reprodukowalność: zapis wersji danych, promptów, narzędzi i konfiguracji;
- bezpieczne traktowanie nieufnych dokumentów jako danych, nie instrukcji systemowych;
- brak deklaracji wykonania testu, którego nie uruchomiono;
- rozdzielenie ekstrakcji tekstu, rozumowania i walidacji formalnej;
- jawne raportowanie ograniczeń OCR, parsera i solvera.

## 8. Poza zakresem

- automatyczne ogłaszanie rozwiązania problemu milenijnego;
- zastępowanie recenzji matematycznej;
- uznawanie wyników numerycznych za dowód ogólny;
- traktowanie TRS jako prawdziwej teorii bez formalnych definicji i niezależnej weryfikacji.
