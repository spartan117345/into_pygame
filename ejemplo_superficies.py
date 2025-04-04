# importamos la libreria pygame
import pygame
import random

rojo = random.randint(0,255)
verde = random.randint(0,255)
azul = random.randint(0,255)

# informar el numero del color
print("el numero del rojo es: " + str(rojo))
print("el numero del azul es: " + str(azul))
print("el numero del verde es: " + str(verde))

# inicialisamos los modulos de pygame

pygame.init()

# establecer nombre a la ventana
pygame.display.set_caption("surface")

# 
ventana = pygame.display.set_mode((400, 400))

# crear una superficie
color_aleatorio = pygame.Surface((400, 200))

color_aleatorio.fill((rojo, verde, azul))

# inserto o muevo la superficie en la ventana
ventana.blit(color_aleatorio, (0,0))

# actualiza la visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break



pygame.quit()