#Crear un modulo calculadora.py con las operaciones basicas de una calculadora.
#Sumar, restar, multiplicar y dividir.
#Importarlo en otro archivo y probar las funciones.
#Lo hacen ustedes y me lo pasan!
class Calculadora:

    @staticmethod #El @ es un decorador que indica que el método es estático y no necesita una instancia de la clase para ser llamado.
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

def mostrar_info():
    print("Módulo Calculadora")
    print("Funciones disponibles:")
    print("- Sumar")
    print("- Restar")
    print("- Multiplicar")
    print("- Dividir")

def borrar_todo_el_disco():
    print("Borrando todo el disco... (esto es solo un ejemplo, no se ejecutará realmente)")

#Quiero que este modulo tenga todos los metodos pero de alguna manera agruparlos por tematica