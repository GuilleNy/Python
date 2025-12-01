from os import strerror

personas = ["Ana", "Pedro", "Eva", "Lucas"]
personas2 = ["Ana\n", "Pedro\n", "Eva\n", "Lucas\n"]

 #Escribir en el fichero
try:
    #recomendable abrir un fichero con with open()
    with open("nuevo_texto.txt", "w", encoding="utf-8") as fichero:

        #Escribir idrectamente una linea
        fichero.write("linea 1\n")

        #Escribir con una lista
        for persona in personas:
            fichero.write(f"{persona}\n")

        #Escribir una secuencia
        #No añade automáticamente saltos de línea, así que si quieres que cada línea sea independiente, debes poner \n al final de cada string.
        fichero.writelines(personas2)

        

except Exception as exc:
    print("Error", strerror(exc.errno))

