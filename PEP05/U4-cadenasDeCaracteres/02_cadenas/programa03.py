"""
Escribe un programa en Python que lea una cadena de caracteres y muestre la siguiente
información:
• La primera letra de cada palabra escrita en mayúsculas. 
Por ejemplo, si recibe
Organización de las Naciones Unidas, debe devolver ONU.
• Las palabras que comienzan por minúscula. 
Por ejemplo, si recibe
Organización de las Naciones Unidas, debe devolver de y las
"""

cadena = "Organización de las Naciones Unidas"

resultado = ""

for i in cadena:
    if i.isupper():
        resultado += i

print(resultado)


cadena2 = cadena.split(' ')
resultado2 = ""

for i in cadena2:
    if i.islower():
        resultado2 += i + " "

print(resultado2)