"""
Eliminación y búsqueda
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo del programa anterior.
     Elimina el cuarto elemento de la lista utilizando la instrucción del.
     Elimina un elemento de la lista utilizando el método remove().
     Verifica si un un elemento pertenece a la lista.
     Muestra por pantalla el índice de un elemento de la lista.
     Muestra por pantalla el número de ocurrencias de un elemento en la lista.
"""

lista = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'banana']

del lista[3]

print(lista)

lista.remove('orange')

print(lista)

if 'orange' in lista:
    print("Si, orange esta en la lista.")
else:
    print("No, orange no esta en la lista.")


print(lista.index('kiwi'))

print(lista.count('banana'))