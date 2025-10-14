"""
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa.
"""

from math import sin, cos, sqrt, pow, radians

print("1. Seno de un ángulo")
print("2. Coseno de ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números.")
opcion = int(input("Introduce una opcion (1-4)"))

match opcion:
    case 1 :
        grado = int(input("Introduce un angulo: "))
        seno = sin(radians(grado))
        print(f"El Seno del angulo {grado} es: {seno}")
    case 2 :
        grado = int(input("Introduce un angulo: "))
        seno = cos(radians(grado))
        print(f"El Coseno del angulo {grado} es: {seno}")   
    case 3 :
        numero = int(input("Introduce un numero: "))
        raiz = sqrt(numero)
        print(f"La raiz cuadrada del numero {numero} es: {raiz}")
    case 4 :
        numero = int(input("Introduce un numero: "))
        exponente = int(input("Introduce el exponente: "))
        result = pow(numero, exponente)
        print(f"La potencia de {numero} elevado a {exponente} es: {result}")
    case _:
        print("Opcion incorrecta.")