from os import strerror
import csv

try:
    #recomendable abrir un fichero con with open()
    with open("U5/03_ficheros_csv/ciudades.csv", "r") as fichero_csv:
        reader = csv.reader(fichero_csv , delimiter=",")

        cabecera_fila = next(reader) #next(reader) avanza una fila del lector
        print(f"Los nombres de las columnas son {",".join(cabecera_fila)}")
        
        for fila in reader:
            print(f"El videojuego {fila[0]} es del genero {fila[1]} y se publico en el año {fila[2]}")

except Exception as exc:
    print("Error", strerror(exc.errno))
