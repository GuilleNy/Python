a = "Hola muy buenas, es un placer conocerlo."
b = "123456789"

c = [5, 7, 23 , 6 , 1, 344]

lista2 = list(b)

print(lista2)

ultimoIndice = len(lista2) -1 

print(lista2[ultimoIndice])



for numeros in lista2:
    print(numeros)

print("")

for i in range(len(lista2)):
    print(lista2[i])



texto = "3+4"
texto2 = "3+4"

lista_split = texto.split('+')
lista_partition = list(texto2.partition('+'))

print(lista_split)
print(lista_partition)