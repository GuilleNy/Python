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
    sql = "CREATE TABLE ciudades (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100) NOT NULL, pais VARCHAR(50), poblacion_millones FLOAT);"

    cursor.execute(sql)

    print("Tabla creada correctamente.")

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