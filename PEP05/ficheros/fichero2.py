from os import strerror


try:
    fichero = open("texto.txt", "rt", encoding="utf-8")

    try:
        contenido2 = fichero.readlines()
        print(contenido2)
    except Exception as exc:
        print("Error", strerror(exc.errno))
    finally:
        fichero.close()

except Exception as exc:
    print("Error", strerror(exc.errno))

