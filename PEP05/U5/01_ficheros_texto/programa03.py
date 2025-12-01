"""
Escritura básica
Escribe un programa que cree un fichero saludo.txt y escriba tres frases dentro.
     Usa el modo 'w'.
     Comprueba que al ejecutar el programa dos veces, el archivo se sobrescribe
"""

#Abrimos el fichero .txt en modo lectura con codificacion UTF-8

fichero = open("saludo.txt", "w", encoding="utf-8")

fichero.write("Hola Guillermo\n")
fichero.write("Hola Melanie\n")
fichero.write("Hola Lisbeth\n")


fichero.close()