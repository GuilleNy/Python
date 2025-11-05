#GUillermo NIEBLA

import random

vidaJugador = 3
puntJugador = 0
nivelJuga = 1

vidaMaquina = 3
puntosMaquina = 0
nivelMaquina = 1




def jugada(jugador_jugad, maquina_jugada, puntuacion, vida):

    if(jugador_jugad > maquina_jugada):
        puntuacion += 1
    elif(maquina_jugada > jugador_jugad):
        vida -= 1

    return puntuacion, vida




ronda = 1

while(vidaJugador > 0):
    
    print(f"Ronda {ronda}")
    print(f"Vidas del jugador: {vidaJugador}")

    for i in range(1, 3):
        print("")
        print(f"Turno {i}")


        if(i == 1):

            print("Elige el tipo de ataque: ")
            print("1. Fuerza")
            print("2. Precision")
            print("3. Riesgo")
            opcion = int(input("Opcion: "))
            print("")
            match(opcion):
                case 1 :
                    fuerza = random.randint(5, 10)
                    defensa = random.randint(3, 10)
                    print("Jugador:")
                    print(f"fuerza: {fuerza}")
                    print("Maquina:")
                    print(f"defensa: {defensa}")
                    print("")

                    puntJugador,vidaJugador = jugada(fuerza, defensa, puntJugador, vidaJugador)

                case 2 :
                    precision = random.randint(3, 8)
                    estable = random.randint(2, 9)
                    print("Jugador:")
                    print(f"precision: {precision}")
                    print("Maquina:")
                    print(f"estable: {estable}")
                    print("")
                    puntJugador,vidaJugador = jugada(precision, estable, puntJugador, vidaJugador)
                case 3 :
                    riesgo = random.randint(1, 10)
                    confunde = random.randint(1, 8)
                    print("Jugador:")
                    print(f"riesgo: {riesgo}")
                    print("Maquina:")
                    print(f"confunde: {confunde}")
                    print("")
                    puntJugador,vidaJugador = jugada(riesgo, confunde, puntJugador, vidaJugador)

            if (puntJugador == 3):
                nivelJuga += 1

        elif(i == 2):
            opcion = random.randint(1, 3)

            match(opcion):
                case 1 :
                    fuerza = random.randint(5, 10)
                    defensa = random.randint(3, 10)
                    print("Maquina:")
                    print(f"fuerza: {fuerza}")
                    print("Jugador:")
                    print(f"defensa: {defensa}")
                    print("")
                    puntosMaquina,vidaMaquina = jugada(fuerza, defensa, puntosMaquina, vidaMaquina)

                case 2 :
                    precision = random.randint(3, 8)
                    estable = random.randint(2, 9)
                    print("Maquina:")
                    print(f"precision: {precision}")
                    print("Jugador:")
                    print(f"estable: {estable}")
                    print("")
                    puntosMaquina,vidaMaquina = jugada(precision, estable, puntosMaquina, vidaMaquina)
                case 3 :
                    riesgo = random.randint(1, 10)
                    confunde = random.randint(1, 8)
                    print("Maquina:")
                    print(f"riesgo: {riesgo}")
                    print("Jugador:")
                    print(f"confunde: {confunde}")
                    print("")
                    puntosMaquina,vidaMaquina = jugada(riesgo, confunde, puntosMaquina, vidaMaquina)
            if (puntosMaquina == 3):
                nivelMaquina += 1
    ronda += 1

else:
    print("")
    print(f"Puntuacion final del jugador es de: {puntJugador}")
    print(f"Con un nivel de: {nivelJuga}")



    


















