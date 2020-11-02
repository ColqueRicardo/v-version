from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)


from PIL import Image, ImageTk

import tkinter as tk

import socket
import sys
import datetime
from tkinter import messagebox
import time

from threading import Lock
import random
'sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")'
'from prueba import *'

class ajedres():
    def __init__(self):
        'pieza actual seleccionada'
        self.pieza_i=0
        self.pieza_j=0
        'ver si hay vista de posibles movimientos activa'
        self.vista=FALSE
        'lista de movimientos'
        self.mov_posibles=[]

        self.tablero = []
        for i in range (8):
            self.tablero.append([])
            for j in range (8):
                self.tablero[i].append(None )
        self.tablero[0][0]=pieza(0,0,1,"torre")
        self.tablero[1][0]=pieza(0,1,1,"caballo")
        self.tablero[2][0]=pieza(0,2,1,"alfil")
        self.tablero[3][0]=pieza(0,3,1,"reina")
        self.tablero[4][0] = pieza(0,4,1,"rey")
        self.tablero[5][0]=pieza(0,5,1,"alfil")
        self.tablero[6][0] = pieza(0,6,1,"caballo")
        self.tablero[7][0] = pieza(0,7,1,"torre")

        self.tablero[0][7] = pieza(7,0,-1,"torre")
        self.tablero[1][7] = pieza(7,1,-1,"caballo")
        self.tablero[2][7] = pieza(7,2,-1,"alfil")
        self.tablero[3][7] = pieza(7,3,-1,"rey")
        self.tablero[4][7] = pieza(7,4,-1,"reina")
        self.tablero[5][7] = pieza(7,5,-1,"alfil")
        self.tablero[6][7] = pieza(7,6,-1,"caballo")
        self.tablero[7][7] = pieza(7,7,-1,"torre")

        for i in range(8):
            self.tablero[i][1]=pieza(1,i,1,"peon")
            self.tablero[i][6]=pieza(6,i,-1,"peon")

        self.turno=1
        self.jugador1=1
        self.jugador2=-1

        self.ventana=Tk()
        self.ventana.geometry("900x800+200+10")
        self.canvas=Canvas(self.ventana)
        self.canvas.place(x=0,y=0,width=480,height=480)


        self.tam=50
        self.inicio_x=30
        ver=TRUE

        self.canvas.create_rectangle(80,80,480,480, fill="white", width=1)

        for i in range(8):
            self.inicio_x += self.tam
            self.inicio_y = 80
            if ver:
                ver=FALSE
            else:
                ver=TRUE
            for i in range(8):
                if ver:
                    self.canvas.create_rectangle(self.inicio_x,self.inicio_y,self.inicio_x+self.tam,self.inicio_y+self.tam,fill="black",width=1)
                    ver=FALSE
                else:
                    self.canvas.create_rectangle(self.inicio_x,self.inicio_y,self.inicio_x+self.tam,self.inicio_y+self.tam, fill="white",width=1)
                    ver=TRUE
                self.inicio_y+=self.tam
        ruta="C:/Users/ricar/Desktop/pruebas/piezas/"

        imagenes=[]
        indice=0

        inicio_x = 30
        for i in range (8):

            inicio_x+=self.tam
            inicio_y=80

            for j in range(2):



                jugador=self.tablero[i][j].jugador
                tipo=self.tablero[i][j].tipo_pieza

                ruta_imagen=ruta+str(tipo)+str(jugador)+".png"
                img=Image.open(ruta_imagen)
                img=img.resize((self.tam,self.tam))

                self.tablero[i][j].imagen_pieza(ImageTk.PhotoImage(img))



                imagenes.append(ImageTk.PhotoImage(img))
                self.canvas.create_image( inicio_x ,inicio_y , anchor="nw", image=imagenes[indice],tags=str(i)+str(j))
                indice+=1

                self.tablero[i][j].x=inicio_x
                self.tablero[i][j].y=inicio_y

                inicio_y+=self.tam

        inicio_x = 30

        for i in range(8):
            inicio_x+=self.tam
            inicio_y=380

            for j in range(6, 8):

                jugador=self.tablero[i][j].jugador+3
                tipo=self.tablero[i][j].tipo_pieza

                ruta_imagen=ruta+str(tipo)+str(jugador)+".png"
                img=Image.open(ruta_imagen)
                img=img.resize((self.tam,self.tam))

                self.tablero[i][j].imagen_pieza(ImageTk.PhotoImage(img))


                imagenes.append(ImageTk.PhotoImage(img))
                self.canvas.create_image( inicio_x ,inicio_y , anchor="nw", image=imagenes[indice],tags=str(i)+str(j))
                indice+=1

                self.tablero[i][j].x=inicio_x
                self.tablero[i][j].y=inicio_y
                inicio_y+=self.tam

        self.canvas.bind('<1>',lambda event:self.hola(event))

        print("enpezo")

        self.ventana.mainloop()

    def hola(self,event):


        '''
        print("coords")
        print(event.x,event.y)
        print(self.canvas.canvasx(event.x),self.canvas.canvasy(event.y))

        print(tk.CURRENT)
        print(self.canvas.find_withtag(tk.CURRENT))
        print(self.canvas.find_closest(event.x,event.y))    '''

        self.detectar_pieza(event.x,event.y,self.canvas.find_withtag(tk.CURRENT))

        'self.canvas.move(self.canvas.find_closest(event.x,event.y),10,10)'
        'self.canvas.delete(self.canvas.find_withtag(tk.CURRENT))'
        '''for i in range (8):
            for j in range(8):
                if(self.canvas.find_withtag(tk.CURRENT)==self.canvas.find_withtag("{},{}".format(i,j))):
                    print("1")

                if(self.canvas.find_closest(event.x,event.y)==self.canvas.find_withtag("{},{}".format(i,j))):
                    print("2")
                if(self.canvas.find_withtag("{},{}".format(i,j))==self.canvas.find_closest(event.x,event.y)):
                    print("3")'''
    def vista_movimiento(self):
        ''
        print(self.tablero[self.pieza_i][self.pieza_j].tipo_pieza)
        if self.tablero[self.pieza_i][self.pieza_j].tipo_pieza=="peon":

            if not self.vista:
                self.movimiento_peon()
                self.vista=TRUE


                '''
                self.tablero[self.pieza_i+jugador][self.pieza_j-jugador]=pieza(x,y,self.tablero[self.pieza_i][self.pieza_j].jugador,"posible")
                self.tablero[self.pieza_i+jugador][self.pieza_j + jugador] = pieza(x,y, self.tablero[self.pieza_i][self.pieza_j].jugador, "posible")
                self.tablero[self.pieza_i+jugador][self.pieza_j ] = pieza(x, y, self.tablero[self.pieza_i][self.pieza_j].jugador, "posible")
                '''
            else:
                self.mov_posibles = []

                self.vista=FALSE
                self.canvas.delete("mov_pos")


    def movimiento_peon(self):
        jugador = self.tablero[self.pieza_i][self.pieza_j].jugador

        y = ((self.pieza_i + self.tablero[self.pieza_i][self.pieza_j].jugador) * self.tam) + 80
        x = ((self.pieza_j + 1) * self.tam) + 30

        self.canvas.create_rectangle(x, y, x + self.tam, y + self.tam, fill="yellow", width=0.1,
                                     tags="mov_pos")
        self.mov_posibles=[]

        if jugador == 1:
            '''
            self.tablero[self.pieza_i + jugador][self.pieza_j - jugador]=pieza(0,0,0,"hola")
            self.tablero[self.pieza_i + jugador][self.pieza_j + jugador]=pieza(0,0,0,"hola")
            '''

            self.mov_posibles.append(self.obtener_i(x))
            self.mov_posibles.append(self.obtener_j(y))

            if type(self.tablero[self.pieza_i + jugador][self.pieza_j + jugador]) == pieza:
                if self.tablero[self.pieza_i + jugador][self.pieza_j + jugador].tipo_pieza != "error":
                    self.canvas.create_rectangle(x + self.tam, y, x + (2 * self.tam), y + self.tam, fill="yellow",
                                                 width=0.1, tags="mov_pos")
                    self.mov_posibles.append(self.obtener_i(x+self.tam))
                    self.mov_posibles.append(self.obtener_j(y))
            if type(self.tablero[self.pieza_i + jugador][self.pieza_j - jugador]) == pieza:
                if self.tablero[self.pieza_i + jugador][self.pieza_j - jugador].tipo_pieza != "error":
                    self.canvas.create_rectangle(x - self.tam, y, x, y + self.tam, fill="yellow", width=0.1,
                                                 tags="mov_pos")

                    self.mov_posibles.append(self.obtener_i(x-self.tam))
                    self.mov_posibles.append(self.obtener_j(y))
            print("matrz mov",self.mov_posibles)
        else:
            'self.tablero[self.pieza_i + jugador][self.pieza_j - jugador] = pieza(0, 0, 0, "hola")'
            'self.tablero[self.pieza_i + jugador][self.pieza_j + jugador] = pieza(0, 0, 0, "hola")'

            if type(self.tablero[self.pieza_i + jugador][self.pieza_j - jugador]) == pieza:
                if self.tablero[self.pieza_i + jugador][self.pieza_j - jugador].tipo_pieza != "error":
                    self.canvas.create_rectangle(x + self.tam, y, x + (2 * self.tam), y + self.tam,
                                                 fill="yellow",
                                                 width=0.1, tags="mov_pos")

            if type(self.tablero[self.pieza_i + jugador][self.pieza_j + jugador]) == pieza:
                if self.tablero[self.pieza_i + jugador][self.pieza_j + jugador].tipo_pieza != "error":
                    self.canvas.create_rectangle(x - self.tam, y, x, y + self.tam, fill="yellow", width=0.1,
                                                 tags="mov_pos")
    def movimiento_torre(self):
        jugador = self.tablero[self.pieza_i][self.pieza_j].jugador

    def detectar_pieza(self,x,y,pieza_canvas):
        self.pieza_j=(y-30)//self.tam -1
        self.pieza_i=(x-30)//self.tam -1
        if type(self.tablero[self.pieza_i][self.pieza_j])==pieza:
            self.vista_movimiento()
        else:
            'mover la pieza'
            print("mover pieza")

            if len(self.mov_posibles)!=0:
                nuevo_i=self.obtener_i(x)
                nuevo_j=self.obtener_j(y)

                print(self.obtener_x_y(nuevo_i) ,self.obtener_x_y(nuevo_j) )
                self.canvas.create_image(self.obtener_x_y(nuevo_i) ,self.obtener_x_y(nuevo_j) , anchor="nw", image=self.tablero[self.pieza_i][self.pieza_j] ,tags=str(self.pieza_i)+str(self.pieza_j))

                self.canvas.delete(str(self.pieza_i)+str(self.pieza_j))


                s=self.tablero[nuevo_i][nuevo_j]
                print(s)

                print(self.tablero[self.pieza_i][self.pieza_j].tipo_pieza)
                self.tablero[nuevo_i][nuevo_j]=self.tablero[self.pieza_i][self.pieza_j]



                self.tablero[self.pieza_i][self.pieza_j]=s
                del s

                self.mov_posibles=[]

    def obtener_i(self,x):

        return int((x - 30) // self.tam - 1)
    def obtener_j(self,y):
        return int((y - 30) // self.tam - 1)
    def obtener_x_y(self,i):
        return int(((i+1)*self.tam)+30)

class pieza():
    def __init__(self,x,y,jugador,tipo_pieza):
        self.x=int(x)
        self.y=int(y)
        self.jugador=int(jugador)
        self.tipo_pieza=tipo_pieza
    def imagen_pieza(self,imagen):
        self.imagen_pieza=imagen


ajedres()


