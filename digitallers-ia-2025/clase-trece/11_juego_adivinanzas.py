# Enunciado
# La PC elegirá un número al azar entre 1 y 100.
# El usuario deberá adivinar el número.
# El usuario tiene 5 intentos para adivinar el número.
# Si el usuario adivina el número, el programa le dirá que ganó.
# Si el usuario no adivina el número y le quedan intentos el programa le dir 
# si el número es mayor o menor al que eligió la PC.
import random

numero_secreto = random.randint(1, 100)
intentos = 5
adivinado = False

while (intentos > 0) and not adivinado:
    intento_usuario = int(input("Adivina el número (entre 1 y 100): "))
    if intento_usuario == numero_secreto:
        print("¡Ganaste!")
        adivinado = True
    elif intento_usuario < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    intentos -= 1

if not adivinado:
    print("Perdiste. El número era:", numero_secreto)