"""
Lectura controlada
Crea un programa que lea un fichero texto.txt carácter a carácter usando read(1) hasta
llegar al final del archivo. Cuenta cuántos caracteres totales contiene y muestra el
resultado
"""




with open("texto.txt" , "r", encoding="utf-8") as fichero:

    c = fichero.read(1)
    cont = 0
    while c: #se repite mientras haya caracteres (si read(1) devuelve "", el bucle termina).
        print(c , end="")
        c = fichero.read(1)
        cont += 1

    print("")
    print(f"Hay {cont} caracteres.")

#Esto me devuelve 32 caracteres.
"""
Cada letra cuenta como 1 carácter.
Cada salto de línea \n también cuenta como 1 carácter.
"""