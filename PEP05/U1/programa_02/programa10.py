"""
Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita
obtener el número invertido.
"""

print("Introduce un numero de dos cifras: ")
num=int(input())

resto=num % 10
num=round(num / 10)

print(f"{resto}{num}")


