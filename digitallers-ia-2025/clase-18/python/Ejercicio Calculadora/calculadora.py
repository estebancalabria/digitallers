#Crear un modulo calculadora.py con las operaciones basicas de una calculadora.
#Sumar, restar, multiplicar y dividir.
#Importarlo en otro archivo y probar las funciones.
#Lo hacen ustedes y me lo pasan!
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b