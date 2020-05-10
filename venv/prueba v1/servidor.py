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

        self.jugador_velocidad=0

        self.velocidad_jugador()
        'variables usadas en el envio / recive'
        self.socket_envia=[]
        self.socket_recive=[]
        self.socket_coneccion=[]
        self.socket_direccion=[]




        '''x = self.ventana.winfo_screenwidth()
        y = self.ventana.winfo_screenheight()'''
        self.jugador_posicion=[]
        self.jugador_posicion.append((800*0.8)*0.25)
        self.jugador_posicion.append((800 * 0.8) * 0.25)
        self.tope_izquierda=(1500*0.8)*0.1
        self.tope_derecha=(1500*0.8)*0.9
        self.tope_arriba=(800*0.8)*0.1
        self.tope_abajo=(800*0.8)*0.9

        x=(1500*0.8)//2
        y=(800*0.8)//2

        t=x*0.01

        self.pelota_posicion=[]
        self.pelota_posicion.append(x-t)
        self.pelota_posicion.append(y-t)
        self.pelota_movimiento=[]
        self.pelota_movimiento.append(0)
        self.pelota_movimiento.append(0)

        self.establecer_conexion()

        self.hilo_pelota_movimiento=threading.Thread(name="movimiento",target=self.movimiento)
        self.hilo_pelota_movimiento.start()
        self.hilo_recive=threading.Thread(name="recive",target=self.recive)
        self.hilo_recive.start()
        self.hilo_envia=threading.Thread(name="envia",target=self.envia)
        self.hilo_envia.start()
        '''self.s=threading.Timer(0.5,function=self.ss())
        self.s.start()'''

    def establecer_conexion(self):
        self.hilo_conexion1=threading.Thread(name=self.ip1)

    def conexion(self,id,puerto1,puerto2):
        while True:
            try:
                self.socket_envia.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
                self.socket_envia[id].connect((self.ip[id], puerto1))
                break
            except:
                ''
        'se establece el recive'
        self.socket_recive.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_recive[id].bind((self.ip, 8000))
        self.socket_recive[id].listen(1)

        self.conexion, self.direccion = self.s.accept()


    '''    def establecer_conexion(self):
        'se establece el envia'
        while True:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.ip, 8001))
                break
            except:
                ''
        'se establece el recive'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, 8000))
        self.s.listen(1)
        self.conexion, self.direccion = self.s.accept()
    '''


    def velocidad_jugador(self):
        self.jugador_velocidad+=10
    def movimiento(self):
        self.velocidad(random.randint(0, 4))
        while True:

            'posicion actual'
            self.pelota_posicion[0] += self.vel_x
            self.pelota_posicion[1] += self.vel_y
            'movimiento actual'
            self.pelota_movimiento[0]+= self.vel_x
            self.pelota_movimiento[1]+= self.vel_y

            print("esto se ejecuta", self.pelota_posicion ,self.pelota_movimiento,"x",self.vel_x,"y",self.vel_y)
            print("derecha",self.tope_derecha,"izquierda",self.tope_izquierda,"arriba",self.tope_arriba,"abajo,",self.tope_abajo)

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
        print(self.vel_x,self.vel_y)

    0


    def envia(self):
        while True:
            'envia posicion de jugador 1 y polota posicion'
            self.socket.sendto(pickle.dumps(self.valores+self.pelota_movimiento ), (self.ip, 8001))
            self.valores[4]=0
            self.pelota_movimiento[0]=0
            self.pelota_movimiento[1]=0
            time.sleep(0.1)
            '''if (self.socket.recv(1024).decode()!="si"):
                break'''
        self.socket.close()
    def recive(self):
        self.valores = []
        self.peticion = self.conexion.recv(1024)
        self.valores = pickle.loads(self.peticion)

        while True:
            self.peticion = self.conexion.recv(1024).decode()
            'print(self.peticion)'
            '''if (self.peticion!=""):
                print(self.peticion)
                print(self.valores[1])
                print(self.valores[2])
                print(self.valores[3])'''
            if self.peticion == "arriba" and self.valores[1]>=self.valores[2]:
                self.valores[1]+=-self.jugador_velocidad
                self.valores[4]+=-self.jugador_velocidad
                'self.conexion.send("arriba".encode())'
                'print("arriba")'
            if self.peticion == "abajo" and self.valores[1]<=self.valores[3]:
                self.valores[1]+=self.jugador_velocidad
                self.valores[4]+=self.jugador_velocidad
                'self.conexion.send("abajo".encode())'
                'print("abajo")'
            'self.conexion.send("sdadsa".encode())'
        self.conexion.close()

servidor = servidor()

'''s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()) ,8000))
s.listen(1)
print("empezo")
print("coneccion nueva")
conexion, direccion = s.accept()
valores=[]
while True:
    peticion = conexion.recv(1024)
    peticion=pickle.loads(peticion)
    if peticion[0]=="inicio":
        print("inicio")
        valores=peticion
        conexion.send(pickle.dumps("inicio"))
    if peticion=="arriba":
        print("arriba")
        conexion.send(pickle.dumps("arriba"))
    if peticion=="abajo":
        print("abajo")
        conexion.send(pickle.dumps("abajo"))
    print(peticion)
conexion.close()
'''