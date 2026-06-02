import mysql.connector
from mysql.connector import Error


try:
    conexion = mysql.connector.connect(
        host="localhost",
        user = "series",
        password = "series",
        database = "series"
    )


    cursor = conexion.cursor()
    """
    sql = "INSERT INTO series (nombre, temporadas, genero) VALUES (%s, %s, %s);"
    valores = ("Breaking Bad", 5, "Drama")
    """
   
    if conexion.is_connected():
        print("Conexión establecida correctamente")

    sql = "SELECT * FROM series;" # Consulta para obtener todos los registros de la tabla 'series'.

    cursor.execute(sql)

    resultados = cursor.fetchall() # Obtener todos los registros, devuelve una lista de tuplas.

    #print(resultados)

    for serie in resultados:
        #print(serie)
        print(serie[1])  # Imprime el segundo campo de cada registro.



    conexion.commit() # Confirma los cambios en la base de datos, cuando tengas operaciones de inserción, actualización o eliminación.
    print(f"Se insertaron {cursor.rowcount} registros.")
    print(conexion)

    cursor.close()
    conexion.close()
except Error as e:
    print(f"Error con MySQL: {e}")