

#Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y perímetro.
base=int(input("Introduce la base:"))
altura=int(input("Introduce la altura:"))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área es: {area}")
print(f"El perímetro es: {perimetro}")
