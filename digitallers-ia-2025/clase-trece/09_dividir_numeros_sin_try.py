#Un programa en python que divida dos numeros y muestre el resultado
## Version Sin Try Except

numero1 = float(input("Ingrese el número a dividir: "))
numero2 = float(input("Ingrese el divisor: "))
if numero2 != 0:
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)
else:
    print("Error: División por cero no permitida.")

