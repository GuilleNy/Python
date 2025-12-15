"""
Escribir un objeto Python en una cadena JSON
Crea el siguiente diccionario en tu programa:
    pais = {
        "nombre": "Islandia",
        "capital": "Reikiavik",
        "idiomas": ["Islandés", "Inglés"],
        "superficie_km2": 103000
    }
• Convierte el diccionario en una cadena JSON con json.dumps().
• Usa los parámetros indent=2 y sort_keys=True.
• Imprime la cadena generada


"""
import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

#Para escribir un objeto en una cadena con formato JSON existe la función json.dumps()

cadena_json = json.dumps(pais, indent=2, ensure_ascii=False ,sort_keys=True)
print(cadena_json)

