"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""

num_par = int(input("Introduce un numero par: "))

if num_par % 2 == 0 :
    num_impar = int(input("Introduce un numero impar: "))
    if num_impar % 2 != 0:
        print("Correcto.")
    else:
        print("EL numero impar introducido no es impar.")
else:
    print("EL numero par introducido no es par.")
