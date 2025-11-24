"""
Listado y filtrado de países
Crea un programa que:
• Lea el archivo paises.json del ejercicio 1.
• Pida al usuario el nombre de un continente.
• Muestre solo los países pertenecientes a ese continente.
• Guarde esos resultados en un nuevo archivo JSON llamado
paises_filtrados.json

"""

from os import strerror
import json




try:

    with open("U5/04_ficheros_json/paises.json", "r", encoding="utf-8") as fichero_paises:
        paises = json.load(fichero_paises)


    continente = input("Introduce el nombre de un continente: ")

    paises_filtrados = []

    for fila in paises:
        if fila['continente'] == continente:
            paises_filtrados.append(fila)
            print(f"{fila['nombre']} tiene una poblacion de {fila['poblacion']} millones de habitantes.")


    with open("U5/04_ficheros_json/paises_filtrados.json", "w+", encoding="utf-8") as fichero_json:
        json.dump( paises_filtrados, fichero_json , ensure_ascii=False, indent=4)

        print("Archivo 'paises_filtrados.json' creado correctamente.")



except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)