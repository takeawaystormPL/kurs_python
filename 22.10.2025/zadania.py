#Zadanie 8: Generator akrostychów Napisz program, który: Wczyta zdanie od użytkownika. Wygeneruje akrostych, używając pierwszych liter każdego słowa. Sprawdza, czy użytkownik podał jakikolwiek tekst – w przeciwnym razie wyświetli komunikato błędzie.Przykład: Wejście: „Lubię codziennie chodzić do szkoły” Wyjście: „Lccds”
def generatorAkrostychow():
    tekst = str("Ala ma krokodyla");
    pierwszeLitery = str("");
    if(len(tekst) == 0):
        print("Za mały tekst");
        exit();
    for i in range(0,len(tekst)):
        if(i == 0): pierwszeLitery += tekst[i];
        if(tekst[i] == " " and i+1 < len(tekst)):
            pierwszeLitery += tekst[i+1];
    print(pierwszeLitery); 
generatorAkrostychow();
def odwracanieSlow():
    zdanie = str(input("Wprowadz tekst:"));
    rozdzieloneZdanie = str.split(zdanie," ");
    for el in rozdzieloneZdanie:
        print(el[::-1],end=" ");
        
    
odwracanieSlow();  
