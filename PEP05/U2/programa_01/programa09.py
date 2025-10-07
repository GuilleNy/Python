
import random

"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra
"""

print("1. Piedra")
print("2. Papel")
print("3. Tijera")

opcion_jug = int(input("Seleccione una opcion (1, 2 o 3): "))

opcion_maquina = random.randrange(1,4)

opciones = ["Piedra" , "Papel" , "Tijera"]


print(f"Tu elegiste: {opciones[opcion_jug-1]}")
print(f"La maquina eligio: {opciones[opcion_maquina-1]}")


if opcion_jug == opcion_maquina:
    print("Empate.")
elif (opcion_jug == 1 and opcion_maquina == 3) or (opcion_jug == 2 and opcion_maquina == 1) or (opcion_jug == 3 and opcion_maquina == 2):
    print("El usuario a ganado.")
else:
    print("Ha ganado la maquina.")