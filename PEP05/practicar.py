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


#for clave , valor in diccionario.items():
#    print(clave, ":", valor)

print()

diccionario.pop("numeros")

#print(diccionario.values())


inventario2 = {}

def agregar_productos(codigo, inventario2 , nombre, precio):

    if codigo not in inventario2:
        inventario2[codigo] = (nombre, [precio])

def añadir_productos(codigo, inventario2, precio_nuevo):

    if codigo in inventario2:
        inventario2[codigo][1].append(precio_nuevo)


agregar_productos("P001", inventario2, "Teclado", 30000)
añadir_productos("P001", inventario2, 2500)


#print(inventario2)


inventario = {
    "P001": ("Portátil", [1200, 1250, 1300]),
    "P002": ("Ratón", [25, 30]),
    "P003": ("Teclado", [50]),
    "P004": ("Monitor", [200, 220, 240])
}

print(inventario["P001"][0]) 
print(inventario["P004"][1][-1])
print(inventario["P001"][1][0])
print()
#Recorre el inventario y muestra solo los nombres.
for nombre in inventario.values():
    print(nombre[0])

#Muestra código y nombre de cada producto.
for codigo, valor in inventario.items():
    print(codigo , ": ", valor[0])

#Muestra el último precio de cada producto.
for valor in inventario.values():
    print(valor[0], ": ", valor[1][-1])

#Añade un nuevo precio de 1350 al producto "P001".
inventario["P001"][1].append(1350)
print(inventario["P001"])
print()

#Recorre todo el inventario mostrando:
for codigo, valor in inventario.items():
    print(f"Codigo: {codigo}")
    print(f"Nombre: {valor[0]}")
    print(f"Historial: {valor[1]}")
    print()

print()