import pygame
import sys
import random

# Colores
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde1 = (36, 223, 70)
azul1 = (0, 85, 194)
AZUL = random. randint(1, 255)

# Inicialización de Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("El cuadrado que rebota")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables para el cuadrado que se mueve
XX = 300
MOVIMIENTO = 3

# Bucle principal
while True:
    clock.tick(50)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color azul
    ventana.fill(azul)

    # Actualizar la posición del cuadrado que rebota
    XX = XX + MOVIMIENTO

    # Comprobar si el cuadrado rebota
    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    # Dibujar el cuadrado principal (rojo) que se mueve
    color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    pygame.draw.rect(ventana, verde1, (XX, 450, 50, 50))
    pygame.draw.rect(ventana, azul1, (XX, 0, 50, 50))
    pygame.draw.rect(ventana, rojo, (0, XX, 50, 50))
    pygame.draw.rect(ventana, azul1, (450,XX, 50, 50))
    pygame.draw.rect(ventana, color, (200,200, 100, 100))
    pygame.draw.rect(ventana, azul1, (XX,XX, 50, 50))
    # Actualizar la pantalla
    pygame.display.flip()