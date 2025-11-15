import numpy as np;
import matplotlib.pyplot as plt;

weights = np.random.uniform(60.0,100.0,10000);
print(f"Średnia waga {np.average(weights)}");
print(f"Wariancja {np.var(weights)}");
print(f"Odchylenie standardowe {np.std(weights)}");

plt.xlabel("Waga");
plt.ylabel("Ilość");
plt.hist(weights,50);
plt.show();