"""
Añadir texto sin borrar el anterior
Modifica el ejercicio anterior para que, en lugar de sobrescribir, añada nuevas líneas cada
vez que se ejecute.
     Usa el modo 'a'.
     Al final, el fichero debe acumular todas las ejecuciones anteriores
"""


fichero = open("saludo.txt", "a", encoding="utf-8")

fichero.write("Hola Emiliano\n")
fichero.write("Hola Maria\n")
fichero.write("Hola Jose\n")


fichero.close()