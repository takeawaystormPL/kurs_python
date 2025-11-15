import pandas as pd

df = pd.read_csv('wyniki.csv',encoding='utf-8-sig',sep=';');
print(df.head());
print("-----");
print(df.head(3));
print("-----");
print(df.tail());
print("-----");
print(df.tail(2));