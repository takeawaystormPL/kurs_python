import json;
#zadanie 1
osoby_z_stypendium_naukowym = set();
osoby_z_stypendium_socjalnym = set();
with open("stypendium_naukowe.txt","r",encoding="utf-8") as plik2:
    zawartosc = plik2.read().split("\n");
    osoby_z_stypendium_naukowym = set(zawartosc);
with open("stypendium_socjalne.txt","r",encoding="utf-8") as plik3:
    zawartosc = plik3.read().split("\n");
    osoby_z_stypendium_socjalnym = set(zawartosc);
suma = osoby_z_stypendium_naukowym & osoby_z_stypendium_socjalnym
roznica = osoby_z_stypendium_naukowym - osoby_z_stypendium_socjalnym;
roznica2 = osoby_z_stypendium_socjalnym - osoby_z_stypendium_naukowym;
wszystkie_osoby = osoby_z_stypendium_naukowym|osoby_z_stypendium_socjalnym;

print(f"Osoby biorace jedno i drugie:{len(suma)}");
print(f"Osoby pobierajace tylko stypendium naukowe:{len(roznica)}")
print(f"Osoby pobierajace tylko stypendium socjalne:{len(roznica2)}")
print(f"Osoby pobierajace oboje stypendium:{len(wszystkie_osoby)}");

#zadanie 2

oceny = dict({
    "Bartosz":4.75,
    "Wiktor":5.0
});
oceny.update({"Kacper":5,
              "Wolodia":4.75});
print(dict(sorted(oceny.items(),key=lambda item:item[1])));
with open("uczniowie.txt","w",encoding="utf-8") as plik:
    json.dump(dict(sorted(oceny.items(),key=lambda item:item[1])),plik,indent=4,ensure_ascii=False);

#zadanie 3
dict_eng = {
"kot": "cat",
"pies": "dog",
"szkoła": "school",
"jabłko": "apple",
"książka": "book",
"uczeń":"student"
}
czyKontynuowac = bool(True);
while(czyKontynuowac):
 slowo = str(input("Wprowadź polskie słowo:"));
 if(slowo in dict_eng.keys()):
     print(dict_eng[slowo]);
 else:
     znaczenie = str(input("Nie ma takiego słowa,podaj znaczenie:"));
     dict_eng.update({slowo:znaczenie});
 czyChce = str(input("Czy chcesz kontynuowac(T/N): "));
 if(czyChce.lower() == "n"): czyKontynuowac = False;
print(dict_eng);
#zadanie 4
zdanie = str(input("Wpisz zdanie: ")).split();
przetlumaczoneZdanie = str("");
for slowo in zdanie:
    if(slowo in dict_eng.keys()):
     przetlumaczoneZdanie +=dict_eng[slowo]
    else:
     for i in range(0,len(slowo)): przetlumaczoneZdanie+="?";
    przetlumaczoneZdanie += " ";
print(przetlumaczoneZdanie);
#zadanie 5
wczytanySlownik = dict({});
with open("slownik.json","r",encoding="utf-8") as slownik:
    wczytanySlownik = json.load(slownik);
    czyKontynuowac = bool(True);
while(czyKontynuowac):
 slowo = str(input("Wprowadź polskie słowo:"));
 if(slowo in wczytanySlownik.keys()):
     print(wczytanySlownik[slowo]);
 else:
     znaczenie = str(input("Nie ma takiego słowa,podaj znaczenie:"));
     wczytanySlownik.update({slowo:znaczenie});
 czyChce = str(input("Czy chcesz kontynuowac(T/N): "));
 if(czyChce.lower() == "n"): czyKontynuowac = False;
with open("slownik.json","w",encoding="utf-8") as slownik:
    json.dump(wczytanySlownik,slownik,indent=4,ensure_ascii=False)