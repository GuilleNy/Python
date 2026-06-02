from random import randint

def ataque_jugador(conocimiento, energia):
    return (conocimiento*energia)*randint(1,3)


def mostrar_jugador(nombre, conocimiento, energia):
    print()
    print(f"Jugadora: {nombre}")
    print(f"Conocimiento: {conocimiento}")
    print(f"Energia: {energia}")
