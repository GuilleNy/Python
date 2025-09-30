#Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print("Introduce el grado Fahrenheit: ")
grado_fh=int(input())

grado_celsius=(((grado_fh - 32) * 5)/ 9)

print(f"Grados Celsius: {grado_celsius:.2f} ºC")