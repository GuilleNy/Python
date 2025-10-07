"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.
"""
correcto = True

while correcto:
    numero = int(input("Ingresa un numero que este en un rango entre 1 y 10. :"))

    if numero >= 1 and numero <= 10:
        print(f"Correcto. Elegiste el numero {numero}")
        correcto = False
    else:
        print("Numero fuera de rango. Intentalo otra vez.")
