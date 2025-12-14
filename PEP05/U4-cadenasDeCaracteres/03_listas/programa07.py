"""
Funciones matemáticas
Escribe un programa en Python que realice las siguientes operaciones con listas.
     Crea una lista solo de números (ejemplo: temperaturas =).
     Calcula la suma de todos los elementos utilizando la función sum() y la media
    (promedio) combinando sum() y len().
     Muestra los valores máximo y mínimo de la lista
"""

temperaturas = [34,56,3,7,36]

print(sum(temperaturas))

media = sum(temperaturas) / len(temperaturas)
print(media)

print(max(temperaturas))
print(min(temperaturas))