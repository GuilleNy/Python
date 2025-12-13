"""
 Formato con str.format y f-strings
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
     Declara variables con tu nombre, curso y año.
     Muestra un mensaje con str.format().
     Muestra el mismo mensaje usando f-strings.
     Usa un f-string para mostrar el resultado de una operación matemática con dos
    números.
"""

nombre = "Guillermo"
curso = "2DAW"
anio = 2025


num1 = 34
num2 = 23

print(f"Total suma: {num1 + num2}")

print("Me llamo {} alumno de {} en el año {}.".format(nombre, curso, anio))
print(f"Me llamo {nombre} alumno de {curso} en el año {anio}.")