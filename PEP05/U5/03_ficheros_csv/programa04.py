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
