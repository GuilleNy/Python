#GUILLERMO NIEBLA

from random import randint


def crear_heroe(nombre, fuerza, agilidad):
    try:
        

        if not 1 <= fuerza <= 10:
            print("Error: La fuerza debe estar entre 1 y 10.")

            
        if not 1 <= agilidad <= 5:
            print("Error: la agilidad debe estar entre 1 y 5.")

                
    except ValueError:
        print("Error: debes introducir un número entero.")



def poder_heroe(fuerza, agilidad):
    return (fuerza*agilidad)*randint(1,3)


def mostrar_heroe(nombre, fuerza, agilidad):
    print()
    print(f"Heroe: {nombre}")
    print(f"Fuerza: {fuerza}")
    print(f"Agilidad: {agilidad}")


