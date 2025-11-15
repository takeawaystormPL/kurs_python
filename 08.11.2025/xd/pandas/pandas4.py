import pandas as pd;

df = pd.read_csv('wyniki.csv',sep=';');
print(df['Pensja']>7800)
print("-----");
print(df[df['Pensja']>7800]);
print("-----");
print(df[(df["Pensja"] < 8000) & (df['Miasto'] == "Rzeszów")]);
print("-----");
age = df['Pensja'] < 8000;
city = df['Miasto'] == "Rzeszów";
print(df[age & city]);