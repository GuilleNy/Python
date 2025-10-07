"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""


print("Sin Break")
correctoA = True
sumaA = 0
contA = 0
while correctoA:
    numero = int(input("Ingresa un numero: "))
    if numero != 0:
        contA = contA + 1
        sumaA +=  numero
    else:
        correctoA = False

if contA > 0:
    mediaA = sumaA / contA 
    print(f"La suma de todos los numeros introducidos es: {sumaA}")
    print(f"La media de todos los numeros introducidos es: {mediaA:.2f}")
else:
    print("Introduce un numero al menos.")


print("Con Break")

correctoB = True
sumaB = 0
contB = 0
while correctoB:
    numero = int(input("Ingresa un numero: "))
    if numero == 0:
        break

    sumaB +=  numero
    contB = contB + 1

if contB > 0:
    mediaB = sumaB / contB 
    print(f"La suma de todos los numeros introducidos es: {sumaB}")
    print(f"La media de todos los numeros introducidos es: {mediaB:.2f}")
else:
    print("Introduce un numero al menos.")

