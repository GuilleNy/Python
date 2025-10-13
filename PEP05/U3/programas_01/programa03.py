"""
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
• calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
retorna su área.
• calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
del triangulo y retorna su área.
• calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
del rectángulo y retorna su área.
• mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
• main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
correspondiente en función de la opción seleccionada.
• opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
sea mayor que 0 y una vez que ha validado el radio llamará a la función
calcular_area_circulo.
• opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
a la función calcular_area_triangulo.
• opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
calcular_area_rectangulo.
"""
import math

##########################Funciones############################
def calcular_area_circulo(radio):
    return math.pi * (radio * 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu ():
    print("1.- Calcular el area de un circulo")
    print("2.- Calcular el area de un triangulo")
    print("3.- Calcular el area de un rectangulo")
    print("4.- Salir")

def opcion1():
    print("Area del Circulo")
    radio = int(input("Introduce el radio del circulo: "))

    if radio > 0 :
        area = calcular_area_circulo(radio)
        print(f"El area del circulo es: {area:.2f}")

def opcion2():
    print("Area del Triangulo")
    base = int(input("Introduce el valor de la base: "))
    altura = int(input("Introduce el valor de la altura: "))

    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print(f"El area del triangulo es: {area}")

def opcion3():
    print("Area del Rectangulo")
    base = int(input("Introduce el valor de la base: "))
    altura = int(input("Introduce el valor de la altura: "))

    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print(f"El area del triangulo es: {area}")

def main():
    correcto = True
    while correcto :
        mostrar_menu()
        opcion = int(input("Introduce una opcion (1-4): "))
        if opcion >= 1 and opcion <= 4:
            match opcion:
                case 1 :
                    opcion1()
                case 2 :
                    opcion2()
                case 3 :
                    opcion3()
                case 4 :
                    print("Fin del programa.")
                    correcto = False        
        else:
            print("Opcion incorrecta.")

#Programa principal
main()