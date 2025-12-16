from funciones import crear_inventario, agregar_producto, actualizar_precio, obtener_productos, analizar_precios_productos


inventario = {"P001": ("Portatil", [1200.00, 1150.50, 1100.00]), 
              "P002": ("Teclado", [15.50, 16.00])}





def main():

    inventario = crear_inventario

    

    codigo = input("Introduce el codigo del producto: ")
    nombre = input("Introduce el nombre del producto: ")
    precio_inicial = int(input("INtroduce el precio inical del producto: "))


    inventario = agregar_producto(inventario, codigo, nombre, precio_inicial)

    obtener_productos(inventario, codigo)


if __name__ == "__main__":
    main()