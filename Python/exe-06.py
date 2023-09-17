# Utilizando a biblioteca math para operações

from math import isqrt

print("-" * 100)
print("- Operações matemáticas -".center(100))
print("-" * 100)

number = int(input("Número: "))

print("-" * 100)

print(f"Dobro: {number * 2}")
print(f"Triplo: {number * 3}")
print(f"Raiz Quadrada: {isqrt(number)}")
