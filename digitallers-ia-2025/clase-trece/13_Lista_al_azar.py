#Generar una lista de 20 numero al azar
import random
lista = []
for i in range(20):
  numero = random.randint(1, 100)
  lista.append(numero)
print(lista)