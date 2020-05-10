from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import socket
import sys
import datetime
from tkinter import messagebox
import time
import threading
from threading import Lock
import random
'sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")'
from prueba import *

class gui_pong():
    def __init__(self):
        self.jugador_id=None


        self.blocker=Lock()


        self.ventana=Tk()
        self.x = int(self.ventana.winfo_screenwidth())
        self.y = int(self.ventana.winfo_screenheight())



        xy = "{0}x{0}+" +"0" + "+" + "0"
        self.ventana.geometry((xy.format(self.x, self.y)))

        self.puntuacion_j1=0
        self.puntuacion_j2=0

        self.tamaño_barra=0


        self.canvas= Canvas(self.ventana,bg="black")
        self.canvas.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.canvas.focus_set()

        self.canvas.create_line(30,self.y//2,30,(self.y//2)*1.2,fill="white",width=15,tags="jugador1")
        self.canvas.create_line(self.x-30,self.y//2,self.x-30,(self.y//2)*1.2,fill="white",width=15,tags="jugador2")
        self.canvas.create_rectangle((self.x//2)-15,(self.y//2)-15,(self.x//2)+15,(self.y//2)+15,fill="white",tags="pelota")

        self.canvas.bind("<Key>",lambda event:self.mover(event))

        self.canvas.move(self.canvas.find_withtag("jugador1"), 30, 0)

        '''
        coneccion_estable=FALSE
        msg=FALSE
        while not msg or not coneccion_estable:
            msg =messagebox.askyesno(message="¿reintentar?", title="espere al otro jugador")
            'funcion para reintentar la conecxion'
            coneccion_estable= self.reintentar()
        '''
        self.reintentar()

        self.hilo_actualizar=threading.Timer(0.01,lambda :self.actualizar())
        self.hilo_actualizar.start()
        '''
        self.hilo_mainloop=threading.Thread(self.ventana.mainloop())
        self.hilo_mainloop.start()
        '''
        self.ventana.mainloop()


    def entablar_conexion(self,mensaje):
        'self.blocker.acquire()'

        self.socket = socket.socket()
        self.socket.connect(('localhost', 8000))

        mensaje_codificado=codificar_mensaje(mensaje)

        self.socket.sendto(mensaje_codificado,('localhost',8000))

        respuesta = decoficar_mensaje(self.socket.recv(1024).decode())
        self.socket.close()
        'self.blocker.release()'
        return respuesta
    def reintentar(self):
        msg=["jugador esperando"],[self.x],[self.y]
        respuesta=self.entablar_conexion(msg)
        if respuesta[0]=="se puede":
            self.jugador_id=respuesta[1]

            self.tamaño_barra=int(respuesta[2])
            self.inicio_y=[]
            self.inicio_y.append(int(respuesta[3]))
            self.inicio_y.append(int(respuesta[4]))


            return TRUE
        else:
            print(respuesta,"fallo")
    def mover(self,event):
        self.canvas.update()
        print(event.char)
        if event.char=="w":
            msg=["arriba"],[self.jugador_id]
            respuesta=(self.entablar_conexion(msg))

            mensaje=["actualizar"],[self.jugador_id]
            respuesta=self.entablar_conexion(mensaje)

            print(respuesta[0])
            print(self.inicio_y[0])

            self.canvas.move(self.canvas.find_withtag("jugador1"),0,int(respuesta[0])-int(self.inicio_y[0]))

            self.inicio_y[0]=int(respuesta[0])

            'self.actualizar(int(respuesta[0]),int(respuesta[0]),230,230)'
            'self.canvas.create_line(30,int(respuesta[0]), 30,int(respuesta[0])+self.tamaño_barra, fill="white", width=15,tags=str(self.jugador_id))'
            '''self.inicio_j1_y=self.inicio_j1_y+ (10*self.velocidad_jugador)
            self.canvas.create_line(30,self.inicio_j1_y,30,self.inicio_j1_y+200,fill="white",width=15,tags="jugador1")
            '''
        elif event.char=="s":
            msg=["abajo"],[self.jugador_id]

            respuesta=(self.entablar_conexion(msg))

            print(respuesta[0])
            print(self.inicio_y[0])

            self.canvas.move(self.canvas.find_withtag("jugador1"),0,int(respuesta[0])-int(self.inicio_y[0]))

            self.inicio_y[0]=int(respuesta[0])

            'self.canvas.create_line(30,int(respuesta[0]), 30,int(respuesta[0])+self.tamaño_barra, fill="white", width=15,tags=str(self.jugador_id))'

            '''
            if self.inicio_j1_y>30:
                self.canvas.delete("jugador1")
                self.inicio_j1_y = self.inicio_j1_y - (10*self.velocidad_jugador)
                self.canvas.create_line(30, self.inicio_j1_y, 30, self.inicio_j1_y + 200, fill="white", width=15, tags="jugador1")
            else:
                print("muy arriba")
            '''
    def actualizar(self):
        while TRUE:
            mensaje=["actualizar"],[self.jugador_id]
            respuesta=self.entablar_conexion(mensaje)

            print("empiezasss",respuesta)
            '[self.inicio_jugadores[0]],[self.inicio_jugadores[1]],[self.pelota_posicion[int(peticion[0])][0]],[self.pelota_posicion[int(peticion[0])][1]]'
            'inicio "y" de j1 y j2 , posicion de la pelota dependiendo de j1 o j2 '

            self.canvas.move(self.canvas.find_withtag("jugador1"),30,int(respuesta[0]))
            '''
            self.canvas.create_line(30,int(respuesta[0]),30,int(respuesta[0])+self.tamaño_barra,fill="white",width=15)
            self.canvas.create_line(self.x-30,int(respuesta[1]),self.x-30,int(respuesta[1])+self.tamaño_barra,fill="white",width=15)
            self.canvas.create_rectangle((int(respuesta[2])//2)-15,(int(respuesta[3])//2)-15,(int(respuesta[2])//2)+15,(int(respuesta[3])//2)+15,fill="white",tags="pelota")
            '''
gui=gui_pong()
