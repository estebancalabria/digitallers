from Persona_Sin_Encapsulamiento import Persona_Sin_Encapsulamiento as PersonaSE
from Persona_Validacion_Constructor import Persona_Validacion_Constructor as PersonaVC
from Persona_Con_Encapsulamiento import Persona_Con_Encapsulamiento as PersonaCE

#Asi todo bien....
persona = PersonaSE("Juan", "Pérez")
persona.mostrar_informacion()

# Que pasa aca? - No Da error peero.. no tiene mucho sentido crear una persona sin nombre y apellido
#persona = PersonaSE("", "")
#persona.mostrar_informacion()

#Voy a Mejorar la clase Persona para que no se pueda crear una persona sin nombre y apellido
persona_valida = PersonaVC("Ana", "Gómez")
persona_valida.mostrar_informacion()

try:
    persona_invalida = PersonaVC("", "")  
except Exception as e:
    print(f"Error al crear una persona con datos incorrectos: {e}`")

#Pero que pasa aca...
#A pesar de que la clase PersonaVC valida los datos al crear una persona,
#no valida si se cambian los atributos directamente.
#persona_temporalmente_valida = PersonaVC("Carlos", "López")
#persona_temporalmente_valida.nombre = ""  # Cambiando el nombre a minúsculas
#persona_temporalmente_valida.mostrar_informacion()

persona_posta = PersonaCE("María", "Fernández")
persona_posta.mostrar_informacion()