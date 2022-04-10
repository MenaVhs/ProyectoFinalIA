from tkinter import filedialog, font
import cv2
import numpy as np
from tkinter import *
import os
import sys
#import requests
from Graficar import graficar
from GetModel import GetModel
import numpy as np


def main():
    graf = graficar()
    
    def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def print_image():
        img = PhotoImage(file=resource_path('scatter.png'))
        l2.config(image=img)
        l2.image = img


    def upload_file():
        file=filedialog.askopenfilename()
        fob=open(file, 'r')
        print(fob.name)

        dirVideo = fob.name
        cap = cv2.VideoCapture(dirVideo)

        model_xml = GetModel.get_model_by_url(inputUrl.get("1.0",END))
        

        with open("cascade.xml", "wb") as f:
            f.write(model_xml)     


        rataClasificador = cv2.CascadeClassifier('cascade.xml')
        ax =  np.array([])
        ay =  np.array([])
        while cap.isOpened():
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rat = rataClasificador.detectMultiScale(gray,
            scaleFactor=2,
            minNeighbors=40,
            minSize=(50, 50))
            for (x, y, w, h) in rat:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, 'Rata', (x, y-10), 2, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
                ax = np.append(ax,x )
                ay = np.append(ay,y*-1 )
            cv2.imshow('frame', frame)
            if cv2.waitKey(40) == 27:
                break
        graf.scatter_graph(ax, ay)
        print_image()
        cv2.destroyAllWindows()
        cap.release()

        
    


    fontTitulo = (resource_path("Inter-Regular"), 24)
    fontTexto = (resource_path("Inter-Regular"), 18)

    raiz = Tk()

    raiz.title("Clasificador de Cascada")
    raiz.resizable(0,0)
    raiz.iconbitmap(resource_path("icono.ico"))


    l1 = Label(raiz, text="Clasificador de Cascada: Roedor",
    font=fontTitulo)
    l1.grid(row=1, column=1)
    
    ls1 = Label(raiz, text="",
    font=fontTexto)
    ls1.grid(row=2, column=1)


    ltext = Label(raiz, text="URL del modelo Haar Cascade Classifier",
    font=fontTexto)
    ltext.grid(row=3, column=1)
    
    inputUrl = Text(raiz, height = 1, width= 50,  font=fontTexto)

    inputUrl.insert(END, "http://192.168.100.29:9099/cascadeModel")
    inputUrl.grid(row=4, column=1)              
    
    ls2 = Label(raiz, text="",
    font=fontTexto)
    ls2.grid(row=5, column=1)
    
    b1 = Button(raiz, text="Seleccionar Video", font=fontTexto,
    command=lambda:upload_file())
    b1.grid(row=6, column=1)

    ls3 = Label(raiz, text="",
    font=fontTexto)
    ls3.grid(row=7, column=1)

    l3 = Label(raiz, text="Mapa de dispersión",
    font=fontTexto)
    l3.grid(row=8, column=1)

    img = PhotoImage(file=resource_path('scatter.png'))
    l2 = Label(raiz, image=img)
    l2.grid(row=9, column=1)


    raiz.mainloop()


    


if __name__ == "__main__":
    main()