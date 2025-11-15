import matplotlib.pyplot as plt;
from scipy import stats;
import numpy as np;
def cwiczenie1():
 x = [1,2,3,4,5,6];
 y = [1000,2000,3000,4000,5000,6000];
 plt.plot(x,y);
 plt.xlabel("Lata doświadczenia");
 plt.ylabel("Płaca");
 plt.title("Zależność lat doświadczenia od płacy");
 plt.axhline(0,color='black');
 plt.axvline(0,color='red');
 plt.show();
#cwiczenie1();
def cwiczenie2():
    x = [4000,5000,6000,7000,8000];
    y = [1,2,3,4,5];
    
    plt.scatter(x,y);
    plt.xlabel("Płaca");
    plt.ylabel("Poziom zadowolenia");
    result = stats.linregress(x,y);
    newY = np.array(list(map(lambda el:result.slope * el + result.intercept,x)));
    plt.plot(x,newY);
    plt.show();
    
    n = int(input("Wprowadź wysokość wynagrodzenia:"));
    print(f"Przy {n} zł wynagrodzenia twój poziom zadowolenia powinien wynieść:{result.slope*n+result.intercept}");
cwiczenie2();
def cwiczenie3():
    x = [1000,2000,3000,4000,5000,6000];
    y = [1,2,3,4,5,6];
    plt.scatter(x,y);
    
    result = stats.linregress(x,y);
    newY = np.array(list(map(lambda s:result.slope*s+result.intercept,x)));
    plt.plot(x,newY);
    plt.show();
cwiczenie3();