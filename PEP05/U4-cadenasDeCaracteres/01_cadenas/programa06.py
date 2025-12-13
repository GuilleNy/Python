"""
Slicing e iteración
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Crea una cadena "Python".
     Extrae la subcadena "Pyt" con slicing.
     Extrae los caracteres en posiciones pares con slicing ::2.
     Invierte la cadena con slicing [::-1].
     Recorre la cadena carácter por carácter e imprímelos
"""

cadena = "Python"

print(cadena[:3])
print(cadena[::2])
print(cadena[::-1])


for i in cadena:
    print(i)