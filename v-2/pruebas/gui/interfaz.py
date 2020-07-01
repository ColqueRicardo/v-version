from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sys
sys.path.append("v-2/pruebas/gui/gestor_file.py")
from gestor_file import *

class gui():
    def __init__(self):

        'imagenes'


        self.vent = Tk()

        self.sistema_de_archivos=carpeta("master")
        self.sistema_de_archivos.asignar_id(0)
        self.cargar_pruebas()
        self.iconos_botones=[]

        self.maximo_ventana_x=1000
        self.maximo_ventana_y=800

        self.vent.geometry(str(self.maximo_ventana_x)+"x"+str(self.maximo_ventana_y))
        self.menu = Menu(self.vent)
        self.opciones = Menu(self.menu, tearoff=0)
        self.opciones.add_command(label="iniciar como servidor", command=self.iniciar_servidor)
        self.opciones.add_command(label="unirse", command=self.unirse)
        self.menu.add_cascade(label="opciones", menu=self.opciones)
        self.vent.config(menu=self.menu)

        self.iconos = Canvas(self.vent,bg="red")
        self.iconos.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.iconos.bind('<1>',lambda event:self.f(event))

        self.vent.mainloop()

    def f(self,event):
        x=(self.iconos.find_withtag(tk.CURRENT))
        'self.iconos.itemconfig(x,args)'
        self.iconos.move(x,0,75)
        print(self.iconos.gettags(x)[0],"tags elemento")
        print(type(self.sistema_de_archivos.contenido[int(self.iconos.gettags(x)[0])])==archivo)


    def iniciar_servidor(self):
        self.carpeta_jpg = "C:/Users/ricar/PycharmProjects/v-version/v-2/pruebas/iconos/carpeta.jpg"
        self.img_carpeta = ImageTk.PhotoImage(Image.open(self.carpeta_jpg).resize((50, 50)))
        self.archivo_jpg = "C:/Users/ricar/PycharmProjects/v-version/v-2/pruebas/iconos/archivo.jpg"
        self.img_archivo = ImageTk.PhotoImage(Image.open(self.archivo_jpg).resize((50, 50)))

        x=50
        y=50
        for i in self.sistema_de_archivos.contenido:
            if (type(i)==carpeta):
                self.iconos_botones.append(self.iconos.create_image(x,y, anchor="nw", image=self.img_carpeta,
                                                                    tags=str(i.id)))
            else:
                self.iconos_botones.append(self.iconos.create_image(x, y, anchor="nw", image=self.img_archivo,
                                                                    tags=str(i.id)))
            if x+100<self.maximo_ventana_x :
                x+=75
            else:
                x=50
                y+=75

        self.vent.mainloop()


    def unirse(self):
        print('unirse')

    def cargar_pruebas(self):
        ''
        for i in range(10):
            self.sistema_de_archivos.agregar_contenido(archivo(str(i) + ".exe"))
        self.sistema_de_archivos.agregar_contenido(carpeta("carpeta  1"))
        self.sistema_de_archivos.agregar_contenido(carpeta("carpeta  2"))
        for i in self.sistema_de_archivos.contenido:
            if type(i) == carpeta:
                for l in range(5):
                    i.agregar_contenido(archivo(str(l) + ".jpg"))

        'recorrer(self.sistema_de_archivos)'


gui()
