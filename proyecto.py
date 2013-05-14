import Tkinter
import cv
from Tkinter import *
from PIL import Image, ImageTk
import sys
from time import *

image_path = None
try:
    image_path = sys.argv[1]
except:
    print "Error Imagen"

class App:
    def __init__(self, master, image_path):
        self.nombre_imagen = image_path
        self.imagen_original = self.abrir_original()
        self.imagen_actual = self.imagen_original
        self.x, self.y = self.imagen_original.size
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
#-------------------------- botones
        self.procesar = Button(self.frame, text = "Ubicar Codigo", fg = "red", command = self.procesar)
        self.guarda = Button(self.frame, text = "Guardar Imagen", fg = "red", command = self.guardar)

        self.procesar.grid(row=0, column = 0, padx = 10, pady = 10)
        self.guarda.grid(row=0, column = 1, padx =10, pady = 10)
        foto = Image.open(image_path)
        foto = ImageTk.PhotoImage(foto)
        self.picture = Label(self.frame, image = foto)
        self.picture.image = foto
        self.picture.grid(row=1, column = 0, columnspan = 7, sticky= W+E+N+S, padx=5, pady=5)
#----------------------------abrir
    def abrir_original(self):
        imagen = Image.open(self.nombre_imagen)
        imagen = imagen.convert('RGB')
        return imagen

    def guardar(self, imgco):
        cv.SaveImage("codigo.jpg",imgco)
        self.imagen_actual.save('detectado.jpg')

    def actualizar_imagen(self):
        foto = ImageTk.PhotoImage(self.imagen_actual)
        self.picture = Label(self.frame, image = foto)
        self.picture.image = foto
        self.picture.grid(row =1,column = 0, columnspan=7,sticky=W+E+N+S, padx=5, pady=5)
  
    def procesar(self):
        time1 = time()
        global image_path
        imgco = cv.LoadImage(image_path) #cargar imagen
        img = cv.CreateImage(cv.GetSize(imgco),8,1)
        imgx = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_16S,1)
        imgy = cv.CreateImage(cv.GetSize(img),cv.IPL_DEPTH_16S,1)
        thresh = cv.CreateImage(cv.GetSize(img),8,1)
#------------Proceso
        #----------Escala de grises
        cv.CvtColor(imgco,img,cv.CV_BGR2GRAY)
        cv.SaveImage("eg.jpg",imgco)

        #----------Aplicamos gradientes ---Mascara de Sobel
        cv.Sobel(img,imgx,1,0,3)
        cv.Abs(imgx,imgx)

        cv.Sobel(img,imgy,0,1,3)
        cv.Abs(imgy,imgy)
        
        cv.Sub(imgx,imgy,imgx)
        cv.ConvertScale(imgx,img)
        
        #----------Filtro
        cv.Smooth(img,img,cv.CV_GAUSSIAN,7,7,0)

        #----------Aplicacion de Umbrales
        cv.Threshold(img,thresh,100,255,cv.CV_THRESH_BINARY)
        
        cv.Erode(thresh,thresh,None,2)
        cv.Dilate(thresh,thresh,None,5)
        
        storage = cv.CreateMemStorage(0)
        contour = cv.FindContours(thresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
        area = 0
        while contour:
            max_area = cv.ContourArea(contour)
            if max_area>area:
                area = max_area
                bar = list(contour) 
            contour=contour.h_next()
            
        bound_rect = cv.BoundingRect(bar)
        pt1 = (bound_rect[0], bound_rect[1])
        pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])

        cv.Rectangle(imgco, pt1, pt2, cv.CV_RGB(255,0,255), 2)

        cv.ShowImage('img',imgco)    
        cv.WaitKey(0)
        time2 = time()
        timef = time2 - time1
        print "Tiempo de ejecucion: " +str(timef)+"segundos."
        return imgco
#--------------------------------Main
def main():
    try:
        image_path = sys.argv[1]
        print image_path
    except:
        print "No imagen"
        return
    root = Tk()
    proceso = App(root, image_path)
    root.title("Proceso de Imagen")
    root.mainloop()

if __name__ == "__main__" :
    main()
