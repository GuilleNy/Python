def crear_inventario():
    inventario = dict()
    return inventario


def agregar_producto(inventario, codigo, nombre, precio_inicial):

    estado = False

    if codigo not in inventario:
        inventario[codigo]=(nombre, [precio_inicial])
        estado = True

    return estado


def actualizar_precio(inventario, codigo, nuevo_precio):
    estado = False

    if codigo in inventario:
        inventario[codigo][1].append(nuevo_precio)
        estado = True

    return estado


def obtener_producto(inventario, codigo):
    cadena = ""

    if codigo in inventario:
        nombre = inventario[codigo][0]
        precio_actual = inventario[codigo][1][-1]

        cadena = f"PRODUCTO: {nombre} | PRECIO ACTUAL: {precio_actual}"

    return cadena


def analizar_precios_producto(inventario, codigo):
    lista_precios = []

    if codigo in inventario:
        lista_precios = inventario[codigo][1].copy()
        lista_precios.sort()

    return lista_precios