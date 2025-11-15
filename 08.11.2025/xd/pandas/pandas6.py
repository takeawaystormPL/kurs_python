import pandas as pd;
import matplotlib.pyplot as plt;
dane = {
    "Godzina":["08:00","12:00","16:00","20:00","23:00"],
    "Skurczowe":[120,130,125,118,135],
    "Rozkurczowe":[80,85,83,78,88]
}   
df = pd.DataFrame(dane);
ax = df.plot(title="Ciśnienie krwi w ciągu dnia",marker="o");
plt.xlabel("Godzina");
plt.ylabel("Ciśnienie");
plt.grid(True);
plt.show();