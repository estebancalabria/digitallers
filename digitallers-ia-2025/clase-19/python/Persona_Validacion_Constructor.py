
class Persona_Validacion_Constructor:
    def __init__(self, nombre, apellido):
        if not nombre or not apellido:
            raise ValueError("Nombre y apellido son obligatorios")
        
        if not isinstance(nombre, str) or not isinstance(apellido, str):
            raise TypeError("Nombre y apellido deben ser cadenas de texto")
        
        if len(nombre) == 0 or len(apellido) == 0:
            raise ValueError("Nombre y apellido no pueden estar vacíos")
        
        if len(nombre) > 50 or len(apellido) > 50:
            raise ValueError("Nombre y apellido no pueden exceder los 50 caracteres")
        
        if not nombre.isalpha() or not apellido.isalpha():
            raise ValueError("Nombre y apellido solo pueden contener letras del alfabeto")
        
        if not nombre[0].isupper() or not apellido[0].isupper():
            raise ValueError("El nombre y el apellido deben comenzar con una letra mayúscula")
    

        self.nombre = nombre
        self.apellido = apellido

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}")