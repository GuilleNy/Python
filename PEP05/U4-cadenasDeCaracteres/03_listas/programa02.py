"""
 Mutabilidad y manipulación simple
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo el programa anterior:
     Partiendo de mi_listaXX del ejercicio anterior modifica el valor del tercer elemento a
    un nuevo valor de tu elección.
     Añade un nuevo elemento al final de la lista utilizando el método append().
     Inserta una nueva cadena de caracteres en la segunda posición de la lista (índice 1) utilizando el método insert().
     Recorre la lista y muestra sus elementos por pantalla
"""

mi_lista = [34, "Hola", "Manzana", 23.5]


mi_lista.append("Mango")
print(mi_lista)

mi_lista.insert(1, "Kiwi")
print(mi_lista)

for i, valor in enumerate(mi_lista):
    print(f"Indice {i}: {valor}" )