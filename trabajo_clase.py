import pygame
import sys

rojo = (255, 0, 0)
azul = (0, 0, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

cuadrado_superficie = pygame.Surface((50, 50))

cuadrado_superficie.fill(rojo)

cuadrado_superficie_2 = pygame.Surface((50, 50))

ventana.blit(cuadrado_superficie_2, (50, 50))

cuadrado_superficie_3 = pygame.Surface((50, 50))

ventana.blit(cuadrado_superficie_3, (450, 225))

cuadrado_superficie_4 = pygame.Surface((50, 50))

ventana.blit(cuadrado_superficie_4, (0, 225))

cuadrado_superficie_4.fill(rojo)

pygame.display.set_caption("el cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

ventana.fill(azul)

XX = XX + MOVIMIENTO

    

if XX >= 420:
    XX = 420
    MOVIMIENTO = -3
elif XX <= 0:
    XX = 0
    MOVIMIENTO = 3

pygame.draw.rect(ventana, rojo, (XX, 200, 80, 80))
pygame.display.flip()

cuadrado_superficie.fill(rojo)

cuadrado_superficie_2.fill(rojo)

cuadrado_superficie_3.fill(rojo)

cuadrado_superficie_4.fill(rojo)