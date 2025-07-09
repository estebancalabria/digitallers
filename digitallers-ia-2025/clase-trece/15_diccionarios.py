# Crear un diccionario que contenga los datos de una persona, incluyendo su nombre, edad y ciudad.
# Luego mostrarlo por pantalla
# Los diccionarios en Python se definen con llaves {}
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Buenos Aires"
}
print(persona)

#Accedo a los valores del diccionario usando las llaves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"]) 

#Recorrer el diccionario con un for
for clave, valor in persona.items():
    print(f"{clave}: {valor}")