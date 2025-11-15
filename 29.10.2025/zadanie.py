import random
class Book:
    __bookCount = 0;
    def __init__(self,title,author,copies):
        self.__title = title;
        self.__author = author;
        self.__copies = copies * -1 if copies<0 else copies;
        Book.__bookCount += 1;
    def get_title(self):
        return self.__title;
    def get_author(self):
        return self.__author;
    def get_copies(self):
        return self.__copies;
    def set_title(self,title):
        self.__title = title;
    def set_author(self,author):
        self.__author = author;
    def set_copies(self,copies):
        self.__copies = copies *-1 if copies < 0 else copies;
    def show(self):
        return f"Tytuł:{self.get_title()}\n Autor:{self.get_title()}\n {self.get_copies()} egzemplarzy"
    def updateBookInfo(self,title,author,copies):
        if(len(title) > 0 and type(title) == "str"):
            self.set_title(title);
        if(len(author) > 0 and type(author) == "str"):
            self.set_author(author);
        if(type(copies) == "int" and copies > 0):
            self.__copies = copies;
    @staticmethod
    def getBookCount():
        return Book.__bookCount;
books = []
sumaEgzemplarzy = int(0);
for i in range(5):
    ss = random.randint(0,100);
    books.append(Book("Moja","Ja",ss));
    sumaEgzemplarzy += ss;
for i in range(len(books)):
    print(books[i].show());
print(f"Liczba egzemplarzy wszystkich książek:{sumaEgzemplarzy} Ilość książek:{Book.getBookCount()}");