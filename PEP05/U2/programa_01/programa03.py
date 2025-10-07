"""
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

num = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num2 == 0:
    print("No se puede dividir a 0.")
else:
    print(f"La division entre {num} y {num2} es: {num/num2}")