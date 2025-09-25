print("Introduce la cantidad de la compra: ")
cantidad=float(input())

cant=cantidad * 0.15
cant_desc= cantidad - cant 

print(f"Total a pagar con el descuento del 15%: {cant_desc}")