"""
Escribe un programa en Python que lea por teclado una cadena y un carácter, y
reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería
devolver su clave como: XXXX
"""

cadena = str(input("Introduce una cadena: "))
caracter = str(input("Introduce un caracter: "))

resultado = ""

for i in cadena:
    if i.isdigit():
        resultado += caracter
    else: 
        resultado += i

print(resultado)