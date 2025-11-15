import pandas as pd;

df = pd.DataFrame({
    "wiek":[23,None,45,31,None],
    "waga":[70,82,None,65,90]
});
print("Przed czyszczeniem");
print(df);
df_clean = df.dropna();
print(df_clean);