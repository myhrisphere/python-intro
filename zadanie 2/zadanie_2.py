# Zadanie 2
# Cel zadania
#   1. Zapoznanie się z podstawami testowania aplikacji w Pythonie.
#   2. Nauka podejścia Test-Driven Development (TDD).
#   3. Implementacja testów jednostkowych z wykorzystaniem modułu unittest.
#   4. Wykorzystanie testów do poprawy jakości kodu.
#   5. Zapoznanie się z narzędziami do analizy pokrycia testowego.
#
# Zakres zadania
#   1. Implementacja testów jednostkowych w Pythonie.
#   2. Praca w podejściu Test-Driven Development.
#   3. Zaprojektowanie i zaimplementowanie pięciu funkcji o ustalonej, jasno zdefiniowanej funkcjonalności– powinny być zróżnicowane (np. operacje na ciągach znaków, 
#   przetwarzanie list, proste obliczenia matematyczne, zarządzanie danymi itd.).
#   4. Modyfikacja kodu w celu spełnienia testów.
#   5. Zapoznanie się z zaawansowanymi technikami testowania, takimi jak testy parametryzowane.
#   6. Analiza pokrycia kodu testami.
#   7. Publikacja wyników na GitHub i złożenie zadania na Moodle.
#
# Wymagania
#   W pliku app.py należy zaimplementować pięć funkcji o ustalonej, jasno zdefiniowanej funkcjonalności. Przykładowe pomysły:
#       • Funkcja sprawdzająca poprawność adresu e-mail.
#       • Funkcja dokonująca prostych obliczeń matematycznych (np. obliczanie pola figury).
#       • Funkcja przetwarzająca listę danych (np. filtracja, sortowanie).
#       • Funkcja konwertująca format dat.
#       • Funkcja sprawdzająca, czy tekst jest palindromem.
#   Każda funkcja powinna mieć jasno określony cel i parametry wejściowe/wyjściowe.
#   
#   Test-Driven Development– cykl pracy
#       1. Napisanie testu– przed napisaniem kodu, najpierw tworzymy testy sprawdzające oczekiwane zachowanie.
#       2. Uruchomienie testów– testy powinny na początku nie przechodzić (ponieważ kod nie jest jeszcze napisany).
#       3. Implementacja funkcji– tworzymy minimalny kod, który spełnia testy.
#       4. Uruchomienie testów ponownie– sprawdzamy, czy testy przechodzą.
#       5. Refaktoryzacja– jeśli kod działa poprawnie, można go zoptymalizować.
#       6. Analiza pokrycia testowego– sprawdzamy, jakie fragmenty kodu nie zostały przetestowane.
# 
#   Implementacja testów w Pythonie
#       • Każda z pięciu funkcji powinna mieć co najmniej trzy testy jednostkowe, uwzględniające typowe przypadki, przypadki brzegowe oraz błędne dane wejściowe (jeśli dotyczy).
#       • Korzystaj z metodasercji dostarczanych przez unittest (np. assertEqual, assertTrue, assertRaises, itd.).
#       • Dla uzyskania lepszej organizacji testów, skorzystaj z klasy dziedziczącej po unittest.TestCase.