

fichero = open("texto.txt", "rt", encoding="utf-8")


contenido1 = fichero.read()

#fichero.seek(0)

contenido2 = fichero.readlines()

print(contenido1)
print(contenido2)

fichero.close()