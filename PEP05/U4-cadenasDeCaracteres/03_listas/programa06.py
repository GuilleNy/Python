"""
Listas y cadenas
Escribe un programa en Python que realice las siguientes operaciones con listas:
     Crea un cadena de caracteres con varias palabras y a partir de ella crear una lista
    que contenga como elementos las palabras de la cadena.
        ◦ Usa la método split().
        ◦ Usa método partition()
     Crea lista que contenga como elementos varias palabras y partir de ella crear una
    cadena de caracteres que contenga las palabras separadas por guiones.
"""

cadena = "mango,piña,manzana,lemon,banana"

lista1 = cadena.split(',')
lista2 = list(cadena.partition(','))

print(lista1)
print(lista2)

#Crea lista que contenga como elementos varias palabras y partir de ella crear una
#cadena de caracteres que contenga las palabras separadas por guiones.
lista3 = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'banana']

cadena_lista = '-'.join(lista3)
print(cadena_lista)