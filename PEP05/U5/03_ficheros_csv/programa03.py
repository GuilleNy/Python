from os import strerror
import csv


try:
   

    #recomendable abrir un fichero con with open()
    with open("U5/03_ficheros_csv/ciudades.csv", "w+", encoding="utf-8") as fichero_csv:
        

except Exception as exc:
    print("Error", strerror(exc.errno))
