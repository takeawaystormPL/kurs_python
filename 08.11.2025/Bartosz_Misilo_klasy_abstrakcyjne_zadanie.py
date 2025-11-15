from abc import ABC,abstractmethod

class Pracownik(ABC):
    def __init__(self,imie):
        self.imie = imie;
    def pokaz_dane(self):
        print(f"{self.imie}");
    @abstractmethod
    def oblicz_wynagrodzenie(self):
        pass
class Etatowy(Pracownik):
    def __init__(self,imie,pensja):
        super().__init__(imie);
        self.pensja = pensja;
    def pokaz_dane(self):
        print(f"{self.imie}:{self.oblicz_wynagrodzenie()}");
    def oblicz_wynagrodzenie(self):
        return self.pensja;
class Zleceniowy(Pracownik):
    def __init__(self,imie,stawka_godzinowa,liczba_godzin):
        super().__init__(imie);
        self.stawka_godzinowa = stawka_godzinowa;
        self.liczba_godzin = liczba_godzin;
    def oblicz_wynagrodzenie(self):
        return self.stawka_godzinowa * self.liczba_godzin;
    def pokaz_dane(self):
        print(f"{self.imie}:{self.oblicz_wynagrodzenie()}");
class Freelancer(Pracownik):
    def __init__(self,imie,kwota_za_projekt):
        super().__init__(imie);
        self.kwota_za_projekt = kwota_za_projekt;
    def pokaz_dane(self):
        print(f"{self.imie}:{self.oblicz_wynagrodzenie()}");
    def oblicz_wynagrodzenie(self):
        return self.kwota_za_projekt;
lista = [Etatowy("Bartosz",10000),Zleceniowy("Bartosz",40,160),Freelancer("Bartosz",500)];
for pracownik in lista:
    pracownik.pokaz_dane();
