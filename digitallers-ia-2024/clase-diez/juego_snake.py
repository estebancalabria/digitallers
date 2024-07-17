import pygame
import random

# Inicializar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
TAMANO_CELDA = 20

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Snake')

# Clase Snake
class Snake:
    def __init__(self):
        self.cuerpo = [(ANCHO // 2, ALTO // 2)]
        self.direccion = pygame.K_RIGHT

    def mover(self):
        x, y = self.cuerpo[0]
        if self.direccion == pygame.K_UP:
            y -= TAMANO_CELDA
        elif self.direccion == pygame.K_DOWN:
            y += TAMANO_CELDA
        elif self.direccion == pygame.K_LEFT:
            x -= TAMANO_CELDA
        elif self.direccion == pygame.K_RIGHT:
            x += TAMANO_CELDA
        self.cuerpo.insert(0, (x, y))

    def crecer(self):
        self.cuerpo.append(self.cuerpo[-1])

    def dibujar(self):
        for segmento in self.cuerpo:
            pygame.draw.rect(pantalla, VERDE, (segmento[0], segmento[1], TAMANO_CELDA, TAMANO_CELDA))

# Clase Comida
class Comida:
    def __init__(self):
        self.posicion = self.generar_posicion()

    def generar_posicion(self):
        x = random.randint(0, (ANCHO - TAMANO_CELDA) // TAMANO_CELDA) * TAMANO_CELDA
        y = random.randint(0, (ALTO - TAMANO_CELDA) // TAMANO_CELDA) * TAMANO_CELDA
        return (x, y)

    def dibujar(self):
        pygame.draw.rect(pantalla, ROJO, (self.posicion[0], self.posicion[1], TAMANO_CELDA, TAMANO_CELDA))

# Inicializar objetos
snake = Snake()
comida = Comida()

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Bucle principal del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                snake.direccion = evento.key

    # Mover la serpiente
    snake.mover()

    # Comprobar colisión con la comida
    if snake.cuerpo[0] == comida.posicion:
        snake.crecer()
        comida = Comida()

    # Comprobar colisión con los bordes
    x, y = snake.cuerpo[0]
    if x < 0 or x >= ANCHO or y < 0 or y >= ALTO:
        jugando = False

    # Comprobar colisión con sí misma
    if snake.cuerpo[0] in snake.cuerpo[1:]:
        jugando = False

    # Dibujar
    pantalla.fill(NEGRO)
    snake.dibujar()
    comida.dibujar()
    pygame.display.flip()

    # Controlar la velocidad del juego
    reloj.tick(10)

# Finalizar Pygame
pygame.quit()