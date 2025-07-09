#Generar una lista de 20 numero al azar por compresion
import random
numeros = [random.randint(1, 100) for _ in range(20)]
print(numeros)