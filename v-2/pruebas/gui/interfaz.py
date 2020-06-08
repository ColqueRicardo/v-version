from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class gui():
    def __init__(self):
        self.vent = Tk()
        self.vent.geometry("1000x800")
        self.menu = Menu(self.vent)
        self.opciones = Menu(self.menu, tearoff=0)
        self.opciones.add_command(label="iniciar como servidor", command=self.iniciar_servidor)
        self.opciones.add_command(label="unirse", command=self.unirse)
        self.menu.add_cascade(label="opciones", menu=self.opciones)
        self.vent.config(menu=self.menu)

        self.iconos = Canvas(self.vent,bg="red")
        self.iconos.place(relx=0, rely=0, relheight=1, relwidth=1)


        self.vent.mainloop()

    def iniciar_servidor(self):
        self.archivos = []
        self.carpetas = []
        self.carpeta_jpg = "C:/Users/ricar/PycharmProjects/v-version/v-2/pruebas/iconos/carpeta.jpg"
        img = ImageTk.PhotoImage(Image.open(self.carpeta_jpg).resize((200,200)))

        self.carpeta = self.iconos.create_image(200, 0, anchor="nw", image=img)
    

        print("iniciar")

    def unirse(self):
        print('unirse')


gui()
