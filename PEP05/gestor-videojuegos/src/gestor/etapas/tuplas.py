
# Lista de videojuegos, cada uno representado como una tupla (titulo, año, genero)

def visualizar_videojuegos():

    videojuegos = (
        ("The Legend of Zelda", 1986, "Rol"),
        ("Super Mario Bros", 1985, "Plataformas"),
        ("Minecraft", 2011, "Sandbox"),
        ("The Witcher 3: Wild Hunt", 2015, "Rol"),
        ("Halo: Combat Evolved", 2001, "Acción")
    )

    for juego in videojuegos:
        titulo, año, genero = juego
        print(f"{titulo} ({año}) {genero}")
