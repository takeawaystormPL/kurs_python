import pandas as pd
import os
os.system("cls")

# Dane o sprzedaży
data = {
    'sklep': ['Sklep1', 'Sklep2', 'Sklep1', 'Sklep2', 'Sklep1', 'Sklep3'],
    'produkt': ['Jabłka', 'Jabłka', 'Banany', 'Banany', 'Jabłka', 'Banany'],
    'ilosc_kg': [5, 8, 7, 3, 2, 10],
    'cena_kg': [3, 3.5, 4, 5, 3.2, 6]
}

df = pd.DataFrame(data)

# Grupowanie po sklepie i produkcie i sumowanie całkowitej sprzedaży
df['wartosc_sprzedazy'] = df['ilosc_kg'] * df['cena_kg']
res = df.groupby(['sklep', 'produkt'])['wartosc_sprzedazy'].sum()
print(res)

print('--------------------------------')

df['wartosc_sprzedazy'] = df['ilosc_kg'] * df['cena_kg']
res = df.groupby(['sklep', 'produkt'])['wartosc_sprzedazy'].sum().reset_index()
#reset_index() w pandas służy do przekształcenia indeksów w normalne kolumny i przywrócenia standardowego, liczbowego indeksu
print(res)

