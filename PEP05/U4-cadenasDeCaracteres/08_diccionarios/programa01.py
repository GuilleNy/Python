"""
Escribe un programa en Python que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo
día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
"""

cadena = "Que lindo día que hace hoy"

lista = cadena.lower().split(' ')



# Diccionario que cuenta cuántas veces aparece cada palabra en una lista
diccionario2 = {valor: lista.count(valor) for valor in lista}
print(diccionario2)

#Otra forma de hacerlo
diccionario = {}

for valor in lista:
    diccionario[valor] = lista.count(valor)

print(diccionario)

