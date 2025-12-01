"""
 Lectura línea a línea
Escribe un programa en Python que lea el mismo archivo datos.txt línea a línea y muestre
cada línea numerada en pantalla.
     Usa la función enumerate().
     El formato debe ser:
        ◦ Línea 1: <contenido>.
        ◦ Línea 2: <contenido>
        ◦ ...
"""

#Abrimos el fichero .txt en modo lectura con codificacion UTF-8

fichero = open("datos.txt", "rt", encoding="utf-8")

#Leemos el contenido

for linea_no, linea in enumerate(fichero, start=1):
    print(f"Linea: {linea_no}: {linea.strip()}")


fichero.close()