from PIL import Image #esto para trabajar con imagenes
import sys
import pygame


#definimos constantes para la ventana :)

ancho = 600
alto = 600

def main ():
    pygame.init()
    pygame.display.set_caption("Ventana")
    screen = pygame.display.set_mode((ancho,alto), 0, 32)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

if __name__ == '__main__':
    main()


