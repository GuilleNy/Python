#GUILLERMO NIEBLA

from random import choice , randint


def generar_villano():
    nombres = ["Mistica","Magneto", "Catwoman", "Ultron", "Venom"]
    nombre = choice(nombres)

    fuerza = randint(1, 10)
    agilidad = randint(1, 5)
    return nombre, fuerza, agilidad

def poder_villano(fuerza, agilidad):
    return (fuerza*agilidad)*randint(1,3)

def mostrar_villano(nombre, fuerza, agilidad):
    print(f"Villano: {nombre}")
    print(f"Fuerza: {fuerza}")
    print(f"Agilidad: {agilidad}")