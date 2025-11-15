class Student:
    #zmienna statyczna
    __count = 0
    def __init__(self,name:str,year:int,isGood):
        self.name = name;
        self.year = year;
        Student.__count+=1;
        self.__isGood = isGood;
        print(f"Uczeń został stworzony");
    def write(self):
        print(f"{self.name} urodzony w roku {self.year}");
    def __str__(self):
        return f"{self.name} urodzony w roku {self.year} jest {self.__isGood}";
    #getters
    def get_name(self):
        return self.name;    
    def get_year(self):
        return self.year;
    def get_isGood(self):
        return self.__isGood;
    #setters
    def set_name(self,name):
        self.name = name;
    def set_year(self,year):
        self.year = year;
    def set_isGood(self,isGood):
        self.__isGood = isGood;
    #destructor
    def __del__(self):
        Student.__count -= 1;
        print(f"Uczeń został skasowany.Ilość uczniów:{Student.__count}");
    @staticmethod
    def showCount():
        print(f"Ilość utworzonych obiektów:{Student.__count}");
student = Student("Witam",2025,False);
student.write();
print(student);
student.name = "Kazio";
student.year = 2025;
student.__isGood = True;
print(student);
print (student.get_isGood());
student.set_isGood(True);
print(student.get_isGood());
student.showCount();
