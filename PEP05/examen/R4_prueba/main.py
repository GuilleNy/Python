from operaciones_tienda import crear_inventario, actualizar_precio, agregar_producto, analizar_precios_producto, obtener_producto



def main():

    inventario = crear_inventario()

    print(agregar_producto(inventario, "P001", "Portátil", 1200.00))
    print(agregar_producto(inventario, "P002", "Teclado", 15.50))

    # Producto duplicado
    print(agregar_producto(inventario, "P001", "Portátil", 1300.00))


    actualizar_precio(inventario, "P001", 1150.50)
    actualizar_precio(inventario, "P001", 1100.00)
    actualizar_precio(inventario, "P002", 16.00)

    print(obtener_producto(inventario, "P001"))

    print(analizar_precios_producto(inventario, "P001"))

    print()











#Programa principal
if __name__ == "__main__":
    main()