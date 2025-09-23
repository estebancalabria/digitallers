from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask("Mi APP con SQLite")
DB = "personas.db"

def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insertar_persona(nombre):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO personas (nombre) VALUES (?)', (nombre,))
    conn.commit()
    conn.close()

#Se fina si existe el archivo personas.db
existe_archivo = os.path.exists(DB)
init_db()
if not existe_archivo:
    insertar_persona("Juan")
    insertar_persona("Maria")

@app.route('/personas', methods=['GET'])
def get_personas():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM personas')
    personas = cursor.fetchall()
    conn.close()
    personas_json = [{"id": id, "nombre": nombre} for id, nombre in personas]
    return jsonify(personas_json)

#Quiero poder recuperar una persona especifica por su ID /personas/1
@app.route('/personas/<int:persona_id>', methods=['GET'])
def get_persona(persona_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM personas WHERE id = ?', (persona_id,))
    persona = cursor.fetchone()
    conn.close()
    if persona:
        return jsonify({"id": persona[0], "nombre": persona[1]})
    return jsonify({"error": "Persona no encontrada"}), 404

#Agrego una persona
@app.route('/personas', methods=['POST'])
def agregar_persona():
    nuevo_nombre = request.json.get('nombre')
    if nuevo_nombre:
        insertar_persona(nuevo_nombre)
        return jsonify({"mensaje": "Persona agregada"}), 201
    return jsonify({"error": "Nombre no proporcionado"}), 400

#Agreguemos el actualizar por put
@app.route('/personas/<int:persona_id>', methods=['PUT'])
def actualizar_persona(persona_id):
    nuevo_nombre = request.json.get('nombre')
    if nuevo_nombre:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute('UPDATE personas SET nombre = ? WHERE id = ?', (nuevo_nombre, persona_id))
        conn.commit()
        conn.close()
        if cursor.rowcount == 0:
            return jsonify({"error": "Persona no encontrada"}), 404
        return jsonify({"mensaje": "Persona actualizada"})
    return jsonify({"error": "Nombre no proporcionado"}), 400

app.run(debug=True)
