"""
 Escritura de un fichero JSON
Crea un programa que genere un archivo capitales.json con la siguiente información:
    capitales = [
        {"país": "Francia", "capital": "París"},
        {"país": "Australia", "capital": "Canberra"},
        {"país": "Kenia", "capital": "Nairobi"},
        {"país": "Brasil", "capital": "Brasilia"}
    ]

Debe:
• Escribir los datos en formato JSON con json.dump().
• Usar los parámetros ensure_ascii=False y indent=4 para mejorar la legibilidad.
• Mostrar el mensaje: "Archivo 'capitales.json' creado
correctamente."
"""


from os import strerror
import json


try:
    capitales = [
        {"país": "Francia", "capital": "París"},
        {"país": "Australia", "capital": "Canberra"},
        {"país": "Kenia", "capital": "Nairobi"},
        {"país": "Brasil", "capital": "Brasilia"}
    ]

    #recomendable abrir un fichero con with open()
    with open("U5/04_ficheros_json/capitales.json", "w+", encoding="utf-8") as fichero_json:
        json.dump(capitales, fichero_json , ensure_ascii=False, indent=4)# ensure_ascii=False → mantiene tildes y ñ, indent=4 → mejora la legibilidad

        print("Archivo 'capitales.json' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
