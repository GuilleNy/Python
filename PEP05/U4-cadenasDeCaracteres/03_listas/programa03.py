"""
Slicing y reverso
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo del programa anterior.
     Crea una nueva lista extrayendo un slice de los elementos desde el índice 2 hasta
    el índice 5 (recuerda que el índice final es excluido).
     Muestra una nueva lista que contenga solo los elementos de tu lista original que
    estén en posiciones pares, utilizando un incremento de 2 en el slicing.
     Reverso
        ◦ Crear nueva lista en orden inverso utilizando la sintaxis de slicing [::-1].
        ◦ Usa el método reverse() para invertir la lista y modificar su contenido.
"""

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[2:6]) #(recuerda que el índice final es excluido) en este caso se pone el numero 6

print(lista[::2]) #indices pares

print(lista[::-1]) #Crear nueva lista en orden inverso utilizando la sintaxis de slicing [::-1].

lista.reverse() #Usa el método reverse() para invertir la lista y modificar su contenido

print(lista)