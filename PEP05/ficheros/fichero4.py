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

except Exception as exc:
    print("Error", strerror(exc.errno))

