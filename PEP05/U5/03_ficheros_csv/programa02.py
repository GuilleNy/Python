from os import strerror
import csv


try:
   

    #recomendable abrir un fichero con with open()
    with open("U5/03_ficheros_csv/ciudades.csv", "r", encoding="utf-8") as fichero_csv:
        reader = csv.DictReader(fichero_csv) #devuelve como un diccionario, usando la cabecera como claves

        cabeceras = reader.fieldnames #reader.fieldnames devuelve las cabeceras del CSV como una lista de strings. ['Ciudad', 'País', 'Población (millones)']
        
        print(f"Los nombres de las columnas son {cabeceras}")

        for fila in reader:
            print(f"{fila[cabeceras[0]]} ({fila[cabeceras[1]]}) tiene una poblacion aproximada de {fila[cabeceras[2]]} millones")


except Exception as exc:
    print("Error", strerror(exc.errno))
