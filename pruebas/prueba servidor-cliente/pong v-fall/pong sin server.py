from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import socket
import sys
import datetime
from tkinter import messagebox
import time
import threading
import random
'sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")'
from prueba import *
import keyboard

class pong():
    def __init__(self):



        self.ventana=Tk()

        self.x = int(self.ventana.winfo_screenwidth())
        self.y = int(self.ventana.winfo_screenheight())

        xy = "{0}x{0}+" +"0" + "+" + "0"
        self.ventana.geometry((xy.format(self.x, self.y)))



        'dimenciones x,y de los jugadores'
        self.tamaño_barra=self.y*0.2

        'int(self.ventana.winfo_screenheight())'
        xy = "{0}x{0}+" +"0" + "+" + "0"
        '        self.ventana.geometry((xy.format(500, 500)))'

        self.velocidad_jugador=1

        self.direccion=random.randint(0,3)

        'donde inicia la barra'
        self.inicio_j1_y=int((self.y//3)*2)
        self.inicio_j2_y = int((self.y // 3) * 2)
        self.velocidad_pelota_x=15
        self.velocidad_pelota_y=20

        self.puntuacion_j1=0
        self.puntuacion_j2=0

        'se define todo en el inicio de secion'
        '''        self.pelota_x=[self.dimenciones[0]//2],[self.dimenciones[2]//2]
        self.pelota_y=[self.dimenciones[1]//2],[self.dimenciones[3]//2]
        '''
        self.pelota_posicion_x=int((self.x//2))
        self.pelota_posicion_y=int((self.y//2))

        'margenes'
        self.margen_y_arriba=(self.y*0.02)
        self.margen_y_abajo=(self.y*0.9)
        self.margen_x_izquierdo=30
        self.margen_x_derecho=self.x-30

        self.timer=time
        '''
        self.servidor.hilo= threading.Timer(0.01,self.servidor_ejecucion())
        self.servidor.hilo.start()

        '''
        '''self.hilo_tiempo = threading.Timer(1, lambda: self.tiempo_ejecucion())
        self.hilo_tiempo.start()
        self.hilo_mainloop=threading.Thread(self.ventana.mainloop())
        self.hilo_mainloop.start()
        '''

        self.canvas= Canvas(self.ventana,bg="black")
        self.canvas.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.canvas.focus_set()

        self.canvas.create_line(self.margen_x_izquierdo, self.inicio_j1_y ,self.margen_x_izquierdo, self.inicio_j1_y+self.tamaño_barra ,fill="white",width=15,tags="jugador1")
        self.canvas.create_line(self.margen_x_derecho,self.inicio_j2_y ,self.margen_x_derecho, self.inicio_j2_y+self.tamaño_barra ,fill="white",width=15,tags="jugador2")
        self.canvas.create_rectangle(self.pelota_posicion_x,self.pelota_posicion_y,self.pelota_posicion_x+25,self.pelota_posicion_y+25,fill="white",tags="pelota")

        self.canvas.create_line(self.margen_x_izquierdo,self.margen_y_arriba,self.margen_x_derecho,self.margen_y_arriba,fill="white",width=5)
        self.canvas.create_line(self.margen_x_izquierdo, self.margen_y_abajo, self.margen_x_derecho,
                                self.margen_y_abajo,fill="white",width=5)

        '''self.hilo_j1= threading.Thread(self.canvas.bind("<Key>",lambda event:self.mover_j1(event)))

        self.hilo_j2 = threading.Thread(self.canvas.bind("<Key>", lambda event: self.mover_j2(event)))

        self.hilo_j1.start()
        self.hilo_j2.start()
        '''
        self.canvas.bind("<Key>", lambda event: self.mover(event))
        '''
        self.hilo_escuchaj2=threading.Thread(target=self.mover_jugador2())
        self.hilo_escuchaj2.start()
        '''
        self.hilo_actualizar= threading.Thread(target=self.tiempo_ejecucion)
        self.hilo_actualizar.start()

        '''        self.hilo_movimiento_jugadores=threading.Thread(target=self.mover)
        self.hilo_movimiento_jugadores.start()'''


        self.hilo_mainloop= threading.Thread(target= self.ventana.mainloop())

        self.hilo_mainloop.start()

    def tiempo_ejecucion(self):
        print("inicio hilo t_eje")
        while self.puntuacion_j1 < 10 and self.puntuacion_j2 < 10:
            self.choque_margen()
            self.timer.sleep(0.05)

    def mover_j1(self,event):
        if event.char=="w":
            self.mover_jugador1_arriba()
        if event.char=="s":
            self.mover_jugador1_abajo()

    def mover_j2(self, event):
        if event.char == "i":
            self.mover_jugador2_arriba()
        if event.char == "k":
            self.mover_jugador2_abajo()

    def mover(self,event):
        '''
        cambiar a lo de arriba de vuelta
        self.hilo_jugador1=threading.Thread(self.mover_jugador1(event.char))
        self.hilo_jugador2=threading.Thread(self.mover_jugador2(event.char))
                self.mover_jugador1(event.char)
        self.mover_jugador2(event.char)
        '''
        '''        while TRUE:
            if keyboard.is_pressed("w"):
                print("uppp")
                sys.exit(0)'''

        if event.char=="w":

            self.mover_jugador1_arriba()
        if event.char=="s":
            self.mover_jugador1_abajo()
        '''
        if event.char == "u":
            self.mover_jugador2_arriba()
        if event.char == "j":
            self.mover_jugador2_abajo()'''
    def mover_jugador2(self):
        while self.puntuacion_j2<10 and self.puntuacion_j1<10:
            if keyboard.is_pressed("u"):
                self.mover_jugador2_arriba()
            if keyboard.is_pressed("j"):
                self.mover_jugador2_abajo()

    def mover_jugador1_abajo(self):
        if self.inicio_j1_y<self.margen_y_abajo-self.tamaño_barra:
            self.inicio_j1_y=self.inicio_j1_y+(10*self.velocidad_jugador)
            'self.canvas.move(self.canvas.find_withtag("jugador1"),0, 10*self.velocidad_jugador)'
            self.canvas.delete(self.canvas.find_withtag("jugador1"))
            self.canvas.create_line(self.margen_x_izquierdo, self.inicio_j1_y    , self.margen_x_izquierdo, self.inicio_j1_y +self.tamaño_barra, fill="white", width=15,
                                    tags="jugador1")
        else:
            print("muy abajo")
    def mover_jugador1_arriba(self):
        if self.inicio_j1_y>self.margen_y_arriba:
            self.inicio_j1_y= self.inicio_j1_y - (10 * self.velocidad_jugador)
            'self.canvas.move(self.canvas.find_withtag("jugador1"),0,- (10 * self.velocidad_jugador))'
            self.canvas.delete(self.canvas.find_withtag("jugador1"))
            self.canvas.create_line(self.margen_x_izquierdo, self.inicio_j1_y, self.margen_x_izquierdo, self.inicio_j1_y + self.tamaño_barra, fill="white",
                                    width=15,
                                    tags="jugador1")
        else:
            print("muy arriba")


    def mover_jugador2_abajo(self):
        if self.inicio_j2_y<self.margen_y_abajo-self.tamaño_barra:
            self.inicio_j2_y=self.inicio_j2_y+(10*self.velocidad_jugador)
            'self.canvas.move(self.canvas.find_withtag("jugador1"),0, 10*self.velocidad_jugador)'
            self.canvas.delete(self.canvas.find_withtag("jugador2"))
            self.canvas.create_line(self.margen_x_derecho, self.inicio_j2_y    , self.margen_x_derecho, self.inicio_j2_y +self.tamaño_barra, fill="white", width=15,
                                        tags="jugador2")
        else:
            print("muy abajo")
    def mover_jugador2_arriba(self):
        if self.inicio_j2_y>self.margen_y_arriba:
            self.inicio_j2_y= self.inicio_j2_y - (10 * self.velocidad_jugador)
            'self.canvas.move(self.canvas.find_withtag("jugador1"),0,- (10 * self.velocidad_jugador))'
            self.canvas.delete(self.canvas.find_withtag("jugador2"))
            self.canvas.create_line(self.margen_x_derecho, self.inicio_j2_y, self.margen_x_derecho, self.inicio_j2_y + self.tamaño_barra, fill="white",
                                        width=15,
                                        tags="jugador2")
        else:
            print("muy arriba")
        'print(self.inicio_j1_y,self.y*0.2,self.y*0.8)'

    def cambio_direccion(self,direccion):
        self.direccion=direccion
        self.velocidad_pelota_y=random.randint(10,25)
        self.velocidad_pelota_y=random.randint(10,25)

    def choque_margen(self):
        'print(self.pelota_posicion_x,self.pelota_posicion_y,self.margen_y_abajo,self.margen_y_arriba)'
        self.mover_pelota()
        if self.margen_y_abajo<=self.pelota_posicion_y:
            if self.direccion==3:
                self.cambio_direccion(1)

            elif self.direccion==2:
                self.cambio_direccion(0)
        elif self.pelota_posicion_y<self.margen_y_arriba:
            if self.direccion==1:
                self.cambio_direccion(3)
            elif self.direccion==0:
                self.cambio_direccion(2)
        if self.margen_x_derecho<self.pelota_posicion_x:
            if self.direccion==1:
                self.cambio_direccion(0)
            elif self.direccion==3:
                self.cambio_direccion(2)
        if self.pelota_posicion_y>=self.inicio_j1_y and self.pelota_posicion_y<=self.inicio_j1_y*self.tamaño_barra and self.pelota_posicion_x<=self.margen_x_izquierdo+2:
            print("paso por aqui xd")
            if self.direccion==0:
                self.cambio_direccion(1)
                self.mover_pelota()
            elif self.direccion==2:
                self.cambio_direccion(3)
                self.mover_pelota()
        if self.pelota_posicion_x<15    :
            print("punto para el j1")
            sys.exit(0)


        '        if self.margen_y_abajo>=self.pelota_posicion_y and self.pelota_posicion_y>self.margen_y_arriba and self.margen_x_derecho>self.pelota_posicion_x and self.pelota_posicion_x>=self.margen_x_izquierdo:'


        'self.canvas.create_line(50, self.inicio_j1_y, 50, self.inicio_j1_y + 200, fill="white", width=15, tags="jugador1")'

        print(self.inicio_j1_y,self.inicio_j1_y*1.2,self.pelota_posicion_x,self.pelota_posicion_y)
    def mover_pelota(self):
        if self.direccion==0:
            self.pelota_posicion_y = self.pelota_posicion_y - self.velocidad_pelota_y
            self.pelota_posicion_x = self.pelota_posicion_x - self.velocidad_pelota_x
            'self.canvas.move(self.canvas.find_withtag("pelota"), -self.velocidad_pelota_x, -self.velocidad_pelota_y)'
            self.canvas.delete(self.canvas.find_withtag("pelota"))
            self.canvas.create_rectangle(self.pelota_posicion_x, self.pelota_posicion_y, self.pelota_posicion_x + 25,
                                         self.pelota_posicion_y + 25, fill="white", tags="pelota")

        elif self.direccion==1:
            self.pelota_posicion_y = self.pelota_posicion_y - self.velocidad_pelota_y
            self.pelota_posicion_x = self.pelota_posicion_x + self.velocidad_pelota_x
            'self.canvas.move(self.canvas.find_withtag("pelota"), self.velocidad_pelota_x, -self.velocidad_pelota_y)'
            self.canvas.delete(self.canvas.find_withtag("pelota"))
            self.canvas.create_rectangle(self.pelota_posicion_x, self.pelota_posicion_y, self.pelota_posicion_x + 25,
                                         self.pelota_posicion_y + 25, fill="white", tags="pelota")

        elif self.direccion==2:
            self.pelota_posicion_y = self.pelota_posicion_y+ self.velocidad_pelota_y
            self.pelota_posicion_x = self.pelota_posicion_x- self.velocidad_pelota_x
            'self.canvas.move(self.canvas.find_withtag("pelota"), -self.velocidad_pelota_x, self.velocidad_pelota_y)'
            self.canvas.delete(self.canvas.find_withtag("pelota"))
            self.canvas.create_rectangle(self.pelota_posicion_x, self.pelota_posicion_y, self.pelota_posicion_x + 25,
                                         self.pelota_posicion_y + 25, fill="white", tags="pelota")

        elif self.direccion==3:
            self.pelota_posicion_y = self.pelota_posicion_y + self.velocidad_pelota_y
            self.pelota_posicion_x = self.pelota_posicion_x + self.velocidad_pelota_x
            'self.canvas.move(self.canvas.find_withtag("pelota"), self.velocidad_pelota_x, self.velocidad_pelota_y)'
            self.canvas.delete(self.canvas.find_withtag("pelota"))
            self.canvas.create_rectangle(self.pelota_posicion_x, self.pelota_posicion_y, self.pelota_posicion_x + 25,
                                         self.pelota_posicion_y + 25, fill="white", tags="pelota")


        '''
        self.canvas.create_rectangle(self.pelota_x - 15, self.pelota_y - 15, self.pelota_x + 15, self.pelota_y + 15,
                                     fill="white", tags="pelota")'''
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