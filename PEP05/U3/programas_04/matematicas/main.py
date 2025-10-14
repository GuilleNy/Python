import conversiones
import figuras
import operaciones

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
    print("Area del Circulo")
    radio = int(input("Introduce el radio del circulo: "))

    if radio > 0 :
        area = figuras.calcular_area_circulo(radio)
        print(f"El area del circulo es: {area:.2f}")

def opcion2_areas():
    print("Area del Triangulo")
    base = int(input("Introduce el valor de la base: "))
    altura = int(input("Introduce el valor de la altura: "))

    if base > 0 and altura > 0:
        area = figuras.calcular_area_triangulo(base, altura)
        print(f"El area del triangulo es: {area}")

def opcion3_areas():
    print("Area del Rectangulo")
    base = int(input("Introduce el valor de la base: "))
    altura = int(input("Introduce el valor de la altura: "))

    if base > 0 and altura > 0:
        area = figuras.calcular_area_rectangulo(base, altura)
        print(f"El area del triangulo es: {area}")

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
main()