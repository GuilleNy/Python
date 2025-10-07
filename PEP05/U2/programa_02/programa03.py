"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue
"""
print("Pares con For: ")
for i in range(0, 10):
    if i % 2 == 0:
        print(i , end=" ")

print("\nPares con While: ")
cont = 0

while cont < 10:
    if cont % 2 == 0:
        print(cont , end=" ")
    cont = cont + 1

print("\nPares con For con continue: ")
for i in range(0, 10):
    if i % 2 != 0:
        continue
    print(i , end=" ")


print("\nPares con While con continue: ")
cont2 = 0

while cont2 < 10:
    if cont2 % 2 != 0:
        cont2 = cont2 + 1
        continue
    print(cont2 , end=" ")
    cont2 = cont2 + 1
