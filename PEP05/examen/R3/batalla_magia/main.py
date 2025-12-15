from enemigo import generar_enemigo, ataque_enemigo, mostrar_enemigo
from jugador import ataque_jugador, mostrar_jugador


def main():
    print("===  BATALLA DE MAGIA  ===\n")

    #Jugador
    nombre = str(input("Introduce tu nombre: "))
    conocimiento = int(input("Nivel de conocimiento (1-10): "))
    energia = int(input("Energia inicial (1-5):"))
    
    print()
    mostrar_jugador(nombre, conocimiento, energia)
    
    #Enemigo
    enemigo = generar_enemigo()
    nombre_enem = enemigo[0]
    conocimiento_enem = enemigo[1]
    energia_enem = enemigo[2]
    
    print()
    mostrar_enemigo(nombre_enem , conocimiento_enem, energia_enem)


    for i in range(1,4):
        print(f"--- RONDA {i} ---\n")
        ataque_jug = ataque_jugador(conocimiento,energia)
        ataque_enem = ataque_enemigo(conocimiento_enem, energia_enem )

        print(f"Magia de {nombre}: {ataque_jug}")
        print(f"Magia de {nombre_enem}: {ataque_enem}")

        if i % 2 == 1:
            energia_enem -= 1
            print(energia_enem)
            print(f"{nombre} lanza un hechizo poderoso! (-1 energia enemigo)")
        else:
            energia -= 1
            print(energia)
            print(f"{nombre_enem} responde con un conjunto devastador! (-1 energia enemigo)")

        
    print("=== FIN DEL DUELO ===\n")
    if energia > energia_enem:
        print(f"{nombre} ha vencido a {nombre_enem}")
    
    if energia_enem > energia:
        print(f"{nombre_enem} ha vencido a {nombre}")

    if energia == energia_enem:
        print(f"Hay empate entre {nombre} y {nombre_enem}")

    

   























#Programa principal
if __name__ == "__main__":
    main()