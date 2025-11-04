# programa02.py
# Pide un número entre 1 y 10 y muestra una lista del 1 al número indicado

correcto = True

while correcto:
    try:
        numero = int(input("Introduce un número entre 1 y 10: "))

        if 1 <= numero <= 10:
            print("Lista de números:")
            for i in range(1, numero + 1):
                print(i, end=" ")
            print()  # salto de línea al final
            correcto = False
        else:
            print("El número debe estar entre 1 y 10.")
    except ValueError:
        print("Debes introducir un número entero.")