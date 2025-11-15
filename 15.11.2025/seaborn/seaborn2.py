import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# wczytanie danych z pliku CSV
data = pd.read_csv("dane.csv", sep=';')
print(data)

sns.barplot(x="miasto", y="temperatura", data=data)
plt.title("Średnia temperatura w miastach")
plt.show()

sns.lineplot(x="rok", y="temperatura", hue="miasto", data=data, marker="o")
plt.title("Zmiana temperatury w czasie")
plt.show()
 
 
sns.scatterplot(x="temperatura", y="opady", hue="miasto", data=data, s=100)
plt.title("Zależność między temperaturą a opadami")
plt.show()

sns.boxplot(x="miasto", y="temperatura", data=data)
plt.title("Rozrzut temperatur w różnych miastach")
plt.show()

corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Macierz korelacji")
plt.show()

sns.set_style("whitegrid")
sns.set_palette("Set2")

sns.lineplot(x="rok", y="opady", hue="miasto", data=data, marker="o")
plt.title("Opady roczne w miastach (ładniejszy styl)")
plt.show()
