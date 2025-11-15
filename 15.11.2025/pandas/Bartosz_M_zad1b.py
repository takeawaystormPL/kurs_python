import pandas as pd;
import matplotlib.pyplot as plt;
df = pd.read_csv("./cisnienie.csv",encoding="utf-8-sig",sep=";");
df2 = pd.DataFrame(df);
srednieSkurczowe = df2.groupby(["Data"])["Skurczowe"].mean();
srednieRozkurczowe = df2.groupby(["Data"])["Rozkurczowe"].mean();
print(pd.concat([srednieSkurczowe,srednieRozkurczowe],axis=1));
print("---------------");
print(f"Data najwiekszego skurczowego:{df2["Data"][df2["Skurczowe"].idxmax()]}");
print(f"Data najwiekszego rozkurczowego:{df2["Data"][df2["Rozkurczowe"].idxmax()]}");
print("----------------");
pogrupowane = df2.groupby(["Data"])
pogrupowane["Skurczowe"].mean().plot(title="Średnie dzienne wartości ciśnienia skurczowego");
pogrupowane["Rozkurczowe"].mean().plot();
plt.show();

