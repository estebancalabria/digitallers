import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definir dimensiones de la ventana
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Saltar Obstáculos")

# Definir dimensiones del jugador y los obstáculos
player_width = 50
player_height = 50
player_x = 50
player_y = HEIGHT - player_height
player_speed = 10
jump_height = 15
gravity = 1

obstacle_width = 50
obstacle_height = 50
obstacle_speed = 10

# Inicializar variables del juego
is_jumping = False
jump_velocity = jump_height
obstacles = []
score = 0

# Configurar el reloj
clock = pygame.time.Clock()

# Fuente para mostrar puntaje
font = pygame.font.Font(None, 36)

# Función para dibujar al jugador
def draw_player(x, y):
    pygame.draw.rect(window, WHITE, (x, y, player_width, player_height))

# Función para dibujar un obstáculo
def draw_obstacle(obstacle):
    pygame.draw.rect(window, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

# Función para mostrar el puntaje
def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

# Bucle principal del juego
running = True
while running:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        jump_velocity = jump_height
    
    if is_jumping:
        player_y -= jump_velocity
        jump_velocity -= gravity
        if player_y >= HEIGHT - player_height:
            player_y = HEIGHT - player_height
            is_jumping = False

    if random.randint(1, 30) == 1:
        obstacles.append([WIDTH, HEIGHT - obstacle_height])

    for obstacle in obstacles[:]:
        obstacle[0] -= obstacle_speed
        if obstacle[0] < -obstacle_width:
            obstacles.remove(obstacle)
            score += 1
        if (player_x < obstacle[0] + obstacle_width and
            player_x + player_width > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and
            player_y + player_height > obstacle[1]):
            running = False

    draw_player(player_x, player_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle)

    show_score()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
