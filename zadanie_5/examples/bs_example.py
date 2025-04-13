import requests
from bs4 import BeautifulSoup

# Pobierz HTML ze strony
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Znajdź wszystkie cytaty na stronie
quotes = soup.find_all("span", class_="text")

print("Znalezione cytaty:")
for quote in quotes:
    print("-", quote.text)