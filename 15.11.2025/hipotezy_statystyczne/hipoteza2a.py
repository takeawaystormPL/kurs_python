import numpy as np
from scipy.stats import chi2_contingency

# Tabela kontyngencji: [ [IT, Medycyna, Edukacja], ... ]
table = np.array([
    [12, 10, 8],  # dziewczęta
    [18, 6, 6]    # chłopcy
])

stat, p, dof, expected = chi2_contingency(table)
print(f"Statystyka: {stat}")      # statystyka chi-kwadrat
print(f"P-partośc: {p}")         # p-value
print(f"Stopnie swobody: {dof}")       # stopnie swobody
# Stopnie swobody - przykład:
# Mamy trzy liczby, które muszą razem dawać 100.
# Możemy wybrać dowolnie dwie z nich, ale trzecia nie jest już wolna. Musi dopełnić sumę.
# dwie liczby są wolne,
# trzecia jest zależna,
# stopnie swobody: 2.

# Test chi-kwadrat
# Dla tabeli R x C:
# dof = (liczba wierszy- 1) × (liczba kolumn- 1)
# Czyli dla tabeli 2x3 (płeć x preferencje zawodowe) mamy (2 - 1) × (3 - 1) = 2 stopnie swobody

print(f"Wartości oczekowane: {expected}")  # wartości oczekiwane

print("Statystyka chi-kwadrat:", stat)
print("p-value:", p)
print("Oczekiwane wartości (gdyby wybory były niezależne):")
print(expected)

if p < 0.05:
    print("Wynik istotny. Płeć ma związek z wyborem ścieżki zawodowej.")
else:
    print("Brak podstaw, aby uznać związek między płcią a wyborem.")