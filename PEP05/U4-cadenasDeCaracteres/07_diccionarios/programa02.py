"""
Acceso a elementos
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
     Define un diccionario con varias claves y valores.
     Accede a algunos valores usando corchetes [] y muestra los resultados.
     Accede a valores usando get() con y sin valor por defecto.
     Intenta acceder a una clave inexistente con get() y observa el resultado
"""

persona = {
        "nombre": "Juana",
        "apellidos": "García",
        "edad": 105,
        "pais": "España",
        "lenguajes": ["JavaScript", "Java", "SQL", "C", "Python"], # esto es una lista
        "direccion": {"calle": "Alcala", "numero": 33}} #esto un diccionario 

print(persona["nombre"])
print(persona["apellidos"])

print(persona.get("edad"))
print(persona.get("lenguajes")[2])
print(persona.get("direccion").get("numero"))

print(persona.get("altura"))