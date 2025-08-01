# Quiero las siguientes funciones:
# 1 Generar un una lista de numeros aleatorios entre 1 y 100 recibiendo como parámetro la cantidad de números a generar
#      generar_lista_aleatoria(cantidad: int) -> list[int]:
# 2 una funcion que reciba una lista y devuelva una lista con el maximo y el minimo de la lista
#      obtener_lista_maximo_minimo(lista: list[int]) -> list[int]:
# 3 una funcion que reciba una lista y devuleva un diccionario con el maximo y el minimo de la lista
#      obtener_diccionario_maximo_minimo(lista: list[int]) -> dict[str, int]:
# 4 una funcion que reciba una lista y devuelva una tupla con el maximo y el minimo de la lista
#       obtener_tupla_maximo_minimo(lista: list[int]) -> tuple[int, int]:
# Luego hacer priunt y probar las funciones
# Una tupla es como una lista, pero inmutable, es decir, no se puede modificar una vez creada.

import random

def lista_aleatoria(cantidad):
  #sintaxis de comprensión de listas
  return [random.randint(1,100) for _ in range(cantidad)]

def lista_aleatoria_sin_comprension(cantidad):
    lista = []
    for _ in range(cantidad):
        lista.append(random.randint(1, 100))
    return lista

def obtener_lista_maximo_minimo(lista: list[int]):
  return [max(lista), min(lista)]

def obtener_diccionario_maximo_minimo(lista: list[int]):
   return {"maximo": max(lista), "minimo": min(lista)}

def obtener_tupla_maximo_minimo(lista: list[int]):
  return (max(lista), min(lista))

numeros = lista_aleatoria(10)
print("Lista aleatoria:", numeros)
print("Máximo y mínimo en lista:", obtener_lista_maximo_minimo(numeros))
print("Máximo y mínimo en diccionario:", obtener_diccionario_maximo_minimo(numeros))
print("Máximo y mínimo en tupla:", obtener_tupla_maximo_minimo(numeros))