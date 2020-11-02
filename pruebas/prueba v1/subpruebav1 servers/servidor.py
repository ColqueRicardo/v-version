import socket
import threading
import time
class server():
    def __init__(self):
        self.ip=socket.gethostbyname(socket.gethostname())
        self.fin=0
        'establece conexion'
        while True:
            try:
                puerto=8000
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.s.connect((self.ip  ,puerto))
                print("se conexto envia")
                break
            except:

                print("sigue")



        puerto=8001
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip,puerto))
        self.server.listen(1)
        self.conexion, self.direccion = self.server.accept()
        'se establecio recive'
        'fin de establece conexion'

        self.comprobacion=0
        self.hilo1=threading.Thread(name="1",target=self.envia)
        self.hilo1.start()
        self.hilo2=threading.Thread(name="1",target=self.recive)
        self.hilo2.start()
        print("inicio")
    def recive(self):
        while True:
            peticion = self.conexion.recv(1024).decode()
            print(peticion)

            if (self.fin==1):
                break
        self.conexion.close()
    def envia(self):
        while True:
            self.s.send("mensaje ".encode('utf-8'))
            print("se a enviado el mensaje")
            time.sleep(1)
            if self.comprobacion==1:
                break
        self.s.close()

h=server()