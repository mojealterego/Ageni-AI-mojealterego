# Walidacja i kryteria akceptacji

## Aktualny stan

Dokumentacja projektowa została zapisana. Nie istnieje jeszcze kod wykonawczy, zatem testy jednostkowe, integracyjne, parsera ani formalnego dowodzenia nie zostały uruchomione.

## Kryteria akceptacji dla przyszłej implementacji

- [ ] Każdy wyodrębniony claim ma identyfikator i lokalizację źródłową.
- [ ] Parser zachowuje symbole, indeksy, kwantyfikatory i strukturę równań.
- [ ] Brakujące definicje są zgłaszane, a nie dopowiadane.
- [ ] Statusy wyników są zgodne z `SPECIFICATION.md`.
- [ ] Wyniki formalnego solvera zawierają nazwę narzędzia, wersję, plik wejściowy i zakres sprawdzenia.
- [ ] Testy obejmują błędne rozumowania, przypadki brzegowe i regresje.
- [ ] Raport rozdziela wyniki klasyczne, twierdzenia warunkowe i hipotezy TRS.
- [ ] Błędy OCR i niepewność ekstrakcji są widoczne w raporcie.
- [ ] Dokumentacja uruchomienia i konfiguracji jest odtwarzalna.

## Zestaw testowy wymagany przed oznaczeniem „gotowy”

1. Parsowanie przykładowego tekstu i LaTeX z definicją, lematem i dowodem.
2. Wykrycie niezdefiniowanego symbolu.
3. Wykrycie nieuzasadnionego przejścia logicznego w kontrolowanym przykładzie.
4. Wykrycie sprzecznych założeń.
5. Zachowanie lokalizacji przy ekstrakcji z wielu sekcji.
6. Próba kontrprzykładu dla twierdzenia o skończonej dziedzinie.
7. Test, że eksperyment numeryczny nie jest klasyfikowany jako dowód ogólny.
8. Test, że brak formalnej specyfikacji TRS skutkuje jawnym komunikatem, a nie wygenerowaniem aksjomatów.

## Warunki oznaczenia statusu

- **Specyfikacja:** dokumenty i kontrakty są zapisane.
- **Implementacja:** kod istnieje i ma instrukcję uruchomienia.
- **Testy:** automatyczne testy zostały rzeczywiście wykonane, z raportem wyniku.
- **Walidacja formalna:** konkretne twierdzenia zostały sprawdzone w wskazanym formalnym systemie.
- **Gotowy:** spełniono uzgodnione kryteria dla określonej wersji i zakresu; nie oznacza to rozwiązania problemu milenijnego.
