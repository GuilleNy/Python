#GUILLERMO NIEBLA


num_int = int(input("Introduce un numero entero: "))
num_dec = float(input("Introduce un numero decimal: "))
cadena = str(input("Introduce una cadena de texto: "))


print(f"el valor {num_int} es de tipo " ,type(num_int))
print(f"el valor {num_dec} es de tipo " ,type(num_dec))
print(f"el valor {cadena} es de tipo " ,type(cadena))


esInt = isinstance(num_int,int)
esFloat = isinstance(num_dec,float)
esStr = isinstance(cadena,str)
print(esInt)
print(esFloat)
print(esStr)


correcto = esInt and esFloat and esStr

suma = num_int + num_dec

print(f"Comprobacion: {correcto}")
print(f"La suma es: {suma}")