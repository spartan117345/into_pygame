import pygame
import random

# Inicialización
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego 2D con Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Jugador
player_size = 50
player_pos = [WIDTH//2, HEIGHT - player_size]
player_speed = 5

# Enemigos
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
enemy_speed = 5

# Reloj
clock = pygame.time.Clock()

# Puntuación
score = 0
font = pygame.font.SysFont("Arial", 30)

def detectar_colision(jugador, enemigo):
    px, py = jugador
    ex, ey = enemigo
    return (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and \
           (ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size)

# Bucle principal
running = True
while running:
    clock.tick(30)
    win.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Movimiento enemigo
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1

    # Dibujar jugador y enemigo
    pygame.draw.rect(win, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(win, RED, (*enemy_pos, enemy_size, enemy_size))

    # Colisiones
    if detectar_colision(player_pos, enemy_pos):
        print("¡Game Over! Puntuación:", score)
        running = False

    # Mostrar puntuación
    text = font.render(f"Puntos: {score}", True, (0, 0, 0))
    win.blit(text, (10, 10))

    # Actualizar pantalla
    pygame.display.update()

pygame.quit()