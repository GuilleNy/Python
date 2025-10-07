"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random


banca = random.randint(17, 21)
print("La banca ya tiene su jugada.")


num_jugadores = int(input("¿Cuantos jugadores van a jugar?: "))


for i in range(1, num_jugadores + 1):
    print(f" Turno del Jugador {i} ")
    puntuacion_jugador = 0

    while True:
        print(f"Tu puntuacion actual es: {puntuacion_jugador}")
        opcion = input("¿Quieres sacar una carta? s o n: ").lower()

        if opcion == "s":
            carta = random.randint(1, 5)
            puntuacion_jugador += carta
            print(f"Sacaste una carta de valor {carta}.")

            if puntuacion_jugador > 21:
                print(f"Te pasaste de 21 con {puntuacion_jugador}. ¡Has perdido!")
                break

        elif opcion == "n":
            print(f"Tu puntuacion final es {puntuacion_jugador}.")
            print(f"La banca tenia {banca}.")

            if puntuacion_jugador > 21:
                print("Te pasaste de 21. Pierdes.")
            elif puntuacion_jugador > banca:
                print("¡Has ganado a la banca")
            elif puntuacion_jugador == banca:
                print("Empate, la banca gana.")
            else:
                print("Has perdido, la banca gana.")
            break
        else:
            print("Opcion no valida. Escribe 's' o 'n'.")

print(f"La banca tenia {banca}. Fin del juego.")