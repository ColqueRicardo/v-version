import socket
import string
import sys
import datetime
import pickle
import _compat_pickle
import threading
from tkinter import *
import os
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba v1/buscaip.py")
from buscaip import *




class trasmisor():
    def __init__(self,ip):
        self.ip=ip
        self.archivo=None
        self.ruta=NONE
        self.vent=Tk()
        self.vent.geometry("300x100")
        self.text= Entry(self.vent)
        self.text.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.45)
        self.boton= Button(self.vent,command=lambda :self.transferir())
        self.boton.place(relx=0.05,rely=0.6,relheight=0.3,relwidth=0.4)
        self.buffer=1024

        self.vent.mainloop()
    def transferir(self):

        self.s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dir=((self.ip,8000))
        self.s.connect(self.dir)
        self.s.sendto(str(self.ip).encode(),(self.dir))
        if (self.s.recv(self.buffer).decode()=="listo"):
            self.vent.destroy()
        self.s.close()



class menu():
    def __init__(self):
        self.limites_conecciones=10
        self.vent= Tk()
        self.vent.geometry("500x500")
        self.list=Listbox(self.vent)
        self.list.place(relx=0.1,rely=0.15,relwidth=0.5,relheight=0.5)
        self.list.bind('<<ListboxSelect>>', lambda event :self.imprimir(event,2))
        self.list.config(state=DISABLED)
        self.actualizar_boton= Button(self.vent,text="actualizar",command=lambda:self.actualizar_comando())
        self.actualizar_boton.place(relx=0.15,rely=0.75,relwidth=0.1,relheight=0.05)
        self.b=Button(self.vent,text="empezar",command=lambda :self.empezar())
        self.b.place(relx=0.5,rely=0.75,relwidth=0.1,relheight=0.05)

        self.hilo_servidor=threading.Thread(name="servidor",target=self.servidor)
        self.hilo_servidor.start()

        self.hilo_mainloop=threading.Thread(name="mainloop",target=self.vent.mainloop())
        self.hilo_mainloop.start()

    def servidor(self):
        print("empezo a funcionar")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 8000))
        self.s.listen(self.limites_conecciones)
        self.buffer = 1024
        while True:
            self.conexion, self.direccion = self.s.accept()
            self.ip = self.conexion.recv(self.buffer).decode()
            self.conexion.sendto("listo".encode(), self.direccion)
            self.conexion.close()

            break
        print("termino hilo servidor")
        self.vent.destroy()
    def empezar(self):
        self.empezar=trasmisor(socket.gethostbyname(socket.gethostname()))
        'print (socket.gethostbyname(socket.gethostname()))'
    def imprimir(self,event,im):

        trasf=trasmisor(self.list.get(self.list.curselection()[0]))
        'print(self.list.get(self.list.curselection()[0]))'
    def actualizar_comando(self):
        gestor_ip=gestor(5,0,100)
        if gestor_ip.estado:
            i=0
            'self.list.config(state=e)'
            self.list.config(state=NORMAL)
            for ip in gestor_ip.obtener_ips():
                self.list.insert(i,ip)
                i+=1

        else:
            print("no se pudo cargar ips")

menu= menu()

