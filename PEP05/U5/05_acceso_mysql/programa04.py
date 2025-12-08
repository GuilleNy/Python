import mysql.connector
from mysql.connector import Error

cursor = None
conexion = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user = "ciudades",
        password = "ciudades",
        database = "ciudades"
    )

    cursor = conexion.cursor()
    sql = "SELECT nombre , poblacion_millones FROM ciudades   WHERE poblacion_millones > 25 "
    cursor.execute(sql)

    resultado = cursor.fetchall()

    for ciudad in resultado:
        print(ciudad)

except Error as e:
    print(f"Error con MySQL: {e}")

finally:
    try:
        if cursor is not None:
            cursor.close()
        if conexion is not None:
            conexion.close()
    except Exception as ex:
        print(f"Error al cerrar la conexión MySQL: {ex}")