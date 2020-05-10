import socket
import pickle
import threading
import time
import random

class servidor():
    def __init__(self,ip1,ip2):
        self.ip=[]
        self.ip.append(ip1)
        self.ip.append(ip2)

        'self.ip=socket.gethostbyname(socket.gethostname())'
        'velocidad de los objetos'
        self.jugador_velocidad=0




        self.velocidad_jugador()
        'variables usadas en el envio / recive'
        self.socket_envia=[]
        self.socket_recive=[]
        '''self.coneccion_envia=[]
        self.direccion_envia=[]
        self.coneccion_recive=[]
        self.direccion_recive=[]'''



        '''x = self.ventana.winfo_screenwidth()
        y = self.ventana.winfo_screenheight()'''
        self.jugador_posicion=[]
        self.jugador_posicion.append((800*0.8)*0.25)
        self.jugador_posicion.append((800 * 0.8) * 0.25)
        self.tope_izquierda=(1500*0.8)*0.1
        self.tope_derecha=(1500*0.8)*0.9
        self.tope_arriba=(800*0.8)*0.1
        self.tope_abajo=800*0.8*0.9
        'el tope de abajo tiene q considerar el tamaño de la barra '
        self.tamaño_barra=800*0.8*0.5
        self.tope_abajo_jugador=((800*0.8)*0.9)-self.tamaño_barra



        x=(1500*0.8)//2
        y=(800*0.8)//2

        t=x*0.01

        self.pelota_posicion=[]
        self.pelota_posicion.append(x-t)
        self.pelota_posicion.append(y-t)


        self.conexion(0,8001,8000)
        self.hilo_pelota_movimiento=threading.Thread(name="movimiento",target=self.movimiento)
        self.hilo_pelota_movimiento.start()
        self.hilo_recive=threading.Thread(name="recive",target=self.recive,args={0,8000})
        self.hilo_recive.start()
        self.hilo_envia=threading.Thread(name="envia",target=self.envia,args={0,8001})
        self.hilo_envia.start()


    def establecer_conexion(self):
        self.hilo_conexion1=threading.Thread(name=self.ip[0],target=self.conexion(0,8000,8001))

    def conexion(self,id,puerto1,puerto2):
        while True:
            try:
                self.socket_envia.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                self.socket_envia[id].connect((self.ip[id], puerto1))
                break
            except:
                ''
        'se establece el recive'
        self.socket_recive.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.socket_recive[id].bind((self.ip[id], puerto2))
        self.socket_recive[id].listen(1)
        self.conexion_recive, self.direccion_recive = self.socket_recive[id].accept()

    def velocidad_jugador(self):
        self.jugador_velocidad+=10
    def movimiento(self):
        while True:
            self.velocidad(random.randint(0, 4))
            break
        while True:

            'posicion actual'
            self.pelota_posicion[0] += self.vel_x
            self.pelota_posicion[1] += self.vel_y


            '''print("esto se ejecuta", self.pelota_posicion ,self.pelota_movimiento,"x",self.vel_x,"y",self.vel_y)
            print("derecha",self.tope_derecha,"izquierda",self.tope_izquierda,"arriba",self.tope_arriba,"abajo,",self.tope_abajo)'''

            if self.pelota_posicion[1]>=self.tope_abajo:
                if self.direccion==2:
                    self.velocidad(0)
                elif self.direccion==3:
                    self.velocidad(1)
            if self.pelota_posicion[1]<=self.tope_arriba:
                if self.direccion==0:
                    self.velocidad(2)
                elif self.direccion==1:
                    self.velocidad(3)
            if self.pelota_posicion[0]>=self.tope_derecha:
                if self.direccion==1:
                    self.velocidad(0)
                elif self.direccion==3:
                    self.velocidad(2)
            if self.pelota_posicion[0]<= self.tope_izquierda:
                if self.direccion==0:
                    self.velocidad(1)
                elif self.direccion==2:
                    self.velocidad(3)
            time.sleep(1)

    def velocidad(self,dir):
        'cambia la direccion accionando por la velocidad'
        self.direccion=dir
        if self.direccion==0:
            self.vel_x=random.randint(20,51)*-1
            self.vel_y=random.randint(20,51)*-1
        elif self.direccion==1:
            self.vel_x = random.randint(20, 51)
            self.vel_y = random.randint(20, 51) *-1
        elif self.direccion==2:
            self.vel_x = random.randint(20, 51) *-1
            self.vel_y = random.randint(20, 51)
        elif self.direccion==3:
            self.vel_x = random.randint(20, 51)
            self.vel_y = random.randint(20, 51)

    def envia(self,id,puerto):
        while True:
            'envia posicion de jugador 1 y polota posicion'
            self.socket_envia[id].sendto(pickle.dumps(self.jugador_posicion+self.pelota_posicion), (self.ip[id], puerto))
            'print(self.jugador_posicion+self.pelota_posicion)'
            time.sleep(0.1)
            '''if (self.socket.recv(1024).decode()!="si"):
                break'''
        self.socket_envia[id].close()
    def recive(self,id,puerto):

        while True:

            self.peticion = self.conexion_recive.recv(1024).decode()
            if self.peticion == "arriba" and self.jugador_posicion[id]>=self.tope_arriba :
                self.jugador_posicion[id]+=-self.jugador_velocidad
                self.jugador_posicion[id+1]+=-self.jugador_velocidad
            if self.peticion == "abajo" and self.jugador_posicion[id]<=self.tope_abajo_jugador:
                self.jugador_posicion[id]+=self.jugador_velocidad
                self.jugador_posicion[id+1]+=self.jugador_velocidad

        self.coneccion_recive.close()

servidor = servidor(socket.gethostbyname(socket.gethostname()),socket.gethostbyname(socket.gethostname()))
