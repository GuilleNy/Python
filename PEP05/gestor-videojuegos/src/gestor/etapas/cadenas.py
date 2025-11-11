


def buscar_videojuego(videojuegos):

    nombre_videJueg = str(input("Escribe el nombre de un videojuego: "))

    #Quitamos los espacios y convertimos a minusculas
    nombre_videJueg = nombre_videJueg.strip().lower()

    # Variable para saber si se ha encontrado el juego
    encontrado = False

    # Buscamos el videojuego en la lista
    for titulo, año, genero in videojuegos:
        if (titulo.lower() == nombre_videJueg) and  not encontrado :
            print(f"Titulo: {titulo} | Genero: {genero} | Año: {año}")
            encontrado = True

    # Si no se encuentra el videojuego
    if not encontrado:
        print("El videojuego no se encuentra en la lista.")

