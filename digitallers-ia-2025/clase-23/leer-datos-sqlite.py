import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('alumnos.db')

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar la consulta SELECT
cursor.execute("SELECT * FROM alumnos")

# Obtener todos los resultados
filas = cursor.fetchall()

# Mostrar los resultados
for fila in filas:
    print(fila)

# Cerrar la conexión
conexion.close()
