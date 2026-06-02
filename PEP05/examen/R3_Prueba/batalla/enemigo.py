from random import choice , randint

def generar_enemigo():
    nombres = ["Hydra","Kraken", "Minotauro", "Gorgona", "Titan"]
    nombre = choice(nombres)

    conocimiento = randint(1, 10)
    energia = randint(1, 5)

    return nombre, conocimiento, energia

def ataque_enemigo(conocimiento, energia):
    return (conocimiento*energia)*randint(1, 3)


def mostrar_enemigo(nombre, conocimiento, energia):
    print(f"Enemigo: {nombre}")
    print(f"Conocimiento: {conocimiento}")
    print(f"Energia: {energia}")