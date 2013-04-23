import sys
from sys import argv
import math
import Image
from PIL import ImageDraw 
from PIL import ImageOps
from math import fabs
from subprocess import call


#histograma del lado horizontal
def horizontalh(image):
    h = list()
    im = image.load()
    fl = open('hzt.dat','w')
    #prom = 0
    for x in range(image.size[0]):
        suma= 0
        for y in range(image.size[1]):
            suma += im[x,y]
        fl.write(str(x)+' '+str(suma)+'\n')
        h.append(suma)
    fl.close()
    #for i in h:
     #   prom+=1
    #prom= float(prom)/len(h)
    return h #, prom

#histograma vertical
def verticalh(image):
    h = list()
    im = image.load()
    fl = open('vert.dat','w')
   # prom=0
    for y in range(image.size[1]):
        suma=0
        for x in range(image.size[0]):
            suma+=im[x,y]
        fl.write(str(y)+' '+str(suma)+'\n')
        h.append(suma)
    #for i in h:
     #   prom +=i
    #prom = float(prom)/len(h)
    fl.close()
    return h#, prom

########################
def filtro(image):
    im= image.load()
    im_copy= (image.copy()).load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            temp=[]
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if x>= 0 and y>= 0 and x<image.size[0] and y<image.size[1]:
                        temp.append(im_copy[x,y])
            temp.sort()
            im[i,j] = int(temp[int(len(temp)/2)])
    return im

########################
def mins(h):
    algo = list()
    for i in range(len(h)):
           try:
               if(h[i-1] > h[i] and h[i+1] > h[i]): 
                algo.append(i)
           except:
               pass
    algo.sort()

    return algo

#######################
def det_agujeros(image_name, size = (128,128)):
    image = Image.open(image_name)
    original_image = image.copy()

    image = ImageOps.grayscale(image)
    filtro(image)

    hist_hor = horizontalh(image)
    hist_vert = verticalh(image)
    

    horizontal = mins(hist_hor)
    vertical = mins(hist_vert)
    
    call(['gnuplot','plot.gnu'])

    r=image.size
    image = original_image
    draw = ImageDraw.Draw(image)
    
    for x in horizontal:
        draw.line((x,0,x, image.size[0]), fill=(255,0,0))
        print 'pasa'

    for y in vertical:
        draw.line((0,y,image.size[1],y), fill = (0,0,255))
        print 'pasa'

    image.save('lin.png')
    #image.show()
def main():

    det_agujeros(argv[1])
    print 'OLA K ASE'
main()
