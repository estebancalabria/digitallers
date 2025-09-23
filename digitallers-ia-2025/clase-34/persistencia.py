
import sqlite3
from model import Automovil

DB_NAME = 'automoviles.db'  ##Constante

class PersistenciaAutomovil:
    
    @staticmethod
    def crear_tabla():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS automoviles (
                id TEXT PRIMARY KEY,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                año INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def insertar_automovil(automovil):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO automoviles (id, marca, modelo, año) VALUES (?, ?, ?, ?)
        ''', (automovil.get_id(), automovil.get_marca(), automovil.get_modelo(), automovil.get_año()))
        conn.commit()
        conn.close()

    @staticmethod
    def recuperar_automovil(id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT id, marca, modelo, año FROM automoviles WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Automovil(id=row[0],marca=row[1], modelo=row[2], año=row[3])
        return None

    @staticmethod
    def recuperar_todos_los_automoviles():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT id, marca, modelo, año FROM automoviles')
        rows = cursor.fetchall()
        conn.close()
        automoviles = []
        for row in rows:
            automoviles.append(Automovil(id=row[0], marca=row[1], modelo=row[2], año=row[3]))
        return automoviles

    @staticmethod
    def actualizar_automovil(automovil):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE automoviles SET marca = ?, modelo = ?, año = ? WHERE id = ?
        ''', (automovil.get_marca(), automovil.get_modelo(), automovil.get_año(), automovil.get_id()))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar_automovil(id):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM automoviles WHERE id = ?', (id,))
        conn.commit()
        conn.close()