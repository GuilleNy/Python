from os import strerror
import json


try:
   

    #recomendable abrir un fichero con with open()
    with open("U5/04_ficheros_json/paises.json", "r", encoding="utf-8") as fichero_json:
        datos = json.load(fichero_json)


        for fila in datos:
            print(f"{fila['nombre']} está en {fila['continente']} y tiene {fila['poblacion']} millones de habitantes.")


except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
