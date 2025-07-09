#Un programa que muestre lo mismo que el usuario igresa hasta que el uuario ingresa un texto vacio
texto = input("Ingrese texto y el programa repite lo que ingresas (o presione Enter para salir): ")
while texto != "":
    print("ECO : " + texto)
    texto = input("")