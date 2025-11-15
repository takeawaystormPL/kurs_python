text = "Ala ma hipopotama";
print(text[0]);
#nie mozna 
#text[0] = "O"
for i in range ((len(text)-1),-1,-1):
    print(text[i]);
lista = list(text);
print(lista);
#wyświetlanie tekstu pierwszą metodą
lista2 = text.split();
print(lista2);
#rozdzielanie tekstu druga metoda
print(text[4:]);
print(text[:5]);
print(text[-2:]);
#kody ascii
litera = 'A'
kod = ord(litera);
print(f"Kod litery {litera} to {kod}");
#zamienianie ascii na litere
nowa_litera = chr(kod+1)
print(f"Następna litera po {litera} to {nowa_litera}");
#replace
tekst = "Ala lubi bigos i bigos lubi Alę, również Ola lubi bigos i bigos lubi Olę!"
tekst1 = tekst.replace("bigos","schab");
tekst2 = tekst.replace("bigos","schab",1)#zmieni jedno wystapienie
#zamienianie liczby binarnej na dziesietna
liczba_binarna = str(input("Podaj liczbe binarna:"));
wynik = ord(liczba_binarna[0])-48;
for i in range (1,len(liczba_binarna)):
  if(liczba_binarna[i] != '0' and liczba_binarna[i] != '1'):
      print("Niepoprawna liczba");
      exit();
  wynik=wynik*2+(ord(liczba_binarna[i])-48);
print(wynik);