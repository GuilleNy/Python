"""
 Escritura desde diccionarios con csv.DictWriter()
Crea un programa que escriba un archivo patrimonios.csv con información sobre
ciudades con lugares Patrimonio de la Humanidad:
    patrimonios = [
        {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
        {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
        {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
    ]
El programa debe:
     Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar
    emblemático"].
     Escribir la cabecera con writeheader() y las filas con writerows().
     Cambiar el delimitador a ;.
     Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente."
"""

from os import strerror
import csv

cabeceras = ["Ciudad", "País", "Lugar emblemático"]

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Egipto", "Lugar emblemático": "Templos históricos"}
]

try:

    #recomendable abrir un fichero con with open()
    with open("U5/03_ficheros_csv/patrimonios.csv", "w+", encoding="utf-8") as fichero_csv:
        
        writer = csv.DictWriter(fichero_csv, fieldnames=cabeceras, delimiter= ";")

        writer.writeheader()
        writer.writerows(patrimonios)
        

    print("Archivo 'patrimonios.csv' creado correctamente.")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
