"""
Escribe un programa en Python que permita crear una lista de palabras y que, a
continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista
"""

numero_palabras = int(input("Cuantas palabras quieres introducir: "))
lista_palabras = []

for i in range(numero_palabras):
    palabra = str(input(f"Introduce la palabra numero {i+1}: "))
    lista_palabras.append(palabra)


print(lista_palabras)

buscar_palabra = str(input("Introduce la palabra a buscar: "))

num_ocurrencias = lista_palabras.count(buscar_palabra)

print(f"La palabra {buscar_palabra} aparece {num_ocurrencias} de veces.")

