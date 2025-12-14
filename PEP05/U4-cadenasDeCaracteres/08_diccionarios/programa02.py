"""
Escribe un programa en Python que cumpla los siguientes requisitos.
     El programa calculará la media de notas de alumnos/as.
     El programa irá pidiendo nombres de alumnos y su calificación
     Los nombres son ingresados en cualquier orden.
     Si un alumno tiene varias notas se pedirá varias veces su nombre y su calificación.
     Cuando se introduzca un nombre vacío se dejaran de pedir datos y se mostrara los
    nombre de los alumnos y el promedio de la calificación de cada uno.
    Los alumnos se gestionarán con un diccionario (la clave es el nombre) y las calificaciones
    el valor (que debe ser una tupla).
"""


calificaciones = {}

nombre = str(input("Introduzca el nombre del alumno: "))

while nombre != "":
    notas = []
    for i in range(4):
        nota = int(input("Introduzca la nota: "))
        notas.append(nota)

    calificaciones[nombre] = tuple(notas)
    nombre = str(input("Introduzca el nombre del alumno: "))

print(calificaciones)

for clave , valor in calificaciones.items():
    media = sum(valor) / len(valor)
    print(f"La media del alumno {clave} es : {media}")

   

