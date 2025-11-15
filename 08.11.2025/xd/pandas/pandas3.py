import pandas as pd;

df = pd.read_csv('wyniki.csv',sep=';');

print(df);
print(df.describe());
print("-----");