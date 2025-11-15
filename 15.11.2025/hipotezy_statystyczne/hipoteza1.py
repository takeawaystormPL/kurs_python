from scipy import stats

# hipotetyczne dane: wyniki dwóch grup uczniów po różnych metodach nauczania
grupa_a = [65, 70, 68, 72, 71, 69, 75]
grupa_b = [60, 62, 58, 61, 59, 63, 64]

# testujemy hipotezę zerową: "średnie obu grup są takie same"
# test - t-Studenta
statystyka, p_value = stats.ttest_ind(grupa_a, grupa_b)

print("Statystyka t:", statystyka)
print("p-value:", p_value)

if p_value < 0.05:
    print("Odrzucamy hipotezę zerową - grupy różnią się istotnie.")
else:
    print("Brak podstaw do odrzucenia H0 - różnice statystycznie nieistotne.")