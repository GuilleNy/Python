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
    sql = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES (%s, %s, %s)"
    datos = [
        ("Tokio", "Japón", 37.4),
        ("Delhi", "India", 30.3),
        ("Shanghái", "China", 27.1),
        ("São Paulo", "Brasil", 22.0),
        ("Ciudad de México", "México", 21.7)
    ]
    cursor.executemany(sql, datos)

    conexion.commit()

    print(cursor.rowcount ,"filas se han insertado..")

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