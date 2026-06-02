from batalla.enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo
from batalla.jugador import ataque_jugador, mostrar_jugador

def main():

    print("=== BATALLA DE MAGIA ===")
    print()

    # Pide al jugador
    nombre_Jugador = ""

    while nombre_Jugador == "":
        nombre_Jugador = input("Introduce tu nombre: ").strip()

        if nombre_Jugador == "":
            print("Error: el nombre no puede estar vacío.")

    conocimiento_Jugador = None

    while conocimiento_Jugador is None:
        try:
            valor = int(input("Nivel de conocimiento (1-10): "))

            if 1 <= valor <= 10:
                conocimiento_Jugador = valor
            else:
                print("Error: el conocimiento debe estar entre 1 y 10.")

        except ValueError:
            print("Error: debes introducir un número entero.")

    energia_jugador = None

    while energia_jugador is None:
        try:
            valor = int(input("Energia inicial (1-5): "))

            if 1 <= valor <= 5:
                energia_jugador = valor
            else:
                print("Error: la energía debe estar entre 1 y 5.")

        except ValueError:
            print("Error: debes introducir un número entero.")

    #Genera un enemigo aleatorio
    nombre_enemigo, conocimiento_enemigo, energia_enemigo = generar_enemigo()


    mostrar_jugador(nombre_Jugador, conocimiento_Jugador, energia_jugador)
    print()
    mostrar_enemigo(nombre_enemigo, conocimiento_enemigo, energia_enemigo)
    print()

    #Logica de juego
    for i in range(1,4):
        print(f"---RONDA {i}---")
        magia_jugador = ataque_jugador(conocimiento_Jugador, energia_jugador)
        magia_enemigo = ataque_enemigo(conocimiento_enemigo, energia_enemigo)

        print(f"Magia de {nombre_Jugador}: {magia_jugador}")
        print(f"Magia de {nombre_enemigo}: {magia_enemigo}")

        if magia_jugador > magia_enemigo:
            print(f"{nombre_Jugador} lanza un hechizo poderoso! (-1 energia enemigo)")
            energia_enemigo -= 1
        elif magia_enemigo > magia_jugador:
            print(f"{nombre_enemigo} responde con un conjunto devastador! (-1 energia jugador)")
            energia_jugador -= 1
        else:
            print(f"{nombre_Jugador} y {nombre_enemigo} empatan (no pierden puntos)")
        print()
        
    print("===FIN DEL DUELO===")
    if energia_jugador > energia_enemigo:
        print(f"Energia jugador: {energia_jugador}")
        print(f"Energia enemigo: {energia_enemigo}")
        print(f"¡{nombre_Jugador} ha vencido a {nombre_enemigo}!")
    elif energia_enemigo > energia_jugador:
        print(f"Energia jugador: {energia_jugador}")
        print(f"Energia enemigo: {energia_enemigo}")
        print(f"¡{nombre_enemigo} ha vencido a {nombre_Jugador}!")
    else: 
        print(f"Energia jugador: {energia_jugador}")
        print(f"Energia enemigo: {energia_enemigo}")
        print(f"¡El duelo entre {nombre_Jugador} y {nombre_enemigo} se queda en empate.!")


#Programa principal
if __name__ == "__main__":
    main()


