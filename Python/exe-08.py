# Converter medidas

print("-" * 100)
print("- Converter medidas -".center(100))
print("-" * 100)

medida = int(input("Metros: "))

print("-" * 100)

print(f"{medida}m -> {medida / 1000}km")
print(f"{medida}m -> {medida / 100}ham")
print(f"{medida}m -> {medida / 10}dam")

print(f"{medida}m -> {medida * 10}dm")
print(f"{medida}m -> {medida * 100}cm")
print(f"{medida}m -> {medida * 1000}mm")


