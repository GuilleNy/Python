import random

def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titan"]

    nombre = random.choice(nombres)

    conocimiento = random.randint(1,10)
    energia = random.randint(1,5)

    return [nombre, conocimiento, energia]


def ataque_enemigo(conocimiento, energia):
    return (conocimiento * energia) * random.randint(1,3)

def mostrar_enemigo(nombre, conocimiento, energia):
    print(f"Jugadora: {nombre}")
    print(f"\tConocimiento: {conocimiento} ")
    print(f"\tEnergia: {energia}\n")
   
