import csv

with open("dane.csv", "r", encoding="utf-8-sig") as plik:
    reader = csv.reader(plik)
    for wiersz in reader:
        print(wiersz)
