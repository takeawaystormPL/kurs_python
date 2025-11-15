import matplotlib.pyplot as plt;
import os;

a = int(input("Podaj a:"));
b = int(input("Podaj b:"));
x = range(-10,11);

y = [];
j = 0;
for i in x:
    y.append(a*i*b);
    print(f'f({i}) = {y[j]}');
    j+=1;
plt.plot(x,y);
plt.title(f'Wykres f(x) = {a}x + b');
plt.grid(True);
plt.axis('equal');
plt.axhline(0,color='black');
plt.axvline(0,color='black');
plt.show();
