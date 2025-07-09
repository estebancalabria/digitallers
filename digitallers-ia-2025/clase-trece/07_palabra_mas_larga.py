#Que el usuario ingrese dos palabras y el programa le diga cuál es la más larga.
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
if len(palabra1) > len(palabra2):
    print("La palabra más larga es:", palabra1)
elif len(palabra1) < len(palabra2):
    print("La palabra más larga es:", palabra2)
else:
    print("Ambas palabras tienen la misma longitud.")