from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import sys
import pickle
sys.path.append("v-2/pruebas/gui/gestor_file.py")
from gestor_file import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
class gui():
    def __init__(self):

        'imagenes'


        self.vent = Tk()

        self.sistema_de_archivos=carpeta("master")
        self.sistema_de_archivos.asignar_id(0)
        self.archivos_contenidos_io=archivo_contenido()

        self.ruta=[]
        self.id_actual=-1
        'fase de pruebas off'
        'self.cargar_pruebas()'

        self.iconos_botones=[]

        self.maximo_ventana_x=1000
        self.maximo_ventana_y=800
        'margen izquierdo'
        self.vent.geometry(str(self.maximo_ventana_x)+"x"+str(self.maximo_ventana_y))
        self.menu = Menu(self.vent)
        self.opciones = Menu(self.menu, tearoff=0)
        self.opciones.add_command(label="iniciar como servidor", command=self.iniciar_servidor)
        self.opciones.add_command(label="unirse", command=self.unirse)
        self.menu.add_cascade(label="opciones", menu=self.opciones)
        self.vent.config(menu=self.menu)


        self.iconos = Canvas(self.vent,bg="red")
        self.iconos.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.iconos.bind('<1>',lambda event:self.select(event))
        self.vent.mainloop()

    def abrir(self):
        'falta tratar archivos'
        print(self.id_actual)
        if self.id_actual != -1:
            bus_complet=self.busqueda_carpeta(self.sistema_de_archivos,self.ruta+[self.id_actual])
            print(type(bus_complet))
            if type(bus_complet)==carpeta:
                self.iconos.delete("all")
                self.ruta.append(self.id_actual)
                self.cargar_canvas(bus_complet)
            else:
                print(self.archivos_contenidos_io.obtener_contenido(bus_complet.contenido))



        else:
            print("no se selecciono ningun archivo")


    def borrar(self):
        'self.ruta + self.icono_actual es el archivo a tocar'
        if self.id_actual!=-1:
            self.busqueda_carpeta(self.sistema_de_archivos,self.ruta).contenido[self.id_actual].visible=0
            self.iconos.delete("all")
            self.cargar_canvas(self.busqueda_carpeta(self.sistema_de_archivos, self.ruta))
            self.id_actual=-1
        else:
            print("no hay archivo seleccionado")

    def volver(self):
        if len(self.ruta)!=0:
            self.ruta.pop(len(self.ruta)-1)
            self.iconos.delete("all")
            self.cargar_canvas(self.busqueda_carpeta(self.sistema_de_archivos,self.ruta))
        else:
            print("no se puede volver atras")
    def select(self,event):
        try:
            'print("----------------------------")'
            x=(self.iconos.find_withtag(tk.CURRENT))
            'self.iconos.itemconfig(x,args)'
            'self.iconos.move(x,0,75)'
            '''print(self.iconos.gettags(x)[0],"tags elemento")
            print(self.obtener_geometry())'''
            self.id_actual=int(self.iconos.gettags(x)[0])
        except:
            print("ocurrio un error")
            self.id_actual=-1
    def agregar_carpeta(self):
        self.iconos.delete("all")
        self.busqueda_carpeta(self.sistema_de_archivos, self.ruta).agregar_contenido(carpeta("nueva carpeta"))
        self.cargar_canvas(self.busqueda_carpeta(self.sistema_de_archivos, self.ruta))
    def agregar_archivo(self):

        exist=False
        file_s= FileDialog.askopenfilename(title="Abrir un fichero")
        if file_s!="":
            name=self.sacar_nombre_direccion(file_s)
            for i in self.busqueda_carpeta(self.sistema_de_archivos, self.ruta).contenido:
                if type(i)==archivo:
                    if name==i.nombre +"."+ i.extencion:
                        exist = True
                        if MessageBox.askquestion("advertencia","¿existe un archvio igual en esta carpeta desea reemplazarlo?"):
                            print("se reemplazo")

            if exist==False:
                c = open(file_s, "rb")
                'crea una instancia de un archivo y la guarda en la carpeta actual'
                print(self.archivos_contenidos_io.cantidad_archivos())
                self.busqueda_carpeta(self.sistema_de_archivos, self.ruta).\
                    agregar_contenido(archivo(name,self.archivos_contenidos_io.cantidad_archivos()))
                'print(self.busqueda_carpeta(self.sistema_de_archivos, self.ruta+[self.id_actual]).contenido)'
                self.archivos_contenidos_io.agregar(c.read())
                print(self.archivos_contenidos_io.cantidad_archivos())
                self.iconos.delete("all")
                self.cargar_canvas(self.busqueda_carpeta(self.sistema_de_archivos, self.ruta))
        else:
            print("no se selecciono ningun archiivo")
    'fin de los eventos de movimiento'
    def iniciar_servidor(self):


        self.menu.add_command(label="abrir",command=lambda : self.abrir())
        self.menu.add_command(label="agreagar archivo",command=lambda : self.agregar_archivo())
        self.menu.add_command(label="nueva carpeta",command=lambda : self.agregar_carpeta())
        self.menu.add_command(label="borrar",command=lambda : self.borrar())
        self.menu.add_command(label="volver",command=lambda : self.volver())


        self.carpeta_jpg = "C:/Users/ricar/PycharmProjects/v-version/v-2/pruebas/iconos/carpeta.jpg"
        self.img_carpeta = ImageTk.PhotoImage(Image.open(self.carpeta_jpg).resize((50, 50)))
        self.archivo_jpg = "C:/Users/ricar/PycharmProjects/v-version/v-2/pruebas/iconos/archivo.jpg"
        self.img_archivo = ImageTk.PhotoImage(Image.open(self.archivo_jpg).resize((50, 50)))

        self.cargar_canvas(self.sistema_de_archivos)

    def obtener_geometry(self):
        v=[]
        v.append("")
        j=0
        print(self.vent.geometry())
        for i in range(len(self.vent.geometry())):
            if self.vent.geometry()[i:i+1]!="+" and self.vent.geometry()[i:i+1]!="x":
                v[j]+=self.vent.geometry()[i:i+1]
            else:
                v.append("")
                j+=1
        return v
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

    def busqueda_carpeta(self,dir_actual, ruta):
        try:
            for i in ruta:
                'si falla es porque se modifico la direccion o ruta actual para que no sea integro'
                dir_actual = dir_actual.contenido[i]
            return dir_actual
        except:
            'print("no se encontro o ruta desconocida")'
            return None

    def busqueda_archivo(self,dir_actual, ruta):
        try:
            for i in ruta:
                if type(dir_actual) == carpeta:
                    dir_actual = dir_actual.contenido[i]
                if type(dir_actual) == archivo:
                    return dir_actual
                    'print("encontrado:", dir_actual.nombre, dir_actual.extencion)'
        except:
            'print("no se encontro o ruta desconocida")'
            return None
    def cargar_canvas(self,sistema_archivos):
        x=50
        y=50
        p=0
        self.iconos_botones=[]
        for i in sistema_archivos.contenido:

            if (i.visible==1):
                if (type(i)==carpeta):
                    self.iconos_botones.append(self.iconos.create_image(x,y, anchor="nw", image=self.img_carpeta,
                                                                        tags=str(i.id)))

                    nom = i.nombre
                else:
                    self.iconos_botones.append(self.iconos.create_image(x, y, anchor="nw", image=self.img_archivo,
                                                                        tags=str(i.id)))
                    nom = i.nombre + "." + i.extencion

                if len(nom)>10:
                    nom=nom[0:10]+"..."
                self.iconos.create_text(x+25,y+60,fill="darkblue",font="arial 8 ",text=nom)
                if x+100<self.maximo_ventana_x :
                    x+=75
                else:
                    x=50
                    y+=75
                p+=1
        self.vent.mainloop()
    def sacar_nombre_direccion(self,direccion):
        i=len(direccion)-1

        while direccion[i:i+1]!="/":
            i-=1
        return direccion[i+1:len(direccion)]

gui()
