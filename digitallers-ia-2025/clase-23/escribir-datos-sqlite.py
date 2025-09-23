##Que me pregunte el nomre y el apellido y lo guarde en la tabla alumnos
import sqlite3

# Connect to SQLite database. It will be created if it doesn't exist.
conn = sqlite3.connect('alumnos.db')

# Ask for user input
nombre = input("Please enter your name: ")
apellido = input("Please enter your last name: ")
# Save to database
cur = conn.cursor()
cur.execute('INSERT INTO alumnos (nombre, apellido) VALUES (?, ?)', (nombre, apellido))
conn.commit()
print(f"Alumno {nombre} {apellido} saved successfully.")

# Close the connection
conn.close()
