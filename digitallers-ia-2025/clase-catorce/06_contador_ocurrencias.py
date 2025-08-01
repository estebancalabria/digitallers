# El usuario ingresa un texto con varias palabras separadas por espacios.
# Las palabras se almacenan en un diccionario donde la clave es la palabra y el valor es la cantidad de veces que aparece en el texto.
# Mostar el diccionario para ver laa cantnidad de veces que aparece cada palabra en orden alfabético.
# Mostar la palabra que aparece mas veces y la que aparece menos veces.

texto = input("Ingrese un texto: ")
palabras = texto.lower().split()
contador = {}

for palabra in palabras:
    #El metodo Get del diccionario tiene un valor por defecto que se usa si la clave no existe
    contador[palabra] = contador.get(palabra, 0) + 1

print("Cantidad de ocurrencias de cada palabra:")
for palabra, cantidad in sorted(contador.items()):
    print(f"{palabra}: {cantidad}")

#Luego lo vemos mas en detalle cuando veamos referencias
max_palabra = max(contador, key=contador.get)
min_palabra = min(contador, key=contador.get)
print("Palabra que aparece más veces:", max_palabra)
print("Palabra que aparece menos veces:", min_palabra)