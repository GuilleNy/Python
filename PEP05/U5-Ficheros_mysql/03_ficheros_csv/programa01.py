"""
Lectura básica con csv.reader()
Crea un fichero llamado ciudades.csv con el siguiente contenido:
    Ciudad,País,Población (millones)
    Tokio,Japón,37.4
    Delhi,India,30.3
    Shanghái,China,27.1
    São Paulo,Brasil,22.0
Escribe un programa que:
 Lea el fichero usando csv.reader().
 Muestre en pantalla frases como:
 La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
 Controle las posibles excepciones
"""

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
