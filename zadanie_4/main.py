import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.weights import entropy_weights
from pymcdm.normalizations import minmax_normalization

# Lista alternatyw
bikes = ['Kross Trans 5.0', 'Romet Gazela 4', 'Merida Crossway 300', 'Kellys Phanatic 10']

# Dane: cena, waga, biegi, bagażnik
data = np.array([
    [3199, 17.5, 24, 18],
    [2899, 18.0, 21, 20],
    [3499, 14.8, 27, 12],
    [2999, 16.2, 24, 15]
])

# Typy kryteriów: -1 minimalizuj, 1 maksymalizuj
criteria = [-1, -1, 1, 1]

# Normalizacja i obliczenie wag entropii
normalized = minmax_normalization(data, criteria)
weights = entropy_weights(normalized)

# Utworzenie instancji metod
topsis = TOPSIS()
spotis = SPOTIS([[np.min(data[:, i]), np.max(data[:, i])] for i in range(data.shape[1])])
vikor = VIKOR()

# Obliczenia
results = {
    'TOPSIS': topsis(data, weights, criteria),
    'SPOTIS': spotis(data, weights, criteria),
    'VIKOR': vikor(data, weights, criteria)
}

# DataFrame z wynikami i rankingami
df = pd.DataFrame(results, index=bikes)
for method in results:
    ascending = method == 'SPOTIS'
    df[method + '_rank'] = df[method].rank(ascending=ascending)

print(df.round(4))
