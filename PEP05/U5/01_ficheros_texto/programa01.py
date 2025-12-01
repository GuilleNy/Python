#Abrimos el fichero .txt en modo lectura con codificacion UTF-8

fichero = open("datos.txt", "rt", encoding="utf-8")

#Leemos el contenido

contenido = fichero.read()

#Imprimimos el contenido

print(contenido)

#Cerramos fichero

fichero.close()