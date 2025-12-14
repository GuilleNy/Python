"""
Ordenación y manejo de Referencias
Escribe un programa en Python que realice las siguientes operaciones con listas.
     Ordenación Modificable vs. no modificable:
    ◦ Crea una lista de cadenas no ordenadas. Utiliza el método sort() para
    ordenar la lista y comprueba que la lista original ha sido modificada.
    ◦ Utiliza la función sorted() y comprueba que la lista original no se modifica.
     Concatenación
    ◦ Crea dos listas y crea una nueva lista que se la concatenación de las anteriores.
    ◦ Crea dos listas y amplia la primera añadiendo los elementos de las segunda
     Diferencia de copia:
    ◦ Asigna tu lista original a una nueva variable utilizando una asignación directa
    (copia = lista). Muestra los identificadores de memoria de ambas variables
    usando id() para verificar que apuntan al mismo objeto
"""

lista = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'banana']
otraLista = ['moto', 'tractor', 'camion', 'coche', 'bicicleta']

print("Lista original -->", lista)

#Crea una lista de cadenas no ordenadas. Utiliza el método sort() para ordenar la lista y comprueba que la lista original ha sido modificada
lista.sort()
print("Lista ordenada con lista.sort() -->" , lista)

#Utiliza la función sorted() y comprueba que la lista original no se modifica.
lista_ordenada = sorted(otraLista)
print(otraLista)
print("Lista ordenada con sorted() -->", lista_ordenada)

#Crea dos listas y crea una nueva lista que se la concatenación de las anteriores.
lista_concatenada = lista + otraLista
print(lista_concatenada)

#Crea dos listas y amplia la primera añadiendo los elementos de las segunda
lista.extend(otraLista)
print(lista)


#Diferencia de copia
lista_original = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'banana']
#asignación directa
copia = lista_original
print(id(lista_original))
print(id(copia))

#crear otro objeto lista --> lista.copy()
copiaReal = lista_original.copy()
print(id(lista_original))
print(id(copiaReal))