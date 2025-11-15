import math
class Triangle:
    def __init__(self,a,b,c):
        self.a = a;
        self.b = b;
        self.c = c;
    def __isCorrect(self):
        if(self.a < 0 or self.b < 0 or self.c < 0):
            return False;
        if((self.a+self.b) <= self.c or (self.a+self.c) <= self.b or (self.b+self.c) <= self.a):
                return False;
        return True;
    def readLengths(self):
        while(True):
         self.a = int(input("Wpisz a:"));
         self.b = int(input("Wpisz b:"));
         self.c = int(input("Wpisz c:"));
         if(self.__isCorrect()):
             break;
         print("Wprowadź poprawnie dane:");
         
    def show(self):
        return f"a:{self.a} b:{self.b} c:{self.c}";
    def triangleSquare(self):
        halfPerimeter = (self.a+self.b+self.c)/2;
        print(halfPerimeter);
        return math.sqrt(halfPerimeter*(halfPerimeter-self.a)*(halfPerimeter - self.b)*(halfPerimeter - self.c));



poleDzialki = float(0);
zIlu = int(input("Podaj ilosc trojkatow: "));
trojkaty = [Triangle(0,0,0) for i in range(zIlu)];
print(trojkaty);
for trojkat in trojkaty:
    trojkat.readLengths();
    poleDzialki += trojkat.triangleSquare()
    print(poleDzialki);
for i in range(len(trojkaty)):
    trojkaty[i].show();
    print(f"Pole trojkata nr {i+1}:{trojkaty[i].triangleSquare():.2f} m2");
print(f"Pole działki wynosi:{poleDzialki:.2f} m2");
