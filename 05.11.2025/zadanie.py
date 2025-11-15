class Fraction:
    def __init__(self,licznik,mianownik):
        self.__licznik = licznik;
        self.__mianownik = mianownik;
    def reduceFraction(self):
        nwdNumber = Fraction.nwd(self.__mianownik,self.__licznik);
        self.__licznik //= nwdNumber;
        self.__mianownik //=nwdNumber; 
    def getFraction(self):
        return f"{self.__licznik}/{self.__mianownik}";
    def setNumerator(self,licznik):
        try:
          self.__licznik = licznik;  
        except Exception as e:
            return e
    def setDenominator(self,mianownik):
        try:
          if(mianownik == 0):
              raise Exception("Can't have values below 0");
          self.__mianownik = mianownik;  
        except Exception as e:
            print(e);
    def getDenominator(self):
        return self.__mianownik;
    def getNumerator(self):
        return self.__licznik;
    def loadFraction(self):
        try:
         numerator = int(input("Enter numerator: "));
         denominator = int(input("Enter denominator: "));
         if(denominator == 0):raise Exception("Can't have denominator equal to 0");
         self.setDenominator(denominator);
         self.setNumerator(numerator);
        except Exception as e:
            print(e);
            self.loadFraction();
    @staticmethod
    def nwd(a,b):
      if b == 0:
       return a
      return Fraction.nwd(b,a%b);
    @staticmethod 
    def lcm(a,b):
     return (a//Fraction.nwd(a,b))*b;
    def __str__(self):
        return f"{self.__licznik}/{self.__mianownik}";
    @staticmethod
    def addFraction(frac1,frac2):
        newDenominator = Fraction.lcm(frac1.getDenominator(),frac2.getDenominator());
        newFraction = Fraction(1,1);
        try:
            newFraction.setDenominator(newDenominator);
            newFraction.setNumerator(frac1.getNumerator()*(newDenominator//frac1.getDenominator()) + frac2.getNumerator()*(newDenominator//frac2.getDenominator()));
            newFraction.reduceFraction();
            return newFraction;
        except Exception as e:
            print(e);
            exit();
    @staticmethod
    def substractFraction(frac1,frac2):
        newDenominator = Fraction.lcm(frac1.getDenominator(),frac2.getDenominator());
        newFraction = Fraction(1,1);
        try:
            newFraction.setDenominator(newDenominator);
            newFraction.setNumerator(frac1.getNumerator()*(newDenominator//frac1.getDenominator()) - frac2.getNumerator()*(newDenominator//frac2.getDenominator()));
            newFraction.reduceFraction();
            return newFraction;
        except Exception as e:
            print(e);
            exit();
    @staticmethod
    def divideFraction(frac1,frac2):
        newFraction = Fraction(1,1);
        try:
            newDenominator = frac1.getDenominator() * frac2.getNumerator();
            if(newDenominator == 0):raise Exception("Can't have zero denominator")
            newFraction.setDenominator(newDenominator);
            newFraction.setNumerator(frac1.getNumerator() * frac2.getDenominator());
            newFraction.reduceFraction();
            
            return newFraction
        except Exception as e:
            print(e);
            return e;
    @staticmethod    
    def multiplyFraction(frac1,frac2):
        newFraction = Fraction(1,1);
        try:
            newDenominator = frac1.getDenominator() * frac2.getDenominator();
            if(newDenominator == 0):raise Exception("Can't have zero denominator")
            newFraction.setDenominator(newDenominator);
            newFraction.setNumerator(frac1.getNumerator() * frac2.getNumerator());
            newFraction.reduceFraction();
            return newFraction
        except Exception as e:
            print(e);
            return e;
ulamek1 = Fraction(15,6);
ulamek2 = Fraction(20,7);
print("Ulamek 1:");
ulamek1.loadFraction();
print("Ulamek 2:");
ulamek2.loadFraction();
print(f"Addition:{Fraction.addFraction(ulamek1,ulamek2)}");
print(f"Substraction:{Fraction.substractFraction(ulamek1,ulamek2)}");
print(f"Multiplication:{Fraction.multiplyFraction(ulamek1,ulamek2)}");
print(f"Division:{Fraction.divideFraction(ulamek1,ulamek2)}");
