from flask import Flask, request, jsonify

print("Creando mi primera API REST con Flask " + __name__)
app = Flask(__name__)  ##Creo un objeto o instancia de Flas

personas = []

@app.route("/personas", methods=["GET"])  ##Otra ruta de acceso
def get_personas():
    return jsonify(personas)

##Obtengo persona por id
@app.route("/personas/<int:id>", methods=["GET"])
def get_persona(id):
    persona = next((p for p in personas if p["id"] == id), None)
    if persona:
        return jsonify(persona)
    return jsonify({"error": "Persona no encontrada"}), 404

@app.route("/personas", methods=["POST"])  ##Otra ruta de acceso
def add_persona():
    data = request.get_json()  ##Obtiene el JSON del cuerpo de la solicitud

    # Validar que tenga nombre y apellido
    if "nombre" not in data or "apellido" not in data:
        return jsonify({"error": "Falta nombre o apellido"}), 400  ##Retorna un error 400 (Solicitud incorrecta)

    nueva_persona = {
        "id": len(personas) + 1,
        "nombre": data["nombre"],
        "apellido": data["apellido"]
    }

    personas.append(nueva_persona)

    return jsonify(nueva_persona), 201  ##Retorna el JSON de la nueva persona y un código de estado 201 (Creado)

app.run(debug=True)  ##Ejecuta la aplicación en modo de depuración