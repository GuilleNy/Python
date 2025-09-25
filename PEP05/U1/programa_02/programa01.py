"""
Escribe un programa que cree cuatro variables que almacenen respectivamente un
entero, un float, un booleano y una cadena de caracteres. A continuación que muestre por
pantalla en valor de cada una de ellas y el tipo de datos de los objetos a los que apuntan
"""

num_entero=34
num_float=4.2
vr_boolean=True
vr_str="Buenos Dias"

print(f"El numero {num_entero} su tipo de dato de objeto al que apunta es:   {id(num_entero)}")
print(f"El numero {num_float} su tipo de dato de objeto al que apunta es:  {id(num_float)}")
print(f"El booleano {vr_boolean} su tipo de dato de objeto al que apunta es:  {id(vr_boolean)}")
print(f"La cadeba '{vr_str}' su tipo de dato de objeto al que apunta es:  {id(vr_str)}")
