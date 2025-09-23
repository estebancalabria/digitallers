from flask import Flask, request

print("Creando mi primera API REST con Flask " + __name__)
app = Flask(__name__)  ##Creo un objeto o instancia de Flas

@app.route("/")  ##Decorador que indica la ruta de acceso
def hola_mundo():
    return "Hola Mundo!"  ##Retorna un string

@app.route("/saludar")  ##Otra ruta de acceso
def saludar():
    nombre = request.args.get("nombre", "Desconcido")  ##Obtiene el parámetro 'nombre' de la URL, si no existe usa "Mundo"
    return "Hola " + nombre + "!"  ##Retorna un string



app.run(debug=True)  ##Ejecuta la aplicación en modo de depuración