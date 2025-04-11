import pygame
import sys
import random

# Colores
amarillo = (187, 173, 4)
amarilo_oscuro = (142, 130, 10 )
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 255)
rosado = (255, 195, 203)
negro = (0,0,0)
naranja = (194, 88, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
gris = (118, 120, 119)
gris_oscuro = (80, 81, 81)
gris_mas_oscuro = (58,59,58)
gris_claro = (198, 200, 199)
boca = (197, 71, 56)
morado = (145, 74, 201 )
cafe = (91, 10, 10 )
# Inicialización de Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("chu chu")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables para el cuadrado que se mueve
XX = 300
MOVIMIENTO = 3

# Bucle principal
while True:
    clock.tick(10)  # Limita los FPS a 50

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Llenar la ventana con color azul
    ventana.fill(rojo)

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
    pygame.draw.rect(ventana, blanco, (50, 140, 400, 250))
    
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("colegio san jose de guanenta",1, negro)
    ventana.blit(texto,(10,10))

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("especialidad de sistemas",1, negro)
    ventana.blit(texto,(40,70))

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("julian camilo sanchez triana",1, negro)
    ventana.blit(texto,(20,450))
    pygame.draw.rect(ventana, gris, (450, XX, 50, 50))

    for i in range(10):
        color_aleatorio = (random.randint(1, 255), random.randint(1,255), random.randint(1,255))
        pygame.draw.circle(ventana,morado, (140, 300), 40 )# circulo de la parte delantera
        pygame.draw.rect(ventana, verde, (150, 250, 150, 100))# cuadrado principal
        pygame.draw.rect(ventana, azul, (120, 260, 30, 80)) # rectangulo al lado del rectangulo principal en el frente
        pygame.draw.rect(ventana, azul, (120, 250, 20, 100)) # rectangulo que esta al lado del circulo frontal
        pygame.draw.rect(ventana, azul, (165, 200, 30, 50)) # rectangulo de el tubo de la chimenea
        pygame.draw.rect(ventana, azul, (160, 200, 40, 20)) # rectangulo en la punta de la chimenea
        pygame.draw.rect(ventana, azul, (220, 190, 70, 60)) # rectangulo de la cabina
        pygame.draw.circle(ventana, color_aleatorio, (175, 350), 25) # rueda delantera
        pygame.draw.circle(ventana, color_aleatorio, (229, 350), 25) # rueda del centro
        pygame.draw.circle(ventana, color_aleatorio, (283, 350), 25) # rueda trasera
        pygame.draw.rect(ventana, negro, (185, 345, 30, 15)) # el rectangulo entre las dos primeras ruedas
        pygame.draw.rect(ventana, negro, (245, 345, 30, 15)) # rectangulo entre las dos ultimas ruedas
        pygame.draw.rect(ventana, gris_claro, (230, 200, 50, 40 )) # rectangulo central de la cabina
        pygame.draw.rect(ventana, morado, (210,170, 90, 20)) # rectangulo grande del techo
        pygame.draw.rect(ventana, morado, (220,150, 70,20 )) # rectangulo pequeño del techo
        pygame.draw.circle(ventana, color_aleatorio, (255, 220,), 25) # cara del matacho
        pygame.draw.circle(ventana, blanco, (246, 217), 7) # ojo izquierdo del matacho
        pygame.draw.circle(ventana, blanco, (266,217), 7) # ojo derecho del matacho
        pygame.draw.circle(ventana, boca, (254,235), 7) # boca del matacho
        pygame.draw.circle(ventana, negro, (246, 217), 4) # pupila izquierdo del matacho
        pygame.draw.circle(ventana, negro, (266, 217), 4) # pupila derecho del matacho
        pygame.draw.line(ventana, amarilo_oscuro,(260, 209),(270,205),3) # ceja derecha del matacho
        pygame.draw.line(ventana, amarilo_oscuro, (240,205),(250,209),3) # ceja izquierda del matacho
        pygame.draw.rect(ventana, negro, (XX,234, 22, 4))
        pygame.draw.rect(ventana, cafe, (XX,234, 18, 4))
     
    # Actualizar la pantalla
    pygame.display.flip()