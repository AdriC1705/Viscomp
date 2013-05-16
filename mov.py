import sys
import Image, ImageDraw
import math
import random
import pygame
from math import *
from PIL import Image
import cv # Para Obtener Imagenes desde la camara

#--------------------------------------Imagen 1------------
def imagen1():
    cam = cv.CaptureFromCAM(0)
    while True:
        img = cv.QueryFrame(cam)
        snapshot = img
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("Img1.jpg",img)
        imagen = cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        break
    #return img
#--------------------------------------Imagen 2------------
def imagen2():
    cam = cv.CaptureFromCAM(0)
    while True:
        img = cv.QueryFrame(cam)
        snapshot = img
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("Img2.jpg",img)
        imagen = cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        break
    #return img
#--------------------Escala de Grises-----------------------
def escg(img,ancho,alto):
    pixeles = img.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = img.getpixel((i,j))
            prom = int((r+g+b)/3)
            pixeles[i,j] = (prom,prom,prom)
    
    return img
#------------------------Filtro-----------------------------
def filtro(img,ancho,alto):
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
    return img
#-------------------------Convolucion----------------------
def conv(img,ancho,alto):
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
    return img
#------------------------Binarizacion-----------------------
def binarizacion(img,ancho,alto):
    z= random.randint(0,100)
    pixel=img.load()
    for i in range (ancho):
        for j in range(alto):
            (r,g,b)=img.getpixel((i,j))
            prom = (r+g+b)/3
            if (prom > z):
                pixel[i,j]= (255,255,255)
            else:
                pixel[i,j] = (0,0,0)
    return img
#--------------------------Diferencias----------------------
def diferencia(img1,img2):
    ancho,alto = foto.size
    ancho,alto = foto2.size
    foto3 = Image.new("RGB",(ancho1,alto1))
    pix = foto.load()
    pixel = foto2.load()
    pixeles = foto3.load()
    for i in range(alto-1):
        for j in range(ancho-1):
            diferen = abs(pixeles[i,j][0] - pixeles2[i,j][0])
            if diferen != 0:
                pixeles3[i,j] = (255,255,255)
            else:
                pixeles3[i,j] = (0,0,0)
    #foto3.save('difer.jpg')
    return foto3
#----------------------------------------------------------
def mov(img1,img2):
    ancho,alto = foto.size
    ancho,alto = foto2.size
    foto3 = Image.new("RGB",(ancho1,alto1))
    pix = foto.load()
    pixel = foto2.load()
    pixeles = foto3.load()
    for i in range(alto-1):
        for j in range(ancho-1):
            diferen = abs(pixeles[i,j][0] - pixeles2[i,j][0])
            if diferen != 0:
                pixeles3[i,j] = (255,255,255)
            else:
                pixeles3[i,j] = (0,0,0)
    return foto3
#----------------------------------------------------------    

#-----------------------------------------------------------
def main():
    f= 0
    print "Presione 1 para tomar fotos"
    r = str(raw_input('tomar foto 1:'))
    if r == "1":
        #imagen1()
        f+=1
    r = str(raw_input('tomar foto 2:'))
    if r =="1":
        #imagen2()
        f+=1
    if f==2:
        print 'procesando imagenes'
    #---------Imagen 1    
        img1 = Image.open('Img1.jpg')
        ancho,alto = img1.size
        escala =escg(img1,ancho,alto)
        escala.save('eg1.jpg')
        fil = filtro(escala,ancho,alto)
        fil.save('fil1.jpg')
        convol = conv(fil,ancho,alto)
        convol.save('conv1.jpg')
        binar1 = binarizacion(convol,ancho,alto)
        binar1.save('bin1.jpg')
    #---------Imagen 2
        img2 = Image.open('Img2.jpg')
        ancho,alto = img2.size
        escala =escg(img2,ancho,alto)
        escala.save('eg2.jpg')
        fil = filtro(escala,ancho,alto)
        fil.save('fil2.jpg')
        convol = conv(fil,ancho,alto)
        convol.save('conv2.jpg')
        binar2 = binarizacion(convol,ancho,alto)
        binar2.save('bin2.jpg')           
     #---------Diferencia
        dife = diferencia(binar1,binar2)
        dife.save('diferencia.jpg')
        movim = mov(dife,bin1)
        movim.save('Movimiento.jpg')
        
    else:
        print 'no existen las imagenes'
    
main()
