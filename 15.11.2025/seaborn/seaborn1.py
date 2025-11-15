import seaborn as sns
import matplotlib.pyplot as plt

# przykładowy zbiór danych
data = sns.load_dataset("tips")
print(data.head())

sns.scatterplot(x="total_bill", y="tip", data=data)# wykres rozrzutu
plt.title("Rachunek vs napiwek")
plt.show()


sns.barplot(x="day", y="total_bill", data=data)# wykres słupkowy
plt.title("Średni rachunek w poszczególne dni")
plt.show()

sns.histplot(data["total_bill"], bins=20, kde=True) 
# kde=True dodaje krzywą gęstości, bins określa liczbę koszyzyków    
plt.title("Rozkład wartości rachunków")
plt.show()

sns.boxplot(x="day", y="tip", data=data)# wykres pudełkowy
plt.title("Wysokość napiwków w różne dni")
plt.show()

sns.violinplot(x="day", y="tip", data=data)# wykres skrzypcowy
plt.title("Rozkład napiwków (violin plot)")
plt.show()

corr = data.corr(numeric_only=True)# obliczanie macierzy korelacji  
sns.heatmap(corr, annot=True, cmap="coolwarm")# mapa cieplna macierzy korelacji
plt.title("Macierz korelacji")
plt.show()

sns.pairplot(data, hue="sex")# wykresy par zmiennych z podziałem na płeć
plt.suptitle("Wykresy par zmiennych z podziałem na płeć", y=1.02)
plt.show()

sns.set_style("darkgrid")  # inne: white, dark, whitegrid, ticks

sns.scatterplot(x="total_bill", y="tip", data=data, hue="day")
plt.title("Styl darkgrid + kolory wg dnia")
plt.show()