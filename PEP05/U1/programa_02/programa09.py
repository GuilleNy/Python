"""
Escribe un programa que calcule la calificación de estudiante en un módulo. La
calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3
20%).
"""

print("Introduce la calificacion para RA1: ")
ra_1=float(input())
print("Introduce la calificacion para RA2: ")
ra_2=float(input())
print("Introduce la calificacion para RA3: ")
ra_3=float(input())

ra_1=ra_1 * 0.20
ra_2=ra_2 * 0.60
ra_3=ra_3 * 0.20

calificacion=ra_1 + ra_2 + ra_3

print(ra_1)
print(ra_2)
print(ra_3)


print(f"La calificación total es: {calificacion:.2f}")