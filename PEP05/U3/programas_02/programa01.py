"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""

import math

print("1. Seno de un ángulo")
print("2. Coseno de ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números.")
opcion = int(input("Introduce una opcion (1-4)"))

match opcion:
    case 1 :
        grado = int(input("Introduce un angulo: "))
        seno = math.sin(math.radians(grado))
        print(f"El Seno del angulo {grado} es: {seno}")
    case 2 :
        grado = int(input("Introduce un angulo: "))
        seno = math.cos(math.radians(grado))
        print(f"El Coseno del angulo {grado} es: {seno}")   
    case 3 :
        numero = int(input("Introduce un numero: "))
        raiz = math.sqrt(numero)
        print(f"La raiz cuadrada del numero {numero} es: {raiz}")
    case 4 :
        numero = int(input("Introduce un numero: "))
        exponente = int(input("Introduce el exponente: "))
        result = math.pow(numero, exponente)
        print(f"La potencia de {numero} elevado a {exponente} es: {result}")
    case _:
        print("Opcion incorrecta.")