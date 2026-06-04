#GUILLERMO NIEBLA PINCAY

from funciones_biblioteca import crear_catalogo, agregar_libro, devolver_libro, obtener_libro, prestar_libro, saludo


def main():

    catalogo = crear_catalogo()

    print("Agregar Libro")
    print(agregar_libro(catalogo, "ISBN-001", "El Quijote", "Cervantes", 1605))
    print(agregar_libro(catalogo, "ISBN-002", "Reina Roja", "Juan Gomez Jurado", 2018))
    print(agregar_libro(catalogo, "ISBN-003", "El saber", "Maria Batistuta", 2002))

    print("Agregar Libro dupicado")
    print(agregar_libro(catalogo, "ISBN-002", "El saber", "Maria Batistuta", 2002))


    print("Prestar dos Libros")
    print(prestar_libro(catalogo, "ISBN-001"))
    print(prestar_libro(catalogo, "ISBN-002"))

    print("Prestar un libro ya prestado")
    print(prestar_libro(catalogo, "ISBN-001"))

    print("Devolver un libro")
    print(devolver_libro(catalogo, "ISBN-002"))

    print("Mostrar Libro")
    print(obtener_libro(catalogo, "ISBN-001"))


#Programa principal
if __name__ == "__main__":
    main()