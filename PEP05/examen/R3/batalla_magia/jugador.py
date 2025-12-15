import random


def ataque_jugador (conocimiento, energia):
    return (conocimiento * energia) * random.randint(1,3)



def mostrar_jugador(nombre, conocimiento, energia):
    print(f"Jugadora: {nombre}")
    print(f"\tConocimiento: {conocimiento} ")
    print(f"\tEnergia: {energia}\n")

