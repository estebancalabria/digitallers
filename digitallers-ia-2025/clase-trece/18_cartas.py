# Hacer un programa que genere un mazo de cartas españolas y las muestre por pantalla.
# El enumerado de palos ya está creado en el ejercicio anterior.
# El diccionario de carta también.
# La lista de cartas debe contener 40 cartas, 10 por palo.
from enum import Enum
class Palo(Enum):
    OROS = "Oros"
    COPAS = "Copas"
    ESPADAS = "Espadas"
    BASTOS = "Bastos"

cartas_por_palo = {
    palo: [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    for palo in Palo
}

mazo = [(valor, palo.value) for palo in Palo for valor in cartas_por_palo[palo]]

for carta in mazo:
  print(carta)