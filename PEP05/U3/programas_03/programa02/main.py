import moduloOperaciones

# Definición de funciones principales
def main():
    """Función principal del programa"""
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    print(f"La suma es: {moduloOperaciones.sumar(num1, num2)}")
    print(f"La resta es: {moduloOperaciones.restar(num1, num2)}")
    print(f"La multiplicacion es: {moduloOperaciones.multiplicar(num1, num2)}")
    print(f"La division es: {moduloOperaciones.dividir(num1, num2)}")


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()