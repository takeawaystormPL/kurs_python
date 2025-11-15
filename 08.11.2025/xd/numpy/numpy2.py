import numpy as np;

arr1 = np.random.randint(1,10,size=20);
print(f"Tablica całkowita:{arr1}");
count = np.bincount(arr1);
print(f"Wystapienia:{count}");
for i in range(1,len(count)):
    print(f"Liczba {i} wystepuje:{count[i]} razy");
print("Losowania liczb z (0,1>):");
arr2 = np.random.random(10);
print(arr2);