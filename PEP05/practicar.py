diccionario = {"telefono"  : "603145785",
               "direccion" : {"calle" : "Alcala", "numero" : 33},
               "lenguaje" : ["Python", "Java", "SQL"],
               "vocales" : {"a", "e", "i", "o", "o"}}


conjunto = {"AWS", "Docker", "Linux", "Linux"}


for conj in conjunto:
    print(conj)

tupla = ("aws", "python", "java")
lista = ["manzana", "pera", "naranja"]


inventario = {}

diccionario["numeros"] = (1, 2, 3, 4)


for clave , valor in diccionario.items():
    print(clave, ":", valor)

print()

diccionario.pop("numeros")

print(diccionario.values())