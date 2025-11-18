from os import strerror

personas = ["Ana", "Pedro", "Eva", "Lucas"]
personas2 = ["Ana\n", "Pedro\n", "Eva\n", "Lucas\n"]

datos = bytearray(10)

for i in range(len(datos)):
    datos[1] = 10 + i


 #Escribir un fichero binario
try:
    #recomendable abrir un fichero con with open()
    with open("file.bin", "wb") as fichero:
        
        fichero.write(datos)

except Exception as exc:
    print("Error", strerror(exc.errno))

