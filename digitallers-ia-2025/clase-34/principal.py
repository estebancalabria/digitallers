from model import Automovil
from persistencia import PersistenciaAutomovil
from flask import Flask, request, jsonify


#Codigo que tenera una app de flask
app = Flask(__name__)


#Quiero un endpoint /api/personas que me devuelva la lista de personas en formato JSON

@app.route('/api/automoviles', methods=['GET'])
def get_automoviles():
    automoviles = PersistenciaAutomovil.recuperar_todos_los_automoviles()

    automoviles_list = [{
        'id': auto.get_id(),
        'marca': auto.get_marca(),
        'modelo': auto.get_modelo(),
        'año': auto.get_año()
    } for auto in automoviles]

    return jsonify(automoviles_list)

#Quiero para recuperar un automovil por id
@app.route('/api/automoviles/<id>', methods=['GET'])
def get_automovil(id):
    automovil = PersistenciaAutomovil.recuperar_automovil(id)
    if automovil:
        return jsonify({
            'id': automovil.get_id(),
            'marca': automovil.get_marca(),
            'modelo': automovil.get_modelo(),
            'año': automovil.get_año()
        })
    return jsonify({'error': 'Automovil no encontrado'}), 404


@app.route('/api/automoviles', methods=['POST'])
def create_automovil():
    data = request.json
    automovil = Automovil(marca=data['marca'], modelo=data['modelo'], año=data['año'])
    PersistenciaAutomovil.insertar_automovil(automovil)
    return jsonify({'message': 'Automovil creado', 'id': automovil.get_id()}), 201

##Quiero para actualizar un automovil por id
@app.route('/api/automoviles/<id>', methods=['PUT'])
def update_automovil(id):
    data = request.json
    automovil = PersistenciaAutomovil.recuperar_automovil(id)
    if automovil:
        automovil.set_marca(data['marca'])
        automovil.set_modelo(data['modelo'])
        automovil.set_año(data['año'])
        PersistenciaAutomovil.actualizar_automovil(automovil)
        return jsonify({'message': 'Automovil actualizado'})
    
    return jsonify({'error': 'Automovil no encontrado'}), 404

##El eliminar
@app.route('/api/automoviles/<id>', methods=['DELETE'])
def delete_automovil(id):
    automovil = PersistenciaAutomovil.recuperar_automovil(id)
    if automovil:
        PersistenciaAutomovil.eliminar_automovil(id)
        return jsonify({'message': 'Automovil eliminado'})
    return jsonify({'error': 'Automovil no encontrado'}), 404

app.run(debug=True)