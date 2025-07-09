#Un programa que lea la entrada del usuario y valide que sea un número entero.
numero = input("Introduce un número entero: ")
try:
    # LA siguiente linea puede lanzar una excepción si la entrada no es un número entero
    numero = int(numero) 
    print("Es un numero.")
except ValueError:
    print("La entrada no es un número entero.")