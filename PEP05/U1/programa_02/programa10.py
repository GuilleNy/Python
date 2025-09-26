print("Introduce un numero de dos cifras: ")
num=int(input())

resto=num % 10
num=round(num / 10)

print(f"{resto}{num}")


