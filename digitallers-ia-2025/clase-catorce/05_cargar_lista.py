# Preguntarle al usuario palabras e ir cargandola en una lista hasta que ingrese <ENTER>
# Luego mostrar la lista y pedir al usuario un numero para mostrar la palabra en esa posición de la lista.
# Si el numero es incorrecto se lanza una excepción y se muestra un mensaje de error.
# En este caso tratar las excepciones: 
# * ValueError (ej int("hola"))
# * IndexError

def pedir_palabras_y_mostrar():
    palabras = []
    
    #while True:
    #    palabra = input("Introduce una palabra (ENTER para terminar): ").strip()
    #    if palabra == "":
    #        break  #Rompe el bucle si se ingresa una línea vacía
    #    palabras.append(palabra)

    #SIn el break porque cuando el profe estudiaba lo reprobaban si usaba break
    while (palabra := input("Introduce una palabra (ENTER para terminar): ").strip()) != "":
        palabras.append(palabra)

    print("\nLista de palabras:", palabras)

    try:
        indice = int(input("Introduce la posición que quieres ver (empieza en 0): "))
        print(f"La palabra en la posición {indice} es: {palabras[indice]}")
    except ValueError:
        print("Error: debes ingresar un número entero.")
    except IndexError as e:
        print(f"Error: {e}. Elige un número entre 0 y {len(palabras)-1}.")
        
pedir_palabras_y_mostrar()