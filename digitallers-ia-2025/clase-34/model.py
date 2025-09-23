
import uuid


class Automovil:
    #Este cuando creo un objeto que viene de la base de datos y ya tiene id
    def __init__(self, marca, modelo, año, id=None):
        # Si no viene un id (caso objeto nuevo), genero uno
        self.__id = id if id else str(uuid.uuid4())
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    # Getters
    def get_id(self):
        return self.__id
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_año(self):
        return self.__año
    
    # Setters
    def set_id(self, id):
        self.__id = id
    def set_marca(self, marca):
        self.__marca = marca
    def set_modelo(self, modelo):
        self.__modelo = modelo
    def set_año(self, año):
        self.__año = año

    def __str__(self):
        return f"Automóvil(ID: {self.__id}, Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año})"