"""
Bloque with
Crea un programa que escriba una lista de nombres (["Ana", "Pedro", "Lucía", "Eva"]) en
un fichero alumnos.txt usando el bloque with.
Luego, en el mismo programa, vuelve a abrir el archivo con with y muestra todos los
nombres en mayúsculas.
"""


personas = ["Ana", "Pedro", "Lucía", "Eva"]


with open("alumnos.txt" , "w", encoding="utf-8") as fichero:
    
    for persona in personas:
        fichero.write(f"{persona}\n")




with open("alumnos.txt" , "r", encoding="utf-8") as fichero:

    contenido = fichero.read().upper()

    print(contenido)