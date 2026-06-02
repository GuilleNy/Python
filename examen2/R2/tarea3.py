import mysql.connector
from mysql.connector import Error
cursor = None
conexion = None

try:
    #Conexion
    conexion = mysql.connector.connect(
        host="localhost",
        user = "planetas",
        password = "planetas",
        database = "planetas"
    )

    #Crear tabla
    cursor = conexion.cursor()
    sql = "CREATE TABLE planetas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100) NOT NULL, tipo VARCHAR(50), lunas INT);"

    cursor.execute(sql)
    print("Tabla creada correctamente.")


    #Insertar tabla
    sql2 = "INSERT INTO planetas (id, nombre, tipo, lunas) VALUES (%s, %s, %s, %s)"
    datos = [
        (1, "Jupiter", "Gaseoso" , 3),
        (2, "Marte", "Rocoso" , 1 )
    ]

    cursor.executemany(sql2, datos)
    conexion.commit()
    print(cursor.rowcount ,"filas se han insertado..")


    #Consulta tabla
    sql_consulta = "SELECT id , nombre, tipo, lunas FROM planetas WHERE id = 1 "
    cursor.execute(sql_consulta)

    resultado = cursor.fetchall() 

    #Visualizo la consulta
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