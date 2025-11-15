numbers = [1,2,2,3,4,4,5];
print(f"Lista:{numbers}");
unique = set(numbers);
print(f"Zbiór:{unique}");

#przyklad 2
dodatkowa_matma = {"Ania", "Bartek", "Kasia", "Piotr"}
dodatkowa_fizyka = {"Bartek", "Kasia", "Marek"}

wspolna = dodatkowa_matma & dodatkowa_fizyka
print(f"Częśc wspólna zbiorów - na obydwa przedmity chodzą: {wspolna}")

suma = dodatkowa_matma | dodatkowa_fizyka
print(f"Suma zbiorów - wszyscy razem: {suma}")

roznica1= dodatkowa_matma - dodatkowa_fizyka
print(f"Różnica zbiorów - chodzą na matme, a nie  na fizykę: {roznica1}")

roznica2= dodatkowa_fizyka - dodatkowa_matma
print(f"Różnica zbiorów - chodzą na fizyke, a nie  na matmę: {roznica2}")

roznica_sym= dodatkowa_matma ^ dodatkowa_fizyka
print(f"Różnica symetryczna zbiorów - chodzą albo na matmę albo na fizykę: {suma}")
 
tekst = "Ala ma hipopotama a hipopotam ma innego hipopotama";
unikalne_slowa = set(tekst);
print(tekst);

def anagram (s1,s2):
    return set(s1) == set(s2);
print(anagram("kot","tok"));
print(anagram("pies","siep"));
zdanie = "Kocham programowac w pythonie";
litery = set(zdanie.lower()) - {" ",",","."};
print(litery);
print(f"Liczba liter:{len(litery)}");
znaki_specjalne = set(".,!?;:");
tekst = "Hej! Czemu sie patrzysz?Cos pewnie chcesz";
oczyszczony = "".join(ch for ch in tekst if ch not in znaki_specjalne)
print(oczyszczony);