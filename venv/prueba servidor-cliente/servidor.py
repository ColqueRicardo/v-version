from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import socket
import sys
import datetime
from tkinter import messagebox
import time
import threading
import random
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")
from prueba import *

class pong():
    def __init__(self):
        self.jugadores_id=0
        'dimenciones x,y de los jugadores'
        self.dimenciones=[["",""],["",""]]
        self.tamaño_barra=[]

        'int(self.ventana.winfo_screenheight())'
        xy = "{0}x{0}+" +"0" + "+" + "0"
        '        self.ventana.geometry((xy.format(500, 500)))'

        self.velocidad_jugador=0.5

        self.direccion=random.randint(0,3)

        'donde inicia la barra'
        self.inicio_jugadores=[]

        self.turno=random.randint(0,1)

        self.velocidad_pelota_x=15
        self.velocidad_pelota_y=20
        'se define todo en el inicio de secion'
        '''        self.pelota_x=[self.dimenciones[0]//2],[self.dimenciones[2]//2]
        self.pelota_y=[self.dimenciones[1]//2],[self.dimenciones[3]//2]
        '''
        self.pelota_posicion=[[0,0],[0,0]]
        self.puntuacion_jugadores=[0],[0]

        self.timer=time
        '''
        self.servidor.hilo= threading.Timer(0.01,self.servidor_ejecucion())
        self.servidor.hilo.start()

        '''
        self.servidor_ejecucion()
        '''self.hilo_tiempo = threading.Timer(1, lambda: self.tiempo_ejecucion())
        self.hilo_tiempo.start()
        self.hilo_mainloop=threading.Thread(self.ventana.mainloop())
        self.hilo_mainloop.start()
        '''
    def servidor_ejecucion(self):
        print("empieza")
        s = socket.socket()
        s.bind(('localhost', 8000))
        s.listen(20)
        while True:
            conexion, direccion = s.accept()
            peticion = conexion.recv(1024).decode()
            peticion=decoficar_mensaje(peticion)

            if peticion[0] == "jugador esperando" and self.jugadores_id<2:


                self.dimenciones[self.jugadores_id][0]=peticion[1]
                self.dimenciones[self.jugadores_id][1]=peticion[2]

                self.tamaño_barra.append(int(self.dimenciones[self.jugadores_id][1])//5)

                self.inicio_jugadores.append(int(self.dimenciones[self.jugadores_id][1])//2)
                self.inicio_jugadores.append(int(self.dimenciones[self.jugadores_id][1])//2)


                self.pelota_posicion[self.jugadores_id][0]=int(self.dimenciones[self.jugadores_id][0]) // 2
                self.pelota_posicion[self.jugadores_id][1]=int(self.dimenciones[self.jugadores_id][1]) // 2


                self.pelota_posicion[self.jugadores_id+1][0]=int(self.dimenciones[self.jugadores_id][0]) // 2
                self.pelota_posicion[self.jugadores_id+1][1]=int(self.dimenciones[self.jugadores_id][1]) // 2


                mensaje=["se puede"],[self.jugadores_id],[self.tamaño_barra[self.jugadores_id]],[self.inicio_jugadores[0]],[self.inicio_jugadores[1]]

                self.jugadores_id=self.jugadores_id+1

                conexion.send(codificar_mensaje(mensaje))

            elif peticion[0] == "abajo":
                self.inicio_jugadores[int(peticion[1])] =int( self.inicio_jugadores[int(peticion[1])] + (10 * self.velocidad_jugador))
                print(codificar_mensaje([self.inicio_jugadores[int(peticion[1])]]),"arriba")
                conexion.send(codificar_mensaje([self.inicio_jugadores[int(peticion[1])]]))
            elif peticion[0] == "arriba":
                self.inicio_jugadores[int(peticion[1])] = int(self.inicio_jugadores[int(peticion[1])] - (10 * self.velocidad_jugador))
                print(codificar_mensaje([self.inicio_jugadores[int(peticion[1])]]),"abajo")
                conexion.send(codificar_mensaje([self.inicio_jugadores[int(peticion[1])]]))
            elif peticion[0]=="actualizar":

                respuesta=[self.inicio_jugadores[0]],[self.inicio_jugadores[1]],[self.pelota_posicion[int(peticion[1])][0]],[self.pelota_posicion[int(peticion[1])][1]]
                conexion.send(codificar_mensaje(respuesta))
                print(respuesta,"actualizar")
            conexion.close()

    def mover(self,event,jugador):
        if event.char=="s":
            if self.inicio_jugadores[jugador]<self.dimenciones[(jugador+1)*2]*0.8:
                self.inicio_jugadores[jugador]=self.inicio_jugadores[jugador]+(10*self.velocidad_jugador)

                return str(self.inicio_jugadores[jugador])
            else:
                return "muy abajo"
        elif event.char=="w":
            if self.inicio_jugadores[jugador]<self.dimenciones[(jugador+1)*2]*0.8:
                self.inicio_jugadores[jugador] = self.inicio_jugadores[jugador] - (10 * self.velocidad_jugador)

                return str(self.inicio_jugadores[jugador])
            else:
                return "muy arriba"

    def tiempo_ejecucion(self):
        while self.puntuacion_j1 < 10 and self.puntuacion_j2 < 10:
            if self.turno == "jugador1":
                self.choque_margen_x()
                self.timer.sleep(0.05)


    def choque_margen_x(self):
        y=self.pelota_y-self.pelota_y_ant
        x=self.pelota_x-self.pelota_x_ant
        self.canvas.delete("pelota")

        if self.y-150<=self.pelota_y:
            if self.direccion==3:
                self.direccion =1
                self.mover_pelota()

                print("paso por 1")

            elif self.direccion==2:
                self.direccion =0
                self.mover_pelota()

                print("paso por 2")
        elif self.pelota_y<30:
            if self.direccion==1:
                self.cambio_direccion(3)
                self.mover_pelota()
                print("paso por 3")
            elif self.direccion==0:
                self.cambio_direccion(2)
                self.mover_pelota()
                print("paso por 4")
        if self.x-30<self.pelota_x:
            if self.direccion==1:
                self.cambio_direccion(0)
                self.mover_pelota()
                print("paso por 5")
            elif self.direccion==3:
                self.cambio_direccion(2)
                self.mover_pelota()
                print("paso por 6")

        if self.pelota_y>=self.inicio_j1_y and self.pelota_y<=self.inicio_j1_y+200 and self.pelota_x<=50 and self.pelota_x>40:
            print("paso por aqui xd")
            if self.direccion==0:
                self.cambio_direccion(1)
                self.mover_pelota()
            elif self.direccion==2:
                self.cambio_direccion(3)
                self.mover_pelota()
        if self.pelota_x<30:
            print("punto para el j1")


        if self.y-150>=self.pelota_y and self.pelota_y>30 and self.x-30>self.pelota_x and self.pelota_x>=30:
                print("paso por 9")
                self.mover_pelota()
        'self.canvas.create_line(50, self.inicio_j1_y, 50, self.inicio_j1_y + 200, fill="white", width=15, tags="jugador1")'

    def mover_pelota(self):
        y=self.pelota_y-self.pelota_y_ant
        x=self.pelota_x-self.pelota_x_ant
        self.pelota_y_ant=self.pelota_y
        self.pelota_x_ant=self.pelota_x

        if x<0:
            x=x*-1
        if y<0:
            y=y*-1
        if self.direccion==0:
            self.pelota_y = self.pelota_y_ant - y
            self.pelota_x = self.pelota_x_ant - x
        elif self.direccion==1:
            self.pelota_y = self.pelota_y_ant - y
            self.pelota_x = self.pelota_x_ant + x
        elif self.direccion==2:
            self.pelota_y = self.pelota_y_ant + y
            self.pelota_x = self.pelota_x_ant - x
        elif self.direccion==3:
            self.pelota_y = self.pelota_y_ant + y
            self.pelota_x = self.pelota_x_ant + x

        self.canvas.create_rectangle(self.pelota_x - 15, self.pelota_y - 15, self.pelota_x + 15, self.pelota_y + 15,
                                     fill="white", tags="pelota")
    def cambio_direccion(self,direccion):
        self.direccion=direccion
        self.velocidad_pelota_y=random.randint(10,25)
        self.velocidad_pelota_y=random.randint(10,25)
pong = pong()
'''
root = Tk()

def key(event,ro):
    print ("pressed", repr(event.char))
    print(ro)
def callback(event):
    print ("clicked at", event.x, event.y)

print(root)
canvas= Canvas(root)
canvas.place(x=0,y=0,height=100,width=100)
canvas.focus_set()
canvas.bind("<Key>",lambda event: key(event,root))
canvas.bind("<Button-1>",  callback)
canvas.pack()

root.mainloop()
'''