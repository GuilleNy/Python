"""
Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde.
"""

print("Introduce una cantidad de minutos: ")
minutos=int(input())

hora=minutos // 60 #Utilizamos la división entera para quedarnos con el entero
min= minutos % 60
print(f"Hora: {hora} h y {min} min")