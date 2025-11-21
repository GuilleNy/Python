from os import strerror
import csv


try:
   

    #recomendable abrir un fichero con with open()
    with open("U5/03_ficheros_csv/ciudades.csv", "r", encoding="utf-8") as fichero_csv:
        reader = csv.reader(fichero_csv , delimiter=",")

        cabecera_fila = next(reader) #next(reader) devuelve la primera fila y avanza a la siguiente fila.
        #print(f"Los nombres de las columnas son {",".join(cabecera_fila)}")
        
        for fila in reader:
            print(f"La ciudad de {fila[0]} esta en {fila[1]} y tiene {fila[2]} millones de habitantes.")

except Exception as exc:
    print("Error", strerror(exc.errno))
