from scipy.stats import chisquare

# Załóżmy, że z ankiety wyszło,że:
# 40 osób wybrało colę, 25 sok, 35 wodę
observed = [40, 25, 35]

# Gdyby wybierali zupełnie losowo, to każdy napój miałby 1/3 udziału
# Oczekiwane liczności:
expected = [sum(observed)/3] * 3
# print(expected)

#test chi-kwadrat
stat, p_value = chisquare(f_obs=observed, f_exp=expected)

print("Statystyka chi-kwadrat:", stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Odrzucamy hipotezę zerową - wybory napojów nie są losowe.")
else:
    print("Brak dowodów na odrzucenie H0 - wygląda jak losowy wybór.")