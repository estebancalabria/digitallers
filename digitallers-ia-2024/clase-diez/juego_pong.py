import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paletas
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
left_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Pelota
BALL_SIZE = 10
BALL_BASE_SPEED = 5
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_BASE_SPEED * random.choice((1, -1))
ball_speed_y = BALL_BASE_SPEED * random.choice((1, -1))

# Puntuación
score_left = 0
score_right = 0
font = pygame.font.Font(None, 36)

# Velocidad de las paletas
PADDLE_SPEED = 7

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de las paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_a] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisiones con los bordes superior e inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Colisiones con las paletas
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Puntuación
    if ball.left <= 0:
        score_right += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    elif ball.right >= WIDTH:
        score_left += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Dibujo
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Mostrar puntuación
    score_surface = font.render(f"{score_left} - {score_right}", True, WHITE)
    screen.blit(score_surface, (WIDTH//2 - score_surface.get_width()//2, 20))

    pygame.display.flip()
    clock.tick(60)