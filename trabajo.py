import pygame
import sys
import random

# Colores
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 255)
rosado = (255, 195, 203)
negro = (0,0,0)
naranja = (194, 88, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)


# Inicialización de Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("trabajo de clase")

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
    ventana.fill(negro)

    # Actualizar la posición del cuadrado que rebota
    XX = XX + MOVIMIENTO

    # Comprobar si el cuadrado rebota
    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    

    inicio = (random.randint(50 , 450), random.randint(150, 400))
    fin = (random.randint(50, 450), random.randint(150, 400))

    # Dibujar el cuadrado principal (rojo) que se mueve
    pygame.draw.line(ventana, blanco, (50, 150), (450, 150), 5)
    pygame.draw.line(ventana, blanco, (50, 400), (450, 400), 5)
    pygame.draw.line(ventana, blanco, (450, 150), (450, 400), 5)
    pygame.draw.line(ventana, blanco, (50, 400), (50, 150), 5)
    
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("colegio san jose de guanenta",1, blanco)
    ventana.blit(texto,(10,10))

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("especialidad de sistemas",1, blanco)
    ventana.blit(texto,(40,70))

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("julian camilo sanchez triana",1, blanco)
    ventana.blit(texto,(20,450))

    for i in range(100):
        
        lo1 = random.randint(50, 450)
        lo2 = random.randint(150, 400)
        lo3 = random.randint(50, 450)
        lo4 = random.randint(150, 400)
        
        
        color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        pygame.draw.line(ventana, color , (lo1, lo2), (lo3, lo4)) 
    
    # Actualizar la pantalla
    pygame.display.flip()