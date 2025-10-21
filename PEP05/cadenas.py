a=3
b=4


cadena1 = "El número a es {} y el número b es {}".format(5, 10)
print(cadena1)

cadena2 = F"El número a es {a} y el número b es {b}"
print(cadena2)

cadena3="hola"
print(cadena3*3)


cadena4 = "a"
cadena5 = "b"

print(cadena4 < cadena5)

#Acceder por slicing
#El slicing permite extraer subcadenas mediante rango de índices.
cadena6="Hola muy buenas"

print(cadena6[0:6])

texto = "Python es genial"

# 1. Extraer los primeros 6 caracteres
print(texto[0:6])  # 'Python'

# 2. Extraer desde el carácter 7 hasta el final
print(texto[7:])   # 'es genial'

# 3. Extraer cada segundo carácter
print(texto[::2])  # 'Pto s enl'

# 4. Invertir la cadena
print(texto[::-1]) # 'laineg se nohtyP'

print(texto[0:10:3])


for letra in texto:
    print(letra)


print("*****************************************+")
for i in range(len(texto)):
    print(texto[i])