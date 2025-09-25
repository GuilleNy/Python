#Siempre saber que tipos de datos se vaya a pedir por teclado para que no exista error.
base=int(input("Introduce la base:"))
altura=int(input("Introduce la altura:"))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")
