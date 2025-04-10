import pygame
import sys
import random
import math

# Colores
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 255)
rosado = (255, 195, 203)
negro = (0,0,0)
naranja = (194, 88, 0)
blanco = (255, 255, 255)
cian = (0, 255, 255)
PI = math.pi

# Inicialización de Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption("dibujar formas con pygame")

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Variables para el cuadrado que se mueve
XX = 300
MOVIMIENTO = 3
###########################
# Bucle principal del juego
###########################
while True:
    clock.tick(50)  # Limita los FPS a 50

    # ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # si s hace click en el boton de cerrar de la ventana, el juego se termina
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # rellenar la ventana de color
    ventana.fill(negro)

    # dibujar fomas con el modulo pygame.draw

    # dibujar una linea
    pygame.draw.line(ventana, rojo, (100, 100), (300, 300))
    pygame.draw.line(ventana, rojo, (100, 100), (300, 100))
    pygame.draw.line(ventana, rojo, (300, 100), (100, 300))
    pygame.draw.line(ventana, rojo, (100, 300), (300, 100))

    # dibujar una linea descontinua
    # true: crea un poligono

    punto2 = ((200, 0), (400, 200), (200, 400), (0, 200))
    pygame.draw.lines(ventana, rojo ,True, punto2)
    puntos3 = ((200, 200), (250,300), (300, 325), (400,350))
    pygame.draw.polygon(ventana, naranja, puntos3, 1)
    # dibujar un rectangulo
    # relleno ubicado en la coordenada 200, 200 y de ancho 200 y altura 100
    pygame.draw.rect(ventana, naranja,((100, 100), (200, 200)), 5)
    # dibujar un circulo
    # centro del circulo: (300, 100)
    # radio del circulo: 100
    # grosor contorno circulo: 1
    pygame.draw.circle(ventana, blanco, (300,100), 30, 5)
    # dibujar una elipse
    pygame.draw.ellipse(ventana, naranja, (100, 150, 200, 100), 5)
    # dibujar un arco de circunferencia
    pygame.draw.arc(ventana, cian, (300,25,180,150),PI/2 , PI,1 )

    # agragar texto
    # estamos creando una fuente de tipo arial con un tamaño de 35 con negrilla y cursiva.
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("sistemas guanenta",1, blanco)
    ventana.blit(texto,(50,50))
    # actualiza la visualisacion del la ventana
    pygame.display.flip()

####################################
# fin del bucle pprincipal del juego
####################################