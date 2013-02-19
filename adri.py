import Image #esto para trabajar con imagenes
import sys
import pygame
import math
from time import *
import random
import ImageDraw

#definimos

minimo = 127
maximo = 200

#cargamos y abrimos imagen
def imagen():
    img = Image.open("figs.jpg")
    img2= Image.open("figs.jpg")
    ancho,alto = img.size
    img = eg(img,ancho,alto,img2)
    return img, ancho, alto
    
def eg(img,ancho,alto,img2):
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
    ruido(img2,ancho,alto)
    byeruido(img2,ancho,alto)
    binarizacion(img,ancho,alto)
    formas(img,ancho,alto)
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


def ruido(img2, ancho,alto):
    t1 = time()
    pixel= img2.load()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)= img2.getpixel((i,j)) #obtener pixeles
            ruido = random.randint(0,255) #generar ruido random
            z = random.randint(0,5000)
            try:
                if (ruido < 100):
                    pixel[i+z,j+z]=(0,0,0) #pixel leido mas un numero random para agregar pimienta
                else:
                    pixel[i+z,j+z] = (255,255,255) #pixel + # rand para agregar sal
            except:
                pass
    img2 = img2.save('ruido.jpg')
    timei=time()
    timef = timei - t1
    print "el tiempo para agregar ruido es:"+str(timef)+"segundos"

def byeruido(img2,ancho,alto):
    pixel = img2.load()
    t2=time()
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)=img2.getpixel((i,j))
            try:
                if(pixel[i,j]==(0,0,0) or pixel[i,j]==(255,255,255)):  
                    #print pixel[i,j]
                    #print "ya pase por aki"
                    pixel[i,j] = pixel[i+1,j]
                    #print pixel[i+1,j]
                    #print "ya pase por aka"
                else:
                    #print "Ola k ase" #es broma
                    continue
            except:
                pass
    img2.save('snruido.jpg')
    timei = time()
    timef = timei -t2
    print "el tiempo para quitar el ruido es:"+str(timef)+"segundos"

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
    img = img.save('binarizada.jpg')

def formas(img,ancho,alto):
    pixel= img.load()
    cntdr = []
    colors=[]
    porcentajes=[]
    cm=[] #cm = centros de masa
    for i in range(ancho):
        for j in range(alto):
            if pixel[i,j]== (0,0,0):
                a=random.randint(0,255)
                b=random.randint(0,255)
                c=random.randint(0,255)
                (r,g,b)= (a,b,c)
                #bfs(img,ancho,alto,(r,g,b),(i,j)) #se llama a la funcion bfs
                cont,color,c1,c2 = bfs(img,ancho,alto,(r,g,b),(i,j))
                por=(cont/float(ancho*alto))*100
                if por>.1:
                    cntdr.append(cont)
                    colors.append(color)
                    porcentajes.append(por)
                #print 'ya pase'
                try:
#c1 =centro 1 y c2 = centro 2
                    cm.append((sum(c1)/float(len(c1)),sum(c2)/float(len(c2))))
                except:
                    pass
#print 'sali'
    m = cntdr.index(max(cntdr))
    n = colors[m]
    print m
    print n
    for i in range(ancho):
        for j in range(alto):
            if pixel[i,j] == n:
                pixel[i,j]=(160,160,160)
                #print 'pase por aki'
    #porcentajes
    #porcentaje = (float(num)/(ancho*alto))*100

    draw=ImageDraw.Draw(img)
    for i,Z in enumerate(cm):
        draw.ellipse((Z[0]-2,Z[1]-2,Z[0]+2,Z[1]+2),fill=(0,0,0))# dibujar elipse 
    img =img.save('cm.jpg')

def bfs(img,ancho,alto,color,posa):
    pixel= img.load()
    cont=0
    cen1=[]
    cen2=[]
    cola=[] #creamos la cola
    cola.append(posa) #posicion actual se agrega a la cola
    inicio = pixel[posa]
    while len(cola)>0: 
        (i,j)=cola.pop(0)
        posa = pixel[i,j]
        if (posa == inicio or posa ==color):
            try:
                if(pixel[i-1,j]):
                    if(pixel[i-1,j]==inicio):
                        pixel[i-1,j] = color
                        cola.append((i-1,j))
                        cont+=1 # contador para encontrar los pixeles ke van en gris
                        cen1.append((i-1))
                        cen2.append((j))
            except:
                pass
            try:
                if(pixel[i+1,j]):
                    if(pixel[i+1,j]==inicio):
                        pixel[i+1,j] = color
                        cola.append((i+1,j))
                        cont+=1
                        cen1.append((i+1))
                        cen2.append((j))
            except:
                pass
            try:
                if(pixel[i,j-1]):
                    if(pixel[i,j-1]==inicio):
                        pixel[i,j-1] = color
                        cola.append((i,j-1))
                        cont+=1
                        cen1.append((i))
                        cen2.append((j-1))
            except:
                pass
            try:
                if(pixel[i,j+1]):
                    if(pixel[i,j+1]==inicio):
                        pixel[i,j+1] = color
                        cola.append((i,j+1))
                        cont+=1
                        cen1.append((i))
                        cen2.append((j+1))
            except:
                pass
    img = img.save('forms.jpg')
    return cont,color,cen1,cen2


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
