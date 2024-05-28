import random

# Constantes
ANCHO_TABLERO = 10
ALTO_TABLERO = 10
LONGITUD_INICIAL_VIBORA = 5

# Inicializar tablero
tablero = [[' ' for _ in range(ANCHO_TABLERO)] for _ in range(ALTO_TABLERO)]

# Inicializar vibora
vibora = [(ANCHO_TABLERO // 2, ALTO_TABLERO // 2) for _ in range(LONGITUD_INICIAL_VIBORA)]

# Inicializar dirección de la vibora
direccion = (1, 0)  # derecha

# Inicializar comida
comida = (random.randint(0, ANCHO_TABLERO - 1), random.randint(0, ALTO_TABLERO - 1))
while comida in vibora:
    comida = (random.randint(0, ANCHO_TABLERO - 1), random.randint(0, ALTO_TABLERO - 1))

# Función para dibujar el tablero
def dibujar_tablero():
    for y in range(ALTO_TABLERO):
        for x in range(ANCHO_TABLERO):
            if (x, y) in vibora:
                print('O', end=' ')
            elif (x, y) == comida:
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print()

# Bucle principal del juego
while True:
    # Dibujar tablero
    dibujar_tablero()

    # Leer entrada del usuario
    entrada = input("Ingrese una dirección (W/A/S/D): ")

    # Actualizar dirección de la vibora
    if entrada.upper() == 'W':
        direccion = (0, -1)
    elif entrada.upper() == 'S':
        direccion = (0, 1)
    elif entrada.upper() == 'A':
        direccion = (-1, 0)
    elif entrada.upper() == 'D':
        direccion = (1, 0)

    # Mover vibora
    cabeza_vibora = vibora[0]
    nueva_cabeza = (cabeza_vibora[0] + direccion[0], cabeza_vibora[1] + direccion[1])
    vibora.insert(0, nueva_cabeza)

    # Comprobar si la vibora se come a sí misma
    if nueva_cabeza in vibora[1:]:
        print("Game over!")
        break

    # Comprobar si la vibora come la comida
    if nueva_cabeza == comida:
        comida = (random.randint(0, ANCHO_TABLERO - 1), random.randint(0, ALTO_TABLERO - 1))
        while comida in vibora:
            comida = (random.randint(0, ANCHO_TABLERO - 1), random.randint(0, ALTO_TABLERO - 1))
    else:
        vibora.pop()

    # Comprobar si la vibora sale del tablero
    if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO_TABLERO or
            nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO_TABLERO):
        print("Game over!")
        break