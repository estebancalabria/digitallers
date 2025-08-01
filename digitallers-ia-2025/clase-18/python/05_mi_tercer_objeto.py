#Crear una clase que represente un numero fraccionario con numerador y denominador 
#debe incluir un metodo para sumar dos fracciones y otro para multiplicar dos fracciones
#tambien debe incluir un metodo para convertir la fraccion a decimal

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar(self, otra):
        nuevo_numerador = (self.numerador * otra.denominador) + (otra.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, otra):
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def a_decimal(self):
        return self.numerador / self.denominador