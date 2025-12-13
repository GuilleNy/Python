"""
Operaciones básicas
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara dos cadenas y únelas con concatenación (+).
     Repite una cadena tres veces con *.
     Compara dos cadenas lexicográficamente e indica cuál es mayor.
     Comprueba si una subcadena pertenece a otra con in.

"""


cadena1 = "Buenos "
cadena2 = "Aias "

cadena3 = cadena1 + cadena2
print(cadena3 * 3 )


if cadena1 > cadena2:
    print("La cadena1 es mayor que la cadena2")
else:
    print("La cadena2 es mayor que la cadena1")


print("n" in cadena1)