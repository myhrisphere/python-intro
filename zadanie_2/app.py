import re
from datetime import datetime

# 1. Sprawdzanie poprawności adresu e-mail
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 2. Obliczanie pola prostokąta
def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Wymiary muszą być większe od zera.")
    return width * height

# 3. Filtracja liczb parzystych z listy
def filter_even_numbers(data):
    return [x for x in data if isinstance(x, int) and x % 2 == 0]

# 4. Konwersja formatu daty (dd/mm/yyyy -> yyyy-mm-dd)
def convert_date_format(date_str):
    try:
        date = datetime.strptime(date_str, '%d/%m/%Y')
        return date.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("Niepoprawny format daty. Oczekiwano formatu dd/mm/yyyy.")

# 5. Sprawdzanie czy tekst jest palindromem
def is_palindrome(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned_text == cleaned_text[::-1]
