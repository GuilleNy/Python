"""
Escribe un programa que
-Cree una variable que almacene el número entero 6.
-Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto
al que apunta la variable (deben ser iguales)
-Cree otra variable a la que se asigne la primera variable.
-Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
al que apunta la variable (deben ser iguales)
-Utilice los operadores de identidad (is e is not) para comprobar y mostrar por
pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma
posición de memoria.
-Asigne la cadena “Hola” a la primera variable.
-Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del
objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
-Utilice la función isinstance() para comprobar y mostrar por pantalla que el
objeto al que apunta la primera variable es de tipo int y el de la segunda es de
tipo str.
"""




#Creamos una variable var_1 con el numero 6 y mostramos el tipo de objeto del numero 6 y el tipo al que apunta la variable var_1.
var_1=6
print(f"El tipo del objeto que contiene el número 6 es {type(6)} y el tipo del objeto al que apunta la variable var_1 es {type(var_1)}")
print(f"type(6) = {type(6)}")
print(f"type(var_1) = {type(var_1)}")
print()

#Mostramos los tipos, creamos una segunda variable var_2 y le asignamos la primera variable var_1 y mostramos el tipo de objeto del numero 6 y el tipo al que apunta la variable var_2.
var_2=var_1
print(f"El tipo del objeto que contiene el número 6 es {type(6)} y el tipo del objeto al que apunta la variable var_2 es {type(var_2)}")
print(f"type(6) = {type(6)}")
print(f"type(var_2) = {type(var_2)}")
print()

#Comprobacion con los operadores de identidad
print(f"var_1 is var_2 -> {var_1 is var_2}")       #True , si apunta
print(f"var_1 is not var_2 -> {var_1 is not var_2}")   #false, si apunta
print()

#Posicion de memoria
print(f"Posicion de memoria de la variable var_1 con id() {id(var_1)}")
print(f"Posicion de memoria de la variable var_2 con id() {id(var_2)}")
print()

#Asigno la cadena "Hola" a la primera variable que es var_1
var_1="Hola"
print(f"El tipo del objeto que contiene la cadena 'Hola' es {type("Hola")} y el tipo del objeto al que apunta la variable var_1 es {type(var_1)}")
print(f"type('Hola') = {type("Hola")}")
print(f"type(var_1) = {type(var_1)}")
print()

#Se comprueba los tipos con isinstance()
print(f"isinstance(var_1, int) -> {isinstance(var_1,int)}")
print(f"isinstance(var_2, str) -> {isinstance(var_2,str)}")