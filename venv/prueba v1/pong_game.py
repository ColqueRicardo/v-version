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

        self.y=800
        self.x=1500

        self.canvas.place(x=self.x*0.1,y=self.y*0.1,width=self.x*0.8,height=self.y*0.8)
        self.cx=self.x*0.8
        self.cy=self.y*0.8
        self.jugador1=  self.canvas.create_line(self.cx*0.075,self.cy*0.25,self.cx*0.075,self.cy*0.75,fill="blue",
                                width=self.cx*0.01,tags="j1")
        self.t=(self.cx*0.01)
        x=(self.cx//2)
        y=(self.cy//2)
        self.tamaño = self.cy * 0.5
        self.pelota= self.canvas.create_rectangle(x-self.t,y-self.t,x+self.t,y+self.t,
                                     fill="white", tags="pelota")
        '''self.pelota_posicion_x=x-self.t
        self.pelota_posicion_y=y-self.t'''

        self.jugador2= self.canvas.create_line(self.cx * 0.925, self.cy * 0.25, self.cx * 0.925, (self.cy * 0.25) +self.tamaño, fill="blue",
                                width=self.cx * 0.01, tags="j2")

        self.inicio_y=self.cy*0.25
        self.minimo_y=self.cy*0.05
        self.maximo_y=self.cy*0.95-self.tamaño

        self.canvas.focus_set()
        self.establecer_conexion()

        'self.canvas.bind("<1>",lambda  event: self.click(event))'
        self.canvas.bind("<Key>",lambda event: self.mover(event))
        self.hilo_actualizador=threading.Thread(name="actualizar",target=self.actualizar)
        self.hilo_actualizador.start()
        self.hilo_mainloop=threading.Thread(name="mainloop",target=self.ventana.mainloop())
        self.hilo_mainloop.start()

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
        mensaje=[]
        mensaje.append("inicio")
        mensaje.append(self.inicio_y)
        mensaje.append(self.minimo_y)
        mensaje.append(self.maximo_y)
        mensaje.append(0)
        self.socket.sendto(pickle.dumps(mensaje), (self.ip, 8000))

    def actualizar(self):
        'conexion de recive'
        while True:
            self.valores = self.conexion.recv(1024)
            self.valores=pickle.loads(self.valores)
            print(self.valores)
            self.canvas.move(self.canvas.find_withtag(self.jugador),0,self.valores[4])

            self.canvas.move(self.pelota ,self.valores[5],self.valores[6])
            'self.conexion.send("si".encode())'
        self.conexion.close()


pg=pong_game(socket.gethostbyname(socket.gethostname()),"j1")