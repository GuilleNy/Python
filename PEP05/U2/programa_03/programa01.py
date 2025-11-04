# programa01.py
# Pide un número entre 1 y 10 y controla errores de entrada

correcto = True

while correcto:
    try:
        numero = int(input("Introduce un numero entre 1 y 10: "))

        if 1 <= numero <= 10:
            print(f"Numero correcto: {numero}")
            correcto = False
        else:
            print("El numero debe estar entre 1 y 10.")
    except ValueError:
        print("Debes introducir un numero entero.")


"""
ZeroDivisionError: Se produce con cualquier operación (/, // o %) que intente dividir
por 0.
ValueError: Generalmente se produce cuando alguna función de conversión como
int() o float() reciben valores que no pueden convertir.
TypeError: Se produce cuando usas un dato de un tipo que no es el adecuado. Por
ejemplo, los índices de las listas tienen que ser enteros.
Exception: sirve para cualquier tipo de excepción.
"""