from flask import Flask, jsonify, request

app = Flask("Mi primera APP con Flask")

@app.route('/hello')
def hello():
    return jsonify(message=f'Hola mundo desde Flask!')


@app.route('/saludar')
def saludar():
    #Para invocar este 
    nombre = request.args.get('nombre', 'Invitado')
    return jsonify(message=f'Hola, {nombre}!')

#Quiero que se llame /sumar?num1=5&num2=10
@app.route('/sumar')
def sumar():
    # Obtenemos los números de la URL, por ejemplo: /sumar?num1=5&num2=10
    num1 = request.args.get('num1', 0)
    num2 = request.args.get('num2', 0)
    
    try:
        # Convertimos a enteros
        suma = int(num1) + int(num2)
        return jsonify(result=suma)
    except ValueError:
        return jsonify(error="Por favor envía números válidos."), 400

app.run(debug=True)
