#GUILLERMO NIEBLA PINCAY
def crear_catalogo():
    catalogo = dict()
    return catalogo

def agregar_libro(catalogo, isbn, titulo, autor, anio):
    existe = False

    if isbn not in catalogo:
        catalogo[isbn]=[(titulo,autor, anio), {"disponible": True, "prestamos":0}]
        existe = True
    return existe

def prestar_libro(catalogo, isbn):
    existe = False

    if isbn in catalogo:
        estado = catalogo[isbn][1]

        if estado["disponible"]:
            estado["disponible"]=False
            estado["prestamos"] += 1
            existe = True

    return existe

def devolver_libro(catalogo, isbn):
    existe = False

    if isbn in catalogo:
        estado = catalogo[isbn][1]

        if not estado["disponible"]:
            estado["disponible"]=True
        
        existe = True

    return existe

def obtener_libro(catalogo, isbn):
    cadena = ""

    if isbn in catalogo:
        datos = catalogo[isbn][0]
        estado = catalogo[isbn][1]

        libro = datos[0]
        autor = datos[1]
        anio = datos[2]

        if estado["disponible"]:
            texto = "Disponible"
        else:
            texto = "Prestado"
    
        cadena = (f"LIBRO: {libro} | AUTOR: {autor} | AÑO: {anio} | ESTADO: {texto}")
    
    return cadena

#def libros_mas_prestados(catalogo, n):
  
def saludo():
    print("hola")