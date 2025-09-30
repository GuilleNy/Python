"""
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales.
"""


print("Introduce un numero de millas: ")
millas=float(input())

print("Introduce un numero de Km")
km=float(input())

km_a_millas=km / 1.61
millas_a_km=millas * 1.61

print(f"{millas} a Km es {millas_a_km:.2f} km")
print(f"{km} a milla es {km_a_millas:.2f} M")