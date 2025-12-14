"""
Añadir y modificar elementos
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
     Crea un diccionario con algunos datos básicos.
     Añade nuevas claves y valores.
     Modifica un valor existente.
     Muestra el diccionario antes y después de los cambios
"""

persona = {
        "nombre": "Juana",
        "apellidos": "García",
        "edad": 105,
        "pais": "España",
        "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"], # esto es una lista
        "direccion": {"calle": "Alcala", "numero": 33}} #esto un diccionario 

print(persona)

persona["altura"] = 1.60
persona["peso"] = 56

print(persona.values())

persona["pais"] = "Ecuador"

print(persona.values())