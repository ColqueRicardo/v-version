import socket
import string
import sys
'''sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba v1/servidor.py")
from servidor import *'''

import datetime
import pickle

import threading
from tkinter import *



class pong_game():
    def __init__(self,ip,jugador):
        self.ip=ip
        self.jugador=jugador

        self.ventana= Tk()
        self.x=self.ventana.winfo_screenwidth()
        self.y=self.ventana.winfo_screenheight()
        self.ventana.geometry("{0}x{1}+0+0".format(self.x,self.y))
        self.ventana.overrideredirect(TRUE)
        self.ventana.config(bg="RED")
        self.canvas= Canvas(self.ventana,bg="Black")

        self.x=1500
        self.y=800

        'pociciones de los objetos'

        self.jugador_posicion = []
        self.jugador_posicion.append((800 * 0.8) * 0.25)
        self.jugador_posicion.append((800 * 0.8) * 0.25)
        self.tope_izquierda = (1500 * 0.8) * 0.1
        self.tope_derecha = (1500 * 0.8) * 0.9
        self.tope_arriba = (800 * 0.8) * 0.1
        'el tope de abajo tiene q considerar el tamaño de la barra '
        self.tamaño_barra = 800 * 0.8 * 0.5
        self.tope_abajo = ((800 * 0.8) * 0.9) - self.tamaño_barra

        x=(1500*0.8)//2
        y=(800*0.8)//2

        t=(1500*0.8)*0.01

        self.pelota_posicion=[]
        self.pelota_posicion.append(x-t)
        self.pelota_posicion.append(y-t)

        'inicio de los objetos'

        self.canvas.place(x=self.x*0.1,y=self.y*0.1,width=self.x*0.8,height=self.y*0.8)

        self.jugador1=  self.canvas.create_line((1500*0.8)*0.075,self.jugador_posicion[0] ,(1500*0.8)*0.075,self.jugador_posicion[0]+self.tamaño_barra
                                                ,fill="blue",width=(1500*0.8)*0.01,tags="j1")

        self.pelota= self.canvas.create_rectangle(self.pelota_posicion[0] ,self.pelota_posicion[1],
                                                  self.pelota_posicion[0]+(2*t),self.pelota_posicion[1]+(2*t),
                                                    fill="white", tags="pelota")



        self.jugador2= self.canvas.create_line((1500*0.8) * 0.925,self.jugador_posicion[0] , (1500*0.8) * 0.925, self.jugador_posicion[0]+self.tamaño_barra
                                               , fill="blue",width=(1500*0.8) * 0.01, tags="j2")


        self.canvas.focus_set()
        self.establecer_conexion()

        self.canvas.bind("<1>",lambda  event: self.click(event))
        self.canvas.bind("<Key>",lambda event: self.mover(event))
        self.hilo_actualizador=threading.Thread(name="actualizar",target=self.actualizar)
        self.hilo_actualizador.start()
        self.hilo_mainloop=threading.Thread(name="mainloop",target=self.ventana.mainloop())
        self.hilo_mainloop.start()

    def click(self,event):
        print(event.x,event.y)

    def mover(self,event):
        if event.char=="w":
            self.enviar_movimiento("arriba")
        if event.char=="s":
            self.enviar_movimiento("abajo")
    def enviar_movimiento(self,movimiento):
        'movimiento = pickle.dumps(movimiento)'
        self.socket.sendto(movimiento.encode(), (self.ip, 8000))

        'respuesta = self.socket.recv(1024).decode()'
        'print(respuesta)'

    def establecer_conexion(self):

        'se establece el recive'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, 8001))
        self.socket.listen(1)
        self.conexion, self.direccion = self.socket.accept()

        'se establece el envia'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, 8000))
        '''
        mensaje=[]
        mensaje.append("inicio")
        mensaje.append(self.inicio_y)
        mensaje.append(self.minimo_y)
        mensaje.append(self.maximo_y)
        'mensaje.append(0)'
        self.socket.sendto(pickle.dumps(mensaje), (self.ip, 8000))'''

    def actualizar(self):
        'conexion de recive'
        while True:
            self.valores = self.conexion.recv(1024)
            self.valores=pickle.loads(self.valores)
            'print(self.valores)'
            self.canvas.move(self.jugador1 ,0,self.valores[0]-self.jugador_posicion[0])
            self.canvas.move(self.jugador2, 0, self.valores[1] - self.jugador_posicion[1])
            self.jugador_posicion[0]=self.valores[0]
            self.jugador_posicion[1]=self.valores[1]
            self.canvas.move(self.pelota,self.valores[2]- self.pelota_posicion[0] ,self.valores[3] - self.pelota_posicion[1])
            self.pelota_posicion[0]=self.valores[2]
            self.pelota_posicion[1]=self.valores[3]


            'self.conexion.send("si".encode())'

        self.conexion.close()


pg=pong_game(socket.gethostbyname(socket.gethostname()),"j1")