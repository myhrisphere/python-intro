# 🚴‍♂️ Zadanie 4 – Metody MCDM z wykorzystaniem biblioteki `pymcdm`

## 🎯 Temat
Ocena alternatyw w wyborze roweru miejskiego z użyciem metod wielokryterialnego podejmowania decyzji: **TOPSIS**, **SPOTIS** oraz **VIKOR**, z pomocą biblioteki `pymcdm`.

## 🚲 Alternatywy

1. Kross Trans 5.0  
2. Romet Gazela 4  
3. Merida Crossway 300  
4. Kellys Phanatic 10

## 📊 Kryteria

| Kryterium       | Typ   | Jednostka | Opis                                     |
|------------------|--------|------------|-------------------------------------------|
| Cena            | Min    | zł         | Im taniej, tym lepiej                     |
| Waga            | Min    | kg         | Lżejszy rower jest bardziej komfortowy    |
| Liczba biegów   | Max    | liczba     | Więcej przełożeń to większa elastyczność  |

> ❗ Nie uwzględniono pojemności bagażnika jako kryterium w analizie.

## 🧮 Dane decyzyjne

| Rower                 | Cena (zł) | Waga (kg) | Biegi |
|------------------------|------------|------------|--------|
| Kross Trans 5.0        | 3199       | 17.5       | 24     |
| Romet Gazela 4         | 2899       | 18.0       | 21     |
| Merida Crossway 300    | 3499       | 14.8       | 27     |
| Kellys Phanatic 10     | 2999       | 16.2       | 24     |

## ⚖️ Wagi

Wagi dla poszczególnych kryteriów wyznaczone zostały metodą **entropii** na podstawie znormalizowanej macierzy decyzyjnej.

## 🧪 Zastosowane metody

- **TOPSIS** – mierzy odległość od rozwiązania idealnego
- **SPOTIS** – ocenia odległość od ustalonych granic
- **VIKOR** – kompromis pomiędzy maksymalizacją korzyści i minimalizacją strat

## 📈 Wyniki

| Rower                 | TOPSIS | SPOTIS | VIKOR | TOPSIS Rank | SPOTIS Rank | VIKOR Rank |
|------------------------|--------|--------|--------|--------------|---------------|--------------|
| Kross Trans 5.0        | 0.5000 | 0.5000 | 0.5000 | 3            | 3             | 2            |
| Romet Gazela 4         | 1.0000 | 0.0000 | 0.0000 | 1            | 1             | 4            |
| Merida Crossway 300    | 0.0000 | 1.0000 | 1.0000 | 4            | 4             | 1            |
| Kellys Phanatic 10     | 0.8333 | 0.1667 | 0.1667 | 2            | 2             | 3            |

## 🧠 Wnioski

- **TOPSIS** i **SPOTIS** zgodnie wskazują, że **Romet Gazela 4** to najlepszy wybór, a **Merida Crossway 300** wypada najsłabiej.
- **VIKOR** daje zupełnie odwrotny ranking – preferuje **Meridę** jako najlepszą alternatywę, a **Romet** jako najgorszą.
- Rozbieżność wyników wynika z odmiennych sposobów obliczania kompromisów i "odległości" między alternatywami.
- W zależności od tego, jakiego kompromisu oczekujemy, wybór najlepszego roweru może się zmieniać.