"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra.
"""

print("Introduce la cantidad de la compra: ")
cantidad=float(input())

cant=cantidad * 0.15
cant_desc= cantidad - cant 

print(f"Total a pagar con el descuento del 15%: {cant_desc}")