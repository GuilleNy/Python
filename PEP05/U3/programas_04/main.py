from matematicas import operaciones, figuras


# Definicion de funciones principales
def menu_opciones():
    print("1.- Operaciones matemáticas")
    print("2.- Cálculo de áreas geométricas")

def mostrar_menu_operaciones():
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")


def opcion1_operaciones():
    print("Sumar")
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(f"La suma es: {operaciones.sumar(num1, num2)}")

def opcion2_operaciones():
    print("Restar")
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(f"La resta es: {operaciones.restar(num1, num2)}")

def opcion3_operaciones():
    print("Multiplicar")
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(f"La multiplicacion es: {operaciones.multiplicar(num1, num2)}")


def opcion4_operaciones():
    print("Dividir")
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    print(f"La division es: {operaciones.dividir(num1, num2)}")



def mostrar_menu_areas ():
    print("1.- Calcular el area de un circulo")
    print("2.- Calcular el area de un triangulo")
    print("3.- Calcular el area de un rectangulo")
    print("4.- Salir")

def opcion1_areas():
    correcto = True
    print("Area del Circulo")
    while correcto:
        radio = int(input("Introduce el radio del circulo: "))
        if radio > 0 :
            area = figuras.calcular_area_circulo(radio)
            print(f"El area del circulo es: {area:.2f}")
            correcto = False
        else:
            print("El radio no puede ser un numero negativo. ")

def opcion2_areas():
    correcto = True
    print("Area del Triangulo")

    while correcto:
        base = int(input("Introduce el valor de la base: "))
        altura = int(input("Introduce el valor de la altura: "))

        if base > 0 and altura > 0:
            area = figuras.calcular_area_triangulo(base, altura)
            print(f"El area del triangulo es: {area}")
            correcto = False
        elif base < 0 or altura < 0:
            print("La base y altura no puede ser un numero negativo. ")
       

def opcion3_areas():
    correcto = True
    print("Área del Rectángulo")
    while correcto:
        base = int(input("Introduce el valor de la base: "))
        altura = int(input("Introduce el valor de la altura: "))

        if base > 0 and altura > 0:
            area = figuras.calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area}")
            correcto = False
        else:
            print("La base y la altura deben ser números positivos. Inténtalo de nuevo.")


# Función principal
"""Función principal del programa"""
def main():
    correcto = True
    while correcto :
        menu_opciones()
        opcion = int(input("Introduce una opcion (1-2): "))
        if opcion >= 1 and opcion <= 2:
            match opcion:
                case 1 :
                    mostrar_menu_operaciones()
                    valido = True
                    while valido:
                        opcion_operaciones = int(input("Introduce una opcion (1-2): "))
                        if opcion_operaciones >= 1 and opcion_operaciones <= 4:
                            match opcion_operaciones:
                                case 1 :
                                    opcion1_operaciones()
                                    valido = False
                                case 2 :
                                    opcion2_operaciones()
                                    valido = False
                                case 3 :
                                    opcion3_operaciones()
                                    valido = False
                                case 4 :
                                    opcion4_operaciones()
                                    valido = False
                                case 5 :
                                    valido = False
                case 2 :
                    mostrar_menu_areas()
                    valido = True
                    while valido:
                        opcion_areas= int(input("Introduce una opcion (1-2): "))
                        if opcion_areas >= 1 and opcion_areas <= 4:
                            match opcion_areas:
                                case 1 :
                                    opcion1_areas()
                                    valido = False
                                case 2 :
                                    opcion2_areas()
                                    valido = False
                                case 3 :
                                    opcion3_areas()
                                    valido = False
                                case 4 :
                                    valido = False
        else:
            print("Opcion incorrecta.")

#Programa principal
if __name__ == "__main__":
    main()