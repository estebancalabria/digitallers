#El codigo de la API
from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para obtener todas las personas
@app.route('/personas', methods=['GET'])
def get_personas():
  personas = [
    {'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez', 'direccion': 'Calle Falsa 123', 'telefono': '123456789'},
    {'id': 2, 'nombre': 'Ana', 'apellido': 'García', 'direccion': 'Avenida Siempre Viva 742', 'telefono': '987654321'}
  ]
  return jsonify(personas)

app.run(port=5000)