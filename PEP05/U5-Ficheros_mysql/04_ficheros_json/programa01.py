"""
Lectura de un fichero JSON
Crea un fichero llamado paises.json con el siguiente contenido:
    [
        {"nombre": "Japón", "continente": "Asia", "poblacion": 125.7},
        {"nombre": "Canadá", "continente": "América", "poblacion": 38.2},
        {"nombre": "España", "continente": "Europa", "poblacion": 48.0}
    ]
Escribe un programa que:
 Abra el archivo y lo lea con json.load().
 Muestre por pantalla cada país con un formato como:
    Japón está en Asia y tiene 125.7 millones de habitantes.
 Controle posibles errores con try/except.
"""
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
