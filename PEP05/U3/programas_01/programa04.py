"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor
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
    correcto = True
    print("Area del Circulo")
    while correcto:
        radio = int(input("Introduce el radio del circulo: "))
        if radio > 0 :
            area = calcular_area_circulo(radio)
            print(f"El area del circulo es: {area:.2f}")
            correcto = False
        else:
            print("El radio no puede ser un numero negativo. ")


    
def opcion2():
    correcto = True
    print("Area del Triangulo")

    while correcto:
        base = int(input("Introduce el valor de la base: "))
        altura = int(input("Introduce el valor de la altura: "))

        if base > 0 and altura > 0:
            area = calcular_area_triangulo(base, altura)
            print(f"El area del triangulo es: {area}")
            correcto = False
        elif base < 0 or altura < 0:
            print("La base y altura no puede ser un numero negativo. ")
       
            
    

def opcion3():
    correcto = True
    print("Area del Rectangulo")

    while correcto:
        base = int(input("Introduce el valor de la base: "))
        altura = int(input("Introduce el valor de la altura: "))

        if base > 0 and altura > 0:
            area = calcular_area_rectangulo(base, altura)
            print(f"El area del triangulo es: {area}")
            correcto = False
        elif base < 0 or altura < 0:
            print("La base y altura no puede ser un numero negativo. ")

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