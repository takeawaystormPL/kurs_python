import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Tablica:\n{arr}")
print(f"Kształt tablicy: {arr.shape}")
print(f"Liczba wymiarów tablicy: {arr.ndim} ")
print(f"Liczba wierszy tablicy: {arr.shape[0]} ")
print(f"Liczba kolumn tablicy: {arr.shape[1]} ")
