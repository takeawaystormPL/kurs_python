import pandas as pd;

df= pd.DataFrame({
    "wiek":[23,None,45,31,None],
    "waga":[70,82,None,65,90]
});
print("Przed: ");
print(df);
df_filled = df.fillna(df.mean(numeric_only=True));
print(df_filled);
