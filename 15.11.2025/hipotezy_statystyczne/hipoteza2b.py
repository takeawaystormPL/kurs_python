import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Tabela kontyngencji (płeć x wybór zawodu):
#                IT   Medycyna   Edukacja
# Dziewczęta:    12       10         8
# Chłopcy:       18        6         6

table = np.array([
    [12, 10, 8],   # dziewczęta
    [18, 6, 6]     # chłopcy
])

# Test chi-kwadrat niezależności
stat, p, dof, expected = chi2_contingency(table)

print(f"Statystyka chi-kwadrat: {stat}")
print(f"p-value: {p}")
print(f"Stopnie swobody: {dof}")

print("\nWartości oczekiwane (gdyby nie było związku):")
print(expected)

# Interpretacja wyniku
if p < 0.05:
    print("\nWynik istotny statystycznie: płeć ma związek z wyborem zawodu.")
else:
    print("\nBrak podstaw, aby uznać związek między płcią a wyborem zawodu.")

# -----------------------------
# WYKRES
# -----------------------------

kategorie = ["IT", "Medycyna", "Edukacja"]
dziewczeta = table[0]
chlopcy = table[1]

x = np.arange(len(kategorie))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, dziewczeta, width, label="Dziewczęta")
plt.bar(x + width/2, chlopcy, width, label="Chłopcy")

plt.xlabel("Ścieżka zawodowa")
plt.ylabel("Liczba uczniów")
plt.title("Preferencje zawodowe według płci (fikcyjne dane)")
plt.xticks(x, kategorie)
plt.legend()

plt.tight_layout()
plt.show()