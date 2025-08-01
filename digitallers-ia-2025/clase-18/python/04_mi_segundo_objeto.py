#Crear una clase en python que repesente un automovil y crear dos instancias de ese automovil.
#Osea dos objetos automovil.
#Este lo hacen ustedes y me lo pasan!
class Automovil:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")

# Crear dos objetos automovil
auto1 = Automovil("Toyota", "Corolla", 2020, "Rojo")
auto2 = Automovil("Ford", "Fiesta", 2018, "Azul")
auto1.mostrar_info()
print("---")
auto2.mostrar_info()