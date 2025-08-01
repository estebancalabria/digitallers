import re
# Hacer una clase con metods estaticos para validar cadenas (strings)
#Tiene los siguientes metodos:
# es_email
# es_url
# es_numero_entero
# logitud_valida(cadena, minimo, maximo)

class ValidadorCadenas:
    @staticmethod
    def es_email(cadena):
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron_email, cadena) is not None
    
    @staticmethod
    def es_url(cadena):
        patron_url = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}(/\S*)?$'
        return re.match(patron_url, cadena) is not None
    
    @staticmethod
    def es_numero_entero(cadena):
        try:
            int(cadena) 
            return True 
        except ValueError:
            return False 
        
    @staticmethod
    def longitud_valida(cadena, minimo, maximo):
        if not isinstance(cadena, str):
            return False 
        longitud = len(cadena)
        return minimo <= longitud <= maximo