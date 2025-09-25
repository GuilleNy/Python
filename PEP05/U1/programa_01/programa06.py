"""
Escribe un programa que use varias veces la función printf() para:
"""
"""
 Mostrar las operaciones del los operadores aritméticos de Python entre dos
números.
"""
a=3
b=2

print("Operadores aritméticos")
print(f"a + b -> {a + b}")
print(f"a - b -> {a - b}")
print(f"a * b -> {a * b}")
print(f"a / b -> {a / b}")
print(f"a // b -> {a // b}")
print(f"a % b -> {a % b}")
print(f"a ** b -> {a ** b}")


"""
 Mostrar las operaciones de los operadores lógicos de Python con valores
booleanos.
"""
v_bolean=True
f_bolean=False

print("Operadores lógicos")
print(f"True and True -> {v_bolean and v_bolean}")
print(f"False and False -> {f_bolean and f_bolean}")
print(f"True and False -> {v_bolean and f_bolean}")

print(f"True or True -> {v_bolean or v_bolean}")
print(f"False or False -> {f_bolean or f_bolean}")
print(f"True or False -> {v_bolean or f_bolean}")

print(f"not False -> {not f_bolean}")
print(f"not True -> {not v_bolean}")

"""
 Mostrar las operaciones de los operadores de comparación de Python con valores
booleanos y/o números.
"""
print("Operadores de comparación")
print(f"True == False -> {v_bolean == f_bolean}")
print(f"True != False -> {v_bolean != f_bolean}")
print(f"True < False -> {v_bolean < f_bolean}")
print(f"True > False -> {v_bolean > f_bolean}")
print(f"True <= False -> {v_bolean <= f_bolean}")
print(f"True >= False -> {v_bolean >= f_bolean}")
print()
print(f"a == b -> {a == b}")
print(f"a != b -> {a != b}")
print(f"a < b -> {a < b}")
print(f"a > b -> {a > b}")
print(f"a <= b -> {a <= b}")
print(f"a >= b -> {a >= b}")

