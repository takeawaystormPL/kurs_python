class Zwierze:
    def __init__(self,name,age,weight):
        self.name = name;
        self.age = age;
        self.weight = weight;
        
    def write(self):
        print(f"{self.name} ma {self.age} lat i waży {self.weight} kg");
class Kot(Zwierze):
    pass
class Pies(Zwierze):
    pass
Zwierz = Zwierze("Pyrdek",69,67);
Zwierz.write();

class Pracownik:
    def __init__(self,name,salary):
        self._name = name;
        self._salary = salary;
    def write(self):
        print(f"{self._name}-{self._salary}");
    def __str__(self):
        return f"{self._name}-{self._salary}";
class Mechanik(Pracownik):
    def __init__(self,name,salary,whichCars):
        super().__init__(name,salary);
        self._whichCars = whichCars;
    def write(self):
        print(f"{self._name}-{self._salary}-{self._whichCars}");
    def __str__(self):
        return f"{self._name}-{self._salary}-{self._whichCars}";
class Programista(Pracownik):
    def __init__(self,name,salary,programmingLanguage):
        super().__init__(name,salary);
        self._programmingLanguage = programmingLanguage;
    def write(self):
        print(f"{self._name}-{self._salary}-{self._programmingLanguage}");
    def __str__(self):
        return f"{self._name}-{self._salary}-{self._programmingLanguage}";
pracownik1 = Mechanik("Bartosz",0,"BMW");
pracownik2 = Programista("Bartosz",10000,"Python");
pracownik3 = Pracownik("Ktos",1000000);
lista = [pracownik1,pracownik2,pracownik3];
for el in lista:
    el.write();
print(f"{pracownik1} jest mechanikiem:{isinstance(pracownik1,Mechanik)}");
pracownik1.write();
    