

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
    
        # Atributos privados para encapsulamiento
        # Los atributos en python se declaran con __ (doble guión bajo) 
        # para que no se puedan acceder directamente desde fuera de la clase
        # para leerlos se deben usar métodos getter
        # para escribirlos se deben usar métodos setter
        # Python no maneja niveles de acceso como otros lenguajes (public, private, protected)
        # Lo del doble guión bajo es una convención para indicar que el atributo es privado
        self.__nombre = nombre
        self.__apellido = apellido

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Apellido: {self.__apellido}")

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    # Métodos setter
    #def set_nombre(self, nombre):
    #    self.__nombre = nombre

    #def set_apellido(self, apellido):
    #    self.__apellido = apellido