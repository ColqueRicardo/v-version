import socket
import pickle
import threading
import time
import random

class servidor():
    def __init__(self,ip1,ip2):
        print("inicio servidor")
        self.ip=[]
        self.ip.append(ip1)
        self.ip.append(ip2)

        self.bandera=0

        'self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)'

        'self.ip=socket.gethostbyname(socket.gethostname())'
        'velocidad de los objetos'
        self.jugador_velocidad=0
        self.vel_x=0
        self.vel_y=0


        self.puerto_recive_j1=8000
        self.puerto_enviar_j1=8001

        self.puerto_recive_j2=8002
        self.puerto_enviar_j2=8003


        self.velocidad_jugador()
        'variables usadas en el envio / recive'
        '''self.socket_envia=[]
        self.socket_recive=[]'''




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


        'self.conexion(0,8001,8000)'
        self.establecer_conexion()

        while True:

            if self.bandera==2:
                print("se an iniciado las 2")
                break
        self.hilo_pelota_movimiento=threading.Thread(name="movimiento",target=self.movimiento)
        self.hilo_pelota_movimiento.start()



    def establecer_conexion(self):
        '''self.puerto_recive_j1=8000
        self.puerto_enviar_j1=8001
        self.puerto_recive_j2=8002
        self.puerto_enviar_j2=8003'''

        self.hilo_conexion1=threading.Thread(name=self.ip[0],target=self.conexion_j1)
        self.hilo_conexion2 = threading.Thread(name=self.ip[1], target=self.conexion_j2)
        self.hilo_conexion1.start()
        self.hilo_conexion2.start()
    def conexion_j1(self):
        'para j1'
        'envia'
        while True:
            try:
                self.socket_envia_j1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_envia_j1.connect((self.ip[0], self.puerto_enviar_j1))
                break
            except:

                ''
        'se establece el recive'
        self.socket_recive_j1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_recive_j1.bind((self.ip[0], self.puerto_recive_j1))
        self.socket_recive_j1.listen(1)
        self.conexion_recive_j1, self.direccion_recive_j1 = self.socket_recive_j1.accept()
        self.bandera+=1
        'inicia el revice . envia del j1'
        self.hilo_recive=threading.Thread(name="recive",target=self.recive_j1)
        self.hilo_recive.start()
        self.hilo_envia=threading.Thread(name="envia",target=self.envia_j1)
        self.hilo_envia.start()

    def conexion_j2(self):
        'para j2'
        'envia'
        while True:
            try:
                self.socket_envia_j2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_envia_j2.connect((self.ip[1], self.puerto_enviar_j2))
                break
            except:
                ''
        'se establece el recive'
        self.socket_recive_j2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_recive_j2.bind((self.ip[1], self.puerto_recive_j2))
        self.socket_recive_j2.listen(1)
        self.conexion_recive_j2, self.direccion_recive_j2 = self.socket_recive_j2.accept()
        self.bandera+=1
        'inicia el recive-envia j2'
        self.hilo_recive=threading.Thread(name="recive",target=self.recive_j2)
        self.hilo_recive.start()
        self.hilo_envia=threading.Thread(name="envia",target=self.envia_j2)
        self.hilo_envia.start()
    def velocidad_jugador(self):
        self.jugador_velocidad+=10
    def movimiento(self):
        print("inicia movimiento")
        while True:
            self.velocidad(random.randint(0, 4))
            break
        while True:

            'posicion actual'
            self.pelota_posicion[0] += self.vel_x
            self.pelota_posicion[1] += self.vel_y
            print(self.pelota_posicion)
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

    def envia_j1(self):
        'para j1'
        print("inicia envio j1")
        while True:
            'envia posicion de jugador 1 y polota posicion'
            self.socket_envia_j1.sendto(pickle.dumps(self.jugador_posicion+self.pelota_posicion), (self.ip[0], self.puerto_enviar_j1))
            time.sleep(0.1)
            '''if (self.socket.recv(1024).decode()!="si"):
                break'''
        self.socket_envia[0].close()
    def recive_j1(self):
        'para _j1'
        print("inicia recive j1")

        while True:

            self.peticion = self.conexion_recive_j1.recv(1024).decode()
            print(self.peticion)
            if self.peticion == "arriba" and self.jugador_posicion[0]>=self.tope_arriba :
                self.jugador_posicion[0]+=-self.jugador_velocidad
            if self.peticion == "abajo" and self.jugador_posicion[0]<=self.tope_abajo_jugador:
                self.jugador_posicion[0]+=self.jugador_velocidad

        self.coneccion_recive.close()

    def envia_j2(self):
        'para _j2'
        print("inicia envio j1")
        while True:
            'envia posicion de jugador 1 y polota posicion'
            self.socket_envia_j2.sendto(pickle.dumps(self.jugador_posicion+self.pelota_posicion), (self.ip[0], self.puerto_enviar_j2))
            time.sleep(0.1)
            '''if (self.socket.recv(1024).decode()!="si"):
                break'''
        self.socket_envia_j2.close()
    def recive_j2(self):
        'para j2'
        print("inicia recive j1")

        while True:

            self.peticion = self.conexion_recive_j2.recv(1024).decode()
            print(self.peticion)
            if self.peticion == "arriba" and self.jugador_posicion[1]>=self.tope_arriba :
                self.jugador_posicion[1]+=-self.jugador_velocidad
            if self.peticion == "abajo" and self.jugador_posicion[1]<=self.tope_abajo_jugador:
                self.jugador_posicion[1]+=self.jugador_velocidad

        self.coneccion_recive.close()

servidor = servidor(socket.gethostbyname(socket.gethostname()),socket.gethostbyname(socket.gethostname()))
