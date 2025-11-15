import pandas as pd;
import matplotlib.pyplot as plt;
df1 = pd.read_csv("./cisnienie.csv",encoding="utf-8-sig",sep=";");
df = pd.DataFrame(df1);
srednia1 = df['Skurczowe'].mean();
srednia2 = df['Rozkurczowe'].mean();
print(f"Średnie ciśnienie skurczowe:{srednia1:.2f}");
print(f"Średnie ciśnienie rozkurczowe:{srednia2:.2f}");
maksRozkurczowe = df["Rozkurczowe"].max();
maksSkurczowe =df["Skurczowe"].max();
data1 = str();
data2 = str();
for i in range(0,len(df["Skurczowe"])):
    if(df["Rozkurczowe"][i] == maksRozkurczowe):
        data2 = df["Data"][i];
    if(df["Skurczowe"][i] == maksSkurczowe):
        data1 = df["Data"][i];
print("");
print(f"Maksymalne ciśnienie skurczowe:{maksSkurczowe} data:{data1}");
print(f"Maksymalne ciśnienie skurczowe:{maksRozkurczowe} data:{data2}");
df['roznica'] = df['Skurczowe']-df['Rozkurczowe'];
print("");
print("Dane z różnicą pomiędzy skurczowym a rozkurczowym");
print(df);
df["Data i godzina"] = df["Data"]+" "+df["Godzina"];
df.groupby(df["Data i godzina"])["Skurczowe"].mean().plot(title="Ciśnienie skurczowe i rozkurczowe",marker="o");
df.groupby(["Data i godzina"])["Rozkurczowe"].mean().plot(marker="o");
plt.grid(True);
plt.show();
        
    