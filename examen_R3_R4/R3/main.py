#GUILLERMO NIEBLA

from liga.heroe import crear_heroe, mostrar_heroe, poder_heroe
from liga.villano import generar_villano, mostrar_villano, poder_villano


def main():
    print("===  LIGA DE SUPERHOMBRES  ===")
    print()

    nombre_jugador = str(input("Introduce tu nombre: ")).strip()
    fuerza_jugador = int(input("Nivel de fuerza (1-10): "))
    agilidad_jugador = int(input("Agilidad inicial (1-5): "))

    crear_heroe(nombre_jugador, fuerza_jugador, agilidad_jugador)
    nombre_villano, fuerza_villano, agilidad_villano = generar_villano()

    mostrar_heroe(nombre_jugador, fuerza_jugador, agilidad_jugador)
    mostrar_villano(nombre_villano, fuerza_villano, agilidad_villano)



    #Logica de juego
    for i in range(1,4):
        print(f"---RONDA {i}---")
        nivelPoder_heroe = poder_heroe(fuerza_jugador, agilidad_jugador)
        nivelPoder_Villano = poder_villano(fuerza_villano, agilidad_villano)

        print(f"Poder de {nombre_jugador}: {nivelPoder_heroe}")
        print(f"Poder de {nombre_villano}: {nivelPoder_Villano}")

        if nivelPoder_heroe > nivelPoder_Villano:
            print(f"{nombre_jugador} lanza un hechizo poderoso! (-1 energia enemigo)")
            agilidad_villano -= 1
        elif nivelPoder_Villano > nivelPoder_heroe:
            print(f"{nombre_villano} responde con un conjunto devastador! (-1 energia jugador)")
            agilidad_jugador -= 1
        else:
            print(f"{nombre_jugador} y {nombre_villano} empatan (no pierden puntos)")
        print()
        
    print("===FIN DEL DUELO===")
    if agilidad_jugador > agilidad_villano:
        print(f"Poder jugador: {agilidad_jugador}")
        print(f"Poder enemigo: {agilidad_villano}")
        print(f"¡{nombre_jugador} ha vencido a {nombre_villano}!")
    elif agilidad_villano > agilidad_jugador:
        print(f"Poder jugador: {agilidad_jugador}")
        print(f"Poder enemigo: {agilidad_villano}")
        print(f"¡{nombre_villano} ha vencido a {nombre_jugador}!")
    else: 
        print(f"Poder jugador: {agilidad_jugador}")
        print(f"Poder enemigo: {agilidad_villano}")
        print(f"¡El duelo entre {nombre_jugador} y {nombre_villano} se queda en empate.!")


#Programa principal
if __name__ == "__main__":
    main()

    