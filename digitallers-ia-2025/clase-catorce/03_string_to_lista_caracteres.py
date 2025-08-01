# Funcion que converta un string en una lista de caracteres
#    # def string_a_lista(string: str) -> list[str]:
# Una funcion que reciba un caracter y una lista de caracteres y devuelva la cantidad de veces que aparece el caracter en la lista
#   # def contar_caracter_en_lista(caracter: str, lista: list[str]) -> int:
# Luego hacer print y probar la función
def string_a_lista(string: str) -> list[str]:
    return list(string)

def contar_caracter_en_lista(caracter: str, lista: list[str]) -> int:
    return lista.count(caracter)

# Probar las funciones
mi_string = "Combocatoria"
mi_lista = string_a_lista(mi_string)

print("Lista de caracteres:", mi_lista)
caracter_a_contar = "a"

cantidad = contar_caracter_en_lista(caracter_a_contar, mi_lista)
print(f"El carácter '{caracter_a_contar}' aparece {cantidad} veces en la lista.")
