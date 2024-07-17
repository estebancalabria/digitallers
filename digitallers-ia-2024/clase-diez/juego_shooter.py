import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter 2D")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Jugador
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Proyectil
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Enemigos
enemy_width = 50
enemy_height = 50
enemy_speed = 2
enemies = []

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Reloj
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Mover jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Mover y eliminar proyectiles
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Generar enemigos
    if len(enemies) < 5 and random.randint(1, 60) == 1:
        enemies.append([random.randint(0, WIDTH - enemy_width), 0])

    # Mover enemigos
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Detectar colisiones
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet[0] < enemy[0] + enemy_width and
                bullet[0] + bullet_width > enemy[0] and
                bullet[1] < enemy[1] + enemy_height and
                bullet[1] + bullet_height > enemy[1]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # Dibujar
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Mostrar puntuación
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()