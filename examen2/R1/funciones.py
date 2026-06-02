
def crear_inventario():
    diccionario = {}
    return diccionario


def agregar_producto(inventario, codigo, nombre, precio_inicial):
    valido = False

    if codigo not in inventario:
        inventario[codigo] = tuple(nombre,list(precio_inicial))

        valido = True

    return valido


def actualizar_precio(inventario, codigo, nuevo_precio):
    
    if codigo in inventario:
        for valor in inventario:
            print()


def obtener_productos(inventario, codigo):
    if codigo in inventario:

        print(f"PRODUCTO: {inventario.get(codigo)[0]} | PRECIO ACTUAL: {inventario.get(codigo)[1][len(inventario.get(codigo)[1])]}")
    else:
        print("No existe")


def analizar_precios_productos(inventario, codigo):
    lista = []
    if codigo in inventario:
        lista.append(max(inventario.get(codigo)[1]))

    lista_ordenada = sorted(lista)
    lista_ordenada.reverse()
    return lista_ordenada