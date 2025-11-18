from os import strerror

datos = bytearray(5)
bytes #mutable
bytearray #inmutable

 #Escribir un fichero binario
try:
    #recomendable abrir un fichero con with open()
    with open("ficheros/file.bin", "rb") as fichero:
        
        #datos = fichero.read()
        #lee todos los bytes del fichero y los almacena de un bytearray

        m = fichero.readinto(datos)
        print(m)
        for b in datos:
            print(hex(b), end=" ")

        #fichero.seek(0) vuelve el puntero al principio
        
        m = fichero.readinto(datos)
        print(m)
        for b in datos:
            print(hex(b), end=" ")


except Exception as exc:
    print("Error", strerror(exc.errno))

