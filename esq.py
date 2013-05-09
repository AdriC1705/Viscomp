import sys
import Image, ImageDraw
import math
import pygame
import numpy as np
from math import *

def imagen():
    img = Image.open("gato.jpg")
    ancho,alto = img.size
    #img = eg(img,ancho,alto)
    return img, ancho, alto
#----------------------------------------------------#
def eg(r,ancho,alto):
    img = Image.open('gato.jpg')
    pixeles = img.load()
    #imageng = 'escg.jpg'
    for i in range (ancho):
        for j in range(alto):
            (r,g,b)= img.getpixel((i,j))
            prom = int((r+g+b)/3)
            pixeles[i,j] = (prom,prom,prom)
    #img.save(imageng)
    #img.save('eg.jpg')
    return img
#----------------------------------------------------#
def filtro_esquinas(img,ancho,alto):
    #pic = Image.open('eg.jpg')
    pixeles = img.load()
    for i in range(ancho):
        for j in range(alto):
            l = []
            (r,g,b) = img.getpixel((i,j))
            try:
                if (pixeles[i+1,j]): #derecha
                        p = pixeles[i+1,j][0]
                        l.append((p))
            except:
                pass
            try: #Izq
                if(pixeles[i-1,j]):
                    p = pixeles[i-1,j][0]
                    l.append((p))
            except:
                pass
            try: #arriba
                if(pixeles[i,j+1]):
                    p = pixeles[i,j+1][0]
                    l.append((p))
            except:
                pass
            try:#abajo
                if(pixeles[i,j-1]):
                    p = pixeles[i,j-1][0]
                    l.append((p))
            except:
                pass
            try:#arriba der
                if(pixeles[i+1,j+1]):
                    p =pixeles[i+1,j+1][0]
                    l.append((p))
            except:
                pass
            try:#arriba izq
                if(pixeles[i-1,j+1]):
                    p =pixeles[i-1,j+1][0]
                    l.append((p))
            except:
                pass
            try: #abajo izq
                if(pixeles[i+1,j-1]):
                    p =pixeles[i+1,j-1][0]
                    l.append((p))
            except:
                pass
            try: #abajo der
                if(pixeles[i-1,j-1]):
                    p =pixeles[i-1,j-1][0]
                    l.append((p))
            except:
                pass
            l.sort()
            print l
            med = int(np.median(l))
            print med
            pixeles[i,j] = (med,med,med)
    #img.save("filtrado.jpg")
    return img
#---------------------------------------------------#
def dif_esq(img,img2,ancho,alto):
    pic = Image.open('eg.jpg')
    pix = pic.load()
    pix2 = img2.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=pic.getpixel((i,j))
            (r,g,b) = img2.getpixel((i,j))
            nw = pix2[i,j][0]
            origi = pix [i,j][0]
            dif = (nw-origi)
            pix[i,j] = (dif,dif,dif)
    return pic
#---------------------------------------------------#
def conv(diferencia,ancho,alto):
    #tiemp = time()
    img = Image.open('dif.jpg')
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
    #im= img.save('conv.png')
    return img
#---------------------------------------------------#    
#---------------------------------------------------#
def main():
    pygame.init()
    r, ancho,alto = imagen()
    esg = eg(r,ancho,alto)
    esg.save('eg.jpg')
    filtro = filtro_esquinas(esg,ancho,alto)
    filtro.save('fil.jpg')
    diferencia = dif_esq(esg,filtro,ancho,alto)
    diferencia.save('dif.jpg')
    convolucion = conv(diferencia,ancho,alto)
    convolucion.save('convi.jpg')
    screen = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Ventana")
    im = pygame.image.load(r)

main()
