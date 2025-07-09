# Crear un enumerado que represente el palo de una baraja de cartas española (oros, copas, espadas, bastos) y mostrarlo por pantalla.
# Crear un diccionario que represente una carta

from enum import Enum

class Palo(Enum):
    OROS = 1
    COPAS = 2
    ESPADAS = 3
    BASTOS = 4

carta = {
    "numero": 7,
    "palo": Palo.OROS
}

print(carta)
