"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana
"""

import random


banca = random.randint(17, 21)
print("La banca ya tiene su jugada.")

puntuacion_jugador = 0

while True:
    print(f"\nTu puntuacion actual es: {puntuacion_jugador}")
    opcion = input("¿Quieres sacar una carta? s o n: ").lower()
    
    if opcion == "s":
        carta = random.randint(1, 5)
        puntuacion_jugador += carta
        print(f"Sacaste una carta de valor {carta}.")
        
        if puntuacion_jugador > 21:
            print(f" Te pasaste de 21 con {puntuacion_jugador}. ¡Has perdido")
            break
    elif opcion == "n":
        print(f"\nTu puntuacion final es {puntuacion_jugador}.")
        print(f"La banca tenía {banca}.")
        
        if puntuacion_jugador > 21:
            print(" Te pasaste de 21. Pierdes.")
        elif puntuacion_jugador > banca:
            print("¡Has ganado")
        elif puntuacion_jugador == banca:
            print("Empate, la banca gana.")
        else:
            print("Has perdido, la banca gana.")
        break
    else:
        print("Opción no valida. Escribe 's' o 'n'.")