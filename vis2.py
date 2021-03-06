import Image #esto para trabajar con imagenes
import sys
import pygame


#definimos

minimo = 100
maximo = 200

#cargamos y abrimos imagen
def imagen():
    img = Image.open("dori.jpg")
    ancho,alto = img.size
    img = eg(img,ancho,alto)
    return img, ancho, alto
    
def eg(img,ancho,alto):
    pixeles = img.load()
    imageng = 'dori_umb.bmp'
    for i in range (ancho):
        for j in range(alto):
            (r,g,b)= img.getpixel((i,j))
            prom = int((r+g+b)/3)
            #Aqui agregamos umbrales
            if prom <= minimo:
                prom =0
            if prom >= maximo:
                prom = 255
            
            pixeles[i,j] = (prom,prom,prom)
    img.save(imageng)
    return imageng

def main ():
    pygame.init()
    #pygame.display.set_caption("Ventana")
    r,ancho,alto = imagen()
    screen = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Ventana")
    im = pygame.image.load(r)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screen.blit(im,(0,0))
        pygame.display.update()
    return 0

main()

