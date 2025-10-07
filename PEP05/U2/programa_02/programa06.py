"""
Escribe un programa que realice las siguientes operaciones:
• Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
• Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
• Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""


correcto = True

while correcto:
    numero = int(input("Ingresa un numero que este en un rango entre 1 y 10. :"))

    if numero >= 1 and numero <= 10:
        print(f"Correcto. Elegiste el numero {numero}")
        for i in range(1,13):
            print(f"{numero} x {i} = {numero * i}")


        if correcto:
            opcion = int(input("Deseas continuar con otro numero?. Selecciona 1 para continuar o 2 para salir: "))
            if opcion == 1 :
                correcto = True
            else:
                correcto = False
    else:
        print("Numero fuera de rango. Intentalo otra vez.")
