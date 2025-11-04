"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos
"""
import random

correcto = True
cont = 0

num_rand = random.randrange(1, 21)

while correcto:
    numero = int(input("Adivina el numero. Ingresa un numero: "))
    

    if numero == num_rand:
        print(f"Correcto. Adivinaste el numero {numero}")
        correcto = False
    else:
        if numero > num_rand:
            print(f"El numero a adivinar es menor que {numero}")
        else:
            print(f"El numero a adivinar es mayor que {numero}")
        cont = cont + 1

    if cont >= 3:
        print("Lo siento. Solo tienes 3 intentos.")
        print(f"El numero era {num_rand}.")
        correcto = False



    

#otra forma
"""

numeroMaquina = random.randrange(1,21)
#numeroMaquina = 20

correcto = True
intento = 3

while correcto :
    numeroJugad=int(input("Introduce el numero a adivinar: "))

    if(numeroJugad == numeroMaquina):
        print("Has adivinado!!!")
        correcto = False
    else:
        if(numeroJugad < numeroMaquina):
            print("EL numero a adivinar es mayor al numero introducido.")
        else:
            print("EL numero a adivinar es menor al numero introducido.")
        
        intento -= 1
        print(f"Te quedan {intento} intentos.")
        

    if(intento == 0):
        print("Has agotado todos los intentos")
        print(f"EL numero era {numeroMaquina}")
        correcto = False
    

"""
