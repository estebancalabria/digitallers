#Generar una lista de 50 numeros al azar
#Luego mostar la lista, el mayor, el menor y el promedio de los numeros
import random
numeros = [random.randint(1, 100) for _ in range(50)]
print("Lista de números:", numeros)
print("Número mayor:", max(numeros))
print("Número menor:", min(numeros))
print("Promedio:", sum(numeros) / len(numeros))