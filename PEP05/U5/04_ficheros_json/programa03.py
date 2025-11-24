"""
Cargar un objeto desde una cadena JSON
Define en tu programa la siguiente cadena:
import json
    cadena_json = '''
        [
            {"nombre": "Chile", "moneda": "Peso chileno"},
            {"nombre": "Egipto", "moneda": "Libra egipcia"}
        ]
    '''
• Convierte la cadena en un objeto Python con json.loads().
• Muestra el tipo de dato que se obtiene.
• Imprime cada país con su moneda.
"""

import json

cadena_json = '''
[
    {"nombre": "chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

data = json.loads(cadena_json)

print("Tipo obtenido:", type(cadena_json))

for pais in data:
    print(f"{pais['nombre']} tiene como moneda el {pais['moneda']}.")