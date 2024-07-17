import random

def leer_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar el número de intentos
intentos = 6
adivino = False

print("Bienvenido al juego de adivinanza!")
print("He pensado un número entre 1 y 100. Tienes 6 intentos para adivinarlo.")

# Bucle principal del juego
while (intentos > 0) and (not adivino):
    # Pedir al jugador que adivine
    adivinanza = leer_numero_entero(f"\nTe quedan {intentos} intentos. Ingresa tu número: ")

    # Comprobar la adivinanza
    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto}.")
        adivino = True
    elif adivinanza < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

    # Reducir el número de intentos
    intentos -= 1

# Si se agotan los intentos
if not adivino:
    print(f"\nGame Over. El número secreto era {numero_secreto}.")