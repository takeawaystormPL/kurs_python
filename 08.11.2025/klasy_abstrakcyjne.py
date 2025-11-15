import os
# Moduł abc zapewnia infrastrukturę do definiowania abstrakcyjnych klas bazowych
from abc import ABC, abstractmethod
# ------------------------------
os.system("cls")

class Animal(ABC):  # bez ABC tez działa
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @abstractmethod  # wymuszenie implementacji tej metody w klasach pochodnych
    def gatunek(self):
        pass

    def write(self):
        print(f"{self.name} to {self.gatunek()}, ma {self.age} lat i waży {self.weight} kg")
# ------------------------------


class Cat(Animal):
    def gatunek(self):
        return "kot"

# ------------------------------


class Dog(Animal):
     def gatunek(self):
        return "pies"


class Hen(Animal):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

    def write(self):
        super().write()
        print(f"{self.name} ma {self.color} kolor\n")

    def gatunek(self):
        return "kura"


# ------------------------------
# Zwierz = Animal("Nie wiadomo jaki Zwierz", 15, 57) Błąd
Mruczek = Cat("Mruczek", 10, 5)
Azor = Dog("Azor", 9, 20)
Kokoszka = Hen("Kokoszka", 2, 3, "czarny")

myAnimals = [Mruczek, Azor, Kokoszka]
for animal in myAnimals:
    animal.write()