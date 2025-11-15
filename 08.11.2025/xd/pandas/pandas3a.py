import pandas as pd;

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv";
df = pd.read_csv(url);

print(df);
print(df.describe());