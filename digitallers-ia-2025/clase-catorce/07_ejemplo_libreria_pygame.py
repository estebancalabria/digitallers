import pygame
import sys

# Inicializar pygame
pygame.init()

# Crear ventana (ancho x alto)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hola Mundo con Pygame")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Crear fuente y renderizar texto
fuente = pygame.font.SysFont(None, 48)
texto = fuente.render("Hola Mundo", True, NEGRO)

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Rellenar fondo
    screen.fill(BLANCO)
    
    # Dibujar texto en la pantalla (centrado)
    rect_texto = texto.get_rect(center=(320, 240))
    screen.blit(texto, rect_texto)
    
    # Actualizar pantalla
    pygame.display.flip()
