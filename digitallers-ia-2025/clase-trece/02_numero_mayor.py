# Que le pregunte al usuario dos numeros y le diga cual es el mayor
# Pregunte al usuario 2 números y muestre el mayor de los 2.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Los números son iguales.")