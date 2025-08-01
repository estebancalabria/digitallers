
class Persona_Sin_Encapsulamiento:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}")