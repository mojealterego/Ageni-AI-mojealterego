# Agent Matematycznych Problemów Milenijnych (TRS)

**Identyfikator:** `millennium-mathematics-trs`  
**Język dokumentacji:** polski  
**Status:** specyfikacja badawcza zapisana; kod agenta, automatyzacja i walidacja niezrealizowane.

## Przeznaczenie

Agent wspiera analizę formalną materiałów dotyczących problemów milenijnych, ze szczególnym uwzględnieniem P vs NP, hipotezy Riemanna, hipotezy Hodge’a i hipotezy Birch–Swinnerton-Dyera (BSD). Ma sprawdzać spójność definicji i argumentów, rozdzielać fakty matematyczne od hipotez oraz pomagać w przygotowaniu raportów i dokumentacji LaTeX.

**Nie jest** automatycznym dowodzącym ani potwierdzeniem rozwiązania któregokolwiek problemu.

## Dokumenty

- [Specyfikacja funkcjonalna i zakres](SPECIFICATION.md)
- [Protokół rygoru matematycznego](RESEARCH_PROTOCOL.md)
- [Architektura i plan implementacji](ARCHITECTURE.md)
- [Kontrola jakości i kryteria akceptacji](VALIDATION.md)
- [Diagramy LaTeX/TikZ](diagrams/README.md)

## Główne funkcje docelowe

1. Przyjmowanie tekstu, PDF lub źródeł LaTeX (po dodaniu parserów).
2. Segmentacja treści na definicje, założenia, lemata, twierdzenia i dowody.
3. Formalizacja twierdzeń i zależności w zapisie matematycznym.
4. Oznaczanie twierdzeń klasycznych, wyników warunkowych, hipotez TRS i twierdzeń niezweryfikowanych.
5. Wyszukiwanie luk logicznych, niejawnych założeń i potencjalnych kontrprzykładów.
6. Generowanie raportu audytu oraz materiałów LaTeX.

## Status

Na tym etapie zapisano dokumentację projektową. Nie ma jeszcze działającego kodu, parsera, integracji z systemem dowodzenia ani testów wykonawczych. TRS jest traktowana jako proponowany formalizm badawczy, którego definicje i aksjomaty wymagają jawnego podania oraz niezależnej oceny.
