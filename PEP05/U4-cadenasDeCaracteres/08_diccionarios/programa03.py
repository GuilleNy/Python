"""
Escribe un programa en Python que cumpla los siguientes requisitos.
     Crea un diccionario llamado 'agenda' donde las claves sean nombres de personas
    y los valores sus números de teléfono.
     Permite añadir, modificar y eliminar contactos.
     Muestra la agenda completa de forma ordenada (por nombre).
     Implementa la búsqueda de un contacto mostrando su número o un mensaje si no
    existe
"""
agenda = {
    "Ana": "123456789",
    "Juan": "987654321",
    "Luis": "555555555"
}

nombre = str(input("Introduce el nombre: "))
telefono = int(input("Introduce el numero de telefono: "))

#Añadir
while nombre != "" :
    agenda[nombre] = telefono
    nombre = str(input("Introduce el nombre: "))
    if nombre != "":
        numero = int(input("Introduce el numero de telefono: "))
    
print(agenda)

#Modificar
nombre_modificar = str(input("Introduce el nombre para modificar el numero: "))
nuevo_numero = int(input("Introduce el nuevo telefono: "))

agenda[nombre_modificar] = nuevo_numero
print(agenda)

#Eliminar
nombre_eliminar = str(input("Introduce el nombre para eliminar el numero: "))
del agenda[nombre_eliminar]
print(agenda)

#Muestra la agenda completa de forma ordenada (por nombre).Ordenar por nombre(clave)

agenda_ordenada = dict(sorted(agenda.items()))

print(agenda_ordenada)

#Implementa la búsqueda de un contacto mostrando su número o un mensaje si no existe
nombre_buscar = str(input("Introduce el nombre para buscar el numero: "))

if nombre_buscar in agenda:
    print(agenda[nombre_buscar])
else:
    print("No se encontro el contacto.")