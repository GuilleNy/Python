
import random

"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""




dados_jug_punt = [0,0]

for i in range(2):
    print(f"Jugador {i+1} tira sus dados: ")
    dados_jug_suma=0
    for j in range(2):
        dados_rand = random.randrange(1,7)
        dados_jug_suma += dados_rand
        print(f"Dado {j+1}: {dados_rand}")
        
    dados_jug_punt[i]= dados_jug_suma



if dados_jug_punt[0] > dados_jug_punt[1] :
    print(f"Jugador 1 gana con una puntuacion de {dados_jug_punt[0]}")
elif dados_jug_punt[1] > dados_jug_punt[0] :
    print(f"Jugador 2 gana con una puntuacion de {dados_jug_punt[1]}")
else:
    print("Jugador 1 y Jugador 2 empatan en puntuaciones con: ")
    print(f"Jugador 1: {dados_jug_punt[0]} puntos.")
    print(f"Jugador 2: {dados_jug_punt[1]} puntos.")


