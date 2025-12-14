"""
Escribe un programa en Python que lea por teclado números y los guare en una lista, el
proceso finaliza cuando se introduzca un número negativo. A continuación que muestre el
máximo de los números guardado en la lista y los números pares de la lista
"""
lista_numeros = []

numeros = int(input("Introduzca cualquier numero: "))

while numeros > 0:
    lista_numeros.append(numeros)
    numeros = int(input("Introduzca cualquier numero: "))

print(lista_numeros)

print(max(lista_numeros))

#Crear una lista con los números pares de los 10 primeros números:
lista_pares = [i for i in lista_numeros if i % 2 ==0]
print(lista_pares)