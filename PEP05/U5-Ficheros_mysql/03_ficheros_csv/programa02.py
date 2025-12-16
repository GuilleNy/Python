"""
Lectura con csv.DictReader()
Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
Debe:
 Mostrar los nombres de las columnas (fieldnames).
 Recorrer las filas e imprimir información como:

    {Ciudad} ({País}) tiene una población aproximada de {Población (millones)} millones.
    
 Si el archivo no incluye cabecera, define manualmente los campos necesarios
"""

from os import strerror
import csv


try:
   

    #recomendable abrir un fichero con with open()
    with open("ciudades.csv", "r", encoding="utf-8") as fichero_csv:
        reader = csv.DictReader(fichero_csv) #devuelve como un diccionario, usando la cabecera como claves

        cabeceras = reader.fieldnames #reader.fieldnames devuelve las cabeceras del CSV como una lista de strings. ['Ciudad', 'País', 'Población (millones)']
        
        print(f"Los nombres de las columnas son {cabeceras}")

        for fila in reader:
            print(f"{fila[cabeceras[0]]} ({fila[cabeceras[1]]}) tiene una poblacion aproximada de {fila[cabeceras[2]]} millones")


except Exception as exc:
    print("Error", strerror(exc.errno))
