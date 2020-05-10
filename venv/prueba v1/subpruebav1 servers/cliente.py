import socket
import threading
from tkinter import *

class hola():
    def __init__(self):
        self.fin=0
        self.ip = socket.gethostbyname(socket.gethostname())
        self.establecer_coneccion_envia()

        self.texto_recivido=""

        self.ventana=Tk()

        self.ventana.geometry("1000x500")



        self.button2=Button(self.ventana,text="envia",command=self.boton_2)
        self.button2.place(x=100, y=200, width=100, height=50)
        self.text1=Entry(self.ventana)
        self.text1.place(x=250,y=100,height=150,width=700)
        self.text2 = Entry(self.ventana)
        self.text2.place(x=250, y=300, height=150, width=700)

        self.hilo1=threading.Thread(name="s", target=self.recive)
        self.hilo1.start()

        self.hilo_main=threading.Thread(name="main", target=self.ventana.mainloop())
        self.hilo_main.start()

    def recive(self):
        self.i=0
        while True:
            self.i+=1
            self.texto_recivido=self.conexion.recv(1024).decode()
            print("se a recivido: ",self.texto_recivido)
            self.text1.insert(0,self.texto_recivido)

            if self.i>10:
                self.text1.delete(0,'end')
                self.i=0

            if (self.fin == 1):
                break
        conexion.close()

    def establecer_coneccion_envia(self):
        puerto = 8000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, puerto))
        self.server.listen(1)
        self.conexion, self.direccion = self.server.accept()

        puerto = 8001
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, puerto))

    def boton_2(self):
        self.s.send("mensaje".encode('utf-8'))
        self.text2.insert(0, "se a enviado")


h=hola()