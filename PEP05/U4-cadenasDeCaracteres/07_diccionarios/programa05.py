"""
Recorrido de diccionarios
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
     Crea un diccionario con varios pares clave-valor.
     Recorre las claves con un bucle for.
     Recorre los valores con un bucle for.
     Recorre las claves y valores a la vez usando items()
"""


persona = {
        "nombre": "Juana",
        "apellidos": "García",
        "edad": 105,
        "pais": "España",
        "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"], # esto es una lista
        "direccion": {"calle": "Alcala", "numero": 33}} #esto un diccionario 

# Recorre las claves con un bucle for.
for claves in persona.keys():
    print(claves)

#Recorre los valores con un bucle for.
for valores in persona.values():
    print(valores)

#Recorre las claves y valores a la vez usando items().
for clave , valor in persona.items():
    print(clave, ":", valor)