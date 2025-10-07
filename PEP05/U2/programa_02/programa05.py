"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto
"""

correcto = True

while correcto:
    numero = int(input("Ingresa un numero que este en un rango entre 1 y 10. :"))

    if numero >= 1 and numero <= 10:
        print(f"Correcto. Elegiste el numero {numero}")
        for i in range(numero):
            print(i+1, end=" ")
        correcto = False
    else:
        print("Numero fuera de rango. Intentalo otra vez.")
