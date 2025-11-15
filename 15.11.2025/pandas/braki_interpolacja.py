import pandas as pd;

df = pd.DataFrame({
    "czas":[1,2,3,4,5],
    "temperatura":[20.0,None,22.5,None,25]
})
print("Przed: ");
print(df);

df_interp = df.interpolate()