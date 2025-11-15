from stat_funcitons import avg, weightedAvg, median, variance, stddev, mode;
data = [189, 170, 189, 183, 178, 185, 180, 170, 181, 186]
print(f"Średnia: {avg(data)}")
print(f"Mediana: {median(data)}")
print(f"Wariancja: {variance(data)}")
print(f"Odchylenie standardowe: {stddev(data):.2f}")
print(f"Dominanta: {mode(data)}")
dataW = [[189, 170, 189, 183, 178], [0.2, 0.1, 0.3, 0.15, 0.25]]
print(f"Średnia ważona: {weightedAvg(dataW)}")
print("--------------------------------");
data = [189, 170, 189, 189, 170, 189, 189, 170, 170, 170]
print(f"Średnia: {avg(data)}")
print(f"Mediana: {median(data)}")
print(f"Wariancja: {variance(data)}")
print(f"Odchylenie standardowe: {stddev(data):.2f}")
print(f"Dominanta: {mode(data)}")
dataW = [[189, 170, 189, 183, 178], [0.2, 0.1]]
print(f"Średnia ważona: {weightedAvg(dataW)}")