# Zadanie 1
# Wyszukaj w dokumentacji Pythona co najmniej trzy zagadnienia:
# • Opis funkcji wbudowanej (zip() w tym wypadku)
# • Opis modułu z biblioteki standardowej (random w tym wypadku)
# • Opis wyjątku (ZeroDivisionError w tym wypadku)
# Podaj krótkie wyjaśnienie każdego zagadnienia oraz link do dokumentacji

# Program powinien wykonywać:
# • Tworzenie dwóch list i łączenie ich funkcją zip().
# • Wykorzystanie jednej funkcji z wybranego modułu Pythona. | (random.randint w tym wypadku)
# • Obsługę wyjątku try-except.
# • Komentarze w kodzie z opisem użytych funkcji i linkami do dokumentacji.

# Importujemy moduł random
# Moduł random służy do generowania liczb losowych i wykonywania operacji losowania.
# Umożliwia generowanie liczb całkowitych, zmiennoprzecinkowych oraz wybór losowych elementów z sekwencji.
# Dokumentacja modułu random: https://docs.python.org/pl/3/library/random.html
import random

# Tworzymy dwie listy z losowymi liczbami
lista_a = [random.randint(1, 50) for _ in range(5)]
lista_b = [random.randint(1, 50) for _ in range(5)]

# Łączymy listy za pomocą funkcji zip()
# Funkcja zip() łączy elementy dwóch list w pary
# Funkcja zwraca iterator, dlatego konwertujemy go na listę
# Dokumentacja funkcji zip(): https://docs.python.org/pl/3/tutorial/datastructures.html
polaczone_listy = list(zip(lista_a, lista_b))
print("Połączone listy:", polaczone_listy)

# Wykorzystanie funkcji z modułu random
# Funkcja random.randint() zwraca losową liczbę całkowitą z podanego przedziału
# Dokumentacja funkcji random.randint(): https://docs.python.org/pl/3/library/random.html#random.randint
dzielnik = random.randint(-1, 1)
print(f"Wylosowany dzielnik to: {dzielnik}")

# Obsługa wyjątku try-except
try:
    # Próba wykonania dzielenia przez zero
    wynik = 100 / dzielnik
    print(f"Wynik dzielenia: {wynik}")
except ZeroDivisionError:
    # Dokumentacja wyjątków: https://docs.python.org/pl/3/tutorial/errors.html
    print("Nie można dzielić przez zero!")