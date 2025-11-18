from os import strerror

personas = ["Ana", "Pedro", "Eva", "Lucas"]
personas2 = ["Ana\n", "Pedro\n", "Eva\n", "Lucas\n"]

datos = bytearray(10)

for i in range(len(datos)):
    datos[1] = 10 + i


 #Escribir un fichero binario
try:
    #recomendable abrir un fichero con with open()
    with open("ficheros/file.bin", "rb") as fichero:
        
        #datos = fichero.read()
        datos = fichero.read(2)
        byte_data = bytearray(datos)

        for b in byte_data:
            print(hex(b), end=" ")

        for b in byte_data:
            print(bin(b), end=" ")


except Exception as exc:
    print("Error", strerror(exc.errno))

