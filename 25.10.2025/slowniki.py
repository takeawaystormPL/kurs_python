import os
os.system('cls')

dict = {
    "Jan": "Jankowski",
    "Piotr":"Piotrowski",
}

print(dict)
print()
for key in dict:
    print(key,end=" ")
print()

for key in dict:
    print(dict[key],end=" ")
print()

for name, surname in dict.items():
    print(f"Imię: {name}, nazwisko:{surname} ",end=" |  ")
print()

dict["Paweł"] = "Pawłowski"
for name, surname in dict.items():
    print(f"Imię: {name}, nazwisko:{surname} ",end=" |  ")
print()

dict.update({"Anna":"Annowska", "Hanna":"Hannowska"})
for name, surname in dict.items():
    print(f"Imię: {name}, nazwisko:{surname} ",end=" |  ")
print()

del dict["Piotr"]
for name, surname in dict.items():
    print(f"Imię: {name}, nazwisko:{surname} ",end=" |  ")
#przykład 2
import os
os.system('cls' if os.name == 'nt' else 'clear')

days = {
    1: "Poniedziałek",
    2: "Wtorek",
    3: "Środa",
    4: "Czwartek",
    5: "Piątek",
    6: "Sobota",
    7: "Niedziela"
}
print(days)
print(days.keys())
print(list(days.keys()))
print(list(days.items()))
print('-------------------')
for key in days:
    print(days[key], end=" ")
print('-------------------')

for day in days.items():
    print(day, end=" ")

print('-------------------')
for key, day in days.items():
    print(day, end=" ")
#przyklad 3
text = "kurs programowania Pythonie"
counter = {}

for litera in text:
    if litera != " ":
        counter[litera] = counter.get(litera, 0) + 1 #get zwraca wartość lub 0 jeśli klucz nie istnieje
        #gdybyśmy użyli counter[litera] += 1 to przy pierwszym wystąpieniu litery byłby błąd bo klucz nie istnieje  

print(counter)

#alternatywnie
for key, value in counter.items():
    print(f"Litera '{key}' występuje {value} razy") 
#przyklad 4 z lambda
operators = {
    "suma": lambda a, b: a + b,
    "roznica": lambda a, b: a - b,
    "iloczyn": lambda a, b: a * b
}

print(operators["suma"](5, 3)) 
print(operators["roznica"](5, 3))
print(operators["iloczyn"](5, 3))