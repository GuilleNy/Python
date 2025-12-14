"""
 Pertenencia, longitud y métodos básicos
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
     Comprueba si ciertas claves existen en el diccionario usando in y not in.
     Muestra el número total de elementos usando len().
     Muestra las claves (keys), los valores (values) y los pares (items).
"""


persona = {
        "nombre": "Juana",
        "apellidos": "García",
        "edad": 105,
        "pais": "España",
        "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"], # esto es una lista
        "direccion": {"calle": "Alcala", "numero": 33}} #esto un diccionario 

print("nombre" in persona)
print("España" in persona["pais"])

print(len(persona))

print(persona.keys())

print(persona.values())

print(persona.items())
