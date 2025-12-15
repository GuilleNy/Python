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

    # Start transaction
    conexion.start_transaction()

    sql = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES ('Madrid', 'España', 6.8)"
    cursor.execute(sql)
    conexion.commit()
    print(cursor.rowcount ,"filas se han insertado.")


    delete = "DELETE FROM ciudades WHERE poblacion_millones < 10 "
    cursor.execute(delete)
    conexion.commit()
    print(cursor.rowcount, "fila actualizada.")

    

    print("Transaction completed successfully")

except Error as e:
    print("Error durante la transacción:", e)
    if 'conexion' in locals() and conexion.is_connected():
        conexion.rollback()
        print("Transacción revertida por error.")

finally:
    if cursor is not None:
        try:
            cursor.close()
        except Exception as ex:
            print(f"Error al cerrar el cursor: {ex}")
    try:
        if conexion is not None:
            conexion.close()
    except Exception as ex:
        print(f"Error al cerrar la conexión MySQL: {ex}")