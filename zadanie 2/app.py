import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return width * height

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def format_date(date):
    try:
        year, month, day = date.split('-')
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Invalid date format")

def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]
