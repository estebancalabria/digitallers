#Definir un enumerado que tenga los dias de la semana y mostrarlo por pantalla.

from enum import Enum

class DiasSemana(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    jueves = 4
    viernes = 5
    sabado = 6
    domingo = 7

for dia in DiasSemana:
    print(f"{dia.name}: {dia.value}")