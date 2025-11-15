import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv('dane_sprzedaz.csv',sep=';');
df.plot();
plt.xlabel("Miesiąc sprzedaży");
plt.ylabel("Zysk");

plt.show();