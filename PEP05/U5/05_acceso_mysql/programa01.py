import mysql.connector
from mysql.connector import Error


try:
    conexion = mysql.connector.connect(
        host="localhost",
        user = "ciudades",
        password = "ciudades",
        database = "ciudades"
    )

    if conexion.is_connected():
        print("Conexión establecida correctamente")

    

except Error as e:
    print(f"Error con MySQL: {e}")

finally:
    try:
        if conexion is not None:
            conexion.close()
    except Exception as ex:
        print(f"Error al cerrar la conexión MySQL: {ex}")