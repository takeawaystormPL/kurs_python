import csv

dane = [
    ["Imię", "Nazwisko", "Wiek"],
    ["Jan", "Kowalski", 30],
    ["Anna", "Nowak", 25],
    ["Piotr", "Zieliński", 40]
]

with open("plik_csv.csv","w",encoding="utf-8-sig") as plik_csv:
    writer = csv.writer(plik_csv);
    writer.writerows(dane);
