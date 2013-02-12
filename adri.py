import Image #esto para trabajar con imagenes
import sys
import pygame
import math
from time import *

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
    imageng = 'escg.jpg'
    for i in range (ancho):
        for j in range(alto):
            (r,g,b)= img.getpixel((i,j))
            prom = int((r+g+b)/3)
            #Aqui agregamos umbrales
            pixeles[i,j] = (prom,prom,prom)
    img.save(imageng)
    filtro(img,ancho,alto)
    conv(img,ancho,alto)
    return imageng

def filtro(img,ancho,alto):
    tiemp= time()
    pixel =img.load() 
    for i in range (ancho):
        for j in range(alto):
            c = 0
            prom = 0.0
            try:
                if(pixel[i+1,j]):
                    prom += pixel[i+1,j][0]
                    c +=1
            except:
                prom += 0
            try:
                if(pixel[i-1,j]):
                    prom += pixel[i-1,j][0]
                    c +=1
            except:
                prom += 0
            try:
                if(pixel[i,j+1]):
                    prom += pixel[i,j+1][0]
                    c+=1
            except:
                prom += 0
            try:
                if(pixel[i,j-1]):
                    prom += pixel[i,j-1][0]
                    c+=1
            except:
                prom += 0
            
            promt = int(prom/c)
            pixel[i,j] = (promt, promt, promt)
    im=img.save ('filtro.jpg')
    timei=time()
    timef= timei - tiemp
    print "Tiempo de ejecucion del filtro: "+str(timef)+"segundos"

def conv(img,ancho,alto):
    tiemp = time()
    pixels =img.load()
    matrizX =([-1,0,1],[-2,0,2],[-1,0,1])
    matrizY =([1,2,1],[0,0,0],[-1,-2,-1])
    
    for i in range(ancho):
        for j in range(alto):
            sumx = 0
            sumy = 0
            a=3
            for x in range(a):
                for y in range(a):
                    try:
                        sumx +=(pixels[x+i,y+j][0]*matrizX[x][y])
                        sumy += (pixels[x+i,y+j][0]*matrizY[x][y])
                    except:
                        pass
            
            grad = math.sqrt(pow(sumx,2)+pow(sumy,2))
            grad = int(grad)
            pixels[i,j] = (grad,grad,grad)
    im= img.save('conv.jpg')
    timei=time()
    timef= timei - tiemp
    print "Tiempo de ejecucion deteccion de bordes: "+str(timef)+"segundos"


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
