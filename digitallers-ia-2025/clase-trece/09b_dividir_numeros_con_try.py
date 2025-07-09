#Un programa en python que divida dos numeros y muestre el resultado
## Version con Try Except

try:
    numero1 = float(input("Ingrese el número a dividir: "))
    numero2 = float(input("Ingrese el divisor: "))
    resultado = numero1 / numero2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
except ValueError:
    print("Error: Entrada no válida. Asegúrese de ingresar números válidos.")