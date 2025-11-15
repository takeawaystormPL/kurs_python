import numpy as np;
import matplotlib.pyplot as plt;

plt.plot()
weights = np.random.randint(40,120,size=20);
values = [];


print(f"Średnia:{np.average(weights)}");
print(f"Wariancja:{np.var(weights)}");
print(f"Odchylenie standardowe:{np.std(weights)}");
plt.xlabel("Masy ciała");
plt.ylabel("Ilość");
plt.title("Masy ciała");
plt.hist(weights,50);
plt.show();

