from os import strerror


try:
    #recomendable abrir un fichero con with open()
    with open("texto.txt", "rt", encoding="utf-8") as fichero:

        #primera forma de leer un fichero
        contenido2 = fichero.readlines()
        print(contenido2)
        #segunda forma de recorrer un fichero

        for linea in fichero:
            print(len(linea))
            print(linea, end=" ")


        #Tercera forma de leer un fichero
        linea = fichero.readlines().strip()
        while linea:
            print(linea)
            linea = fichero.readlines().strip()
        

        #Cuarta forma de leer un fichero caracter a caracter.
        c = fichero.read(1)
        print(c)

        #mueve el puntero del archivo a la posición indicada.
        #En este caso, 0 significa volver al inicio del archivo.
        fichero.seek(0)
        print(c, end="")
        print()

        print(fichero .tell())



except Exception as exc:
    print("Error", strerror(exc.errno))

