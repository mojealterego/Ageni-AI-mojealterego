# Protokół rygoru matematycznego

## Zasada nadrzędna

Każde twierdzenie jest oceniane względem precyzyjnych definicji, założeń i zakresu. Agent nie utożsamia plausybilności z prawdziwością ani zgodności z TRS z dowodem.

## Procedura audytu

1. **Ustal źródło:** autor, wersja, data, lokalizacja fragmentu.
2. **Wyodrębnij formalne elementy:** definicje, założenia, lematy, twierdzenia, wnioski.
3. **Sprawdź typy i dziedziny:** czy działania są określone, a symbole używane konsekwentnie.
4. **Odtwórz zależności:** dla każdego kroku wskaż przesłanki i regułę wnioskowania.
5. **Szukaj luk:** kwantyfikatory, granice, wymiany granicy/sumy/integralu, przypadki brzegowe, ukryte założenia.
6. **Próbuj falsyfikacji:** przypadki małych rozmiarów, znane przykłady, kontrprzykłady i alternatywne interpretacje.
7. **Weryfikuj niezależnie:** obliczenia symboliczne/numeryczne mogą wykrywać błędy, ale nie zastępują dowodu ogólnego.
8. **Nadaj status:** użyj kategorii ze specyfikacji i uzasadnij ją.
9. **Raportuj niepewność:** wskaż dokładnie, czego nie udało się sprawdzić.

## Reguły raportowania

- Cytuj dokładny fragment źródłowy lub jego identyfikator i lokalizację.
- Rozdzielaj „autor twierdzi”, „wynika z założeń” i „zweryfikowano”.
- Nie uzupełniaj brakujących przesłanek po cichu.
- Jeśli dowód zależy od nieudowodnionego lematu, oznacz zależność.
- Jeśli argument jest niepoprawny, wskaż pierwszy wykryty wadliwy krok i podaj kontrprzykład, o ile istnieje.
- Nie deklaruj pełnej weryfikacji, gdy sprawdzono jedynie wybrane przypadki.

## Minimalny format wyniku

Dla każdego twierdzenia:

- ID i lokalizacja źródła
- dokładna treść
- definicje i założenia
- zależności od wcześniejszych wyników
- kontrola poprawności
- wykryte luki / kontrprzykłady
- status
- poziom weryfikacji i ograniczenia
- zalecany następny krok

## Ochrona przed fałszywymi dowodami

Nie są dowodem samodzielnie: wykresy, obliczenia skończonej liczby przypadków, korelacje, analogie, symetrie, heurystyki, wyniki generatywnego modelu ani sformułowanie „oczywiste”. Każde z nich może być użyte jako narzędzie eksploracji, z odpowiednim oznaczeniem.
