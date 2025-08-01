
class Persona:
    pass

#En python las atributos de un objeto se pueden definir de forma dinámica
persona = Persona()  # Creación de un objeto persona mediante su constructor
persona.nombre = "Juan"
persona.apellido = "Pérez"
persona.edad = 30

print(f"Hola, me llamo {persona.nombre} {persona.apellido}. de {persona.edad} años.")

#Convertir un objeto a un diccionario
dict_persona = persona.__dict__
print(dict_persona)  # Imprime los atributos del objeto como un diccionario

#OTra forma de obtener los atributos de un objeto
dict_persona_2 = vars(persona)
print(dict_persona_2)  # Imprime los atributos del objeto como un diccionario