"""
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""

num = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))



if num > num2 :
    print(f"El {num} es mayor que {num2}")
elif num < num2:
    print(f"El {num2} es mayor que {num}")
else:
    print("Ambos numeros son iguales.")

