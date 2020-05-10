from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import socket
import sys
import datetime
from tkinter import messagebox

'''sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/clase bd/usuario_gestor.py")
'''
'''sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/clase bd/usuario_secion.py")
'''
'''sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/clase bd/prueba.py")'''
from usuario_secion import usuario_secion
from usuario_gestor import gestor_usuarios
from prueba import *


class usuarios():
    def __init__(self):
        self.ventana=Tk()
        x=int(self.ventana.winfo_screenwidth()*0.3)
        y=int(self.ventana.winfo_screenheight()*0.2)
        xy="{0}x{0}+"+str(x)+"+"+str(y)
        self.ventana.geometry((xy.format(500, 300)))
        self.usuario_variable = StringVar()
        self.usuario_label=Label(self.ventana,text="Ingrese el nombre del usuario")
        self.usuario_label.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.05)
        self.usuario_textbox = Entry(self.ventana)
        self.usuario_textbox.place(relx=0.15,rely=0.1,relwidth=0.7,relheight=0.05)
        self.password_label=Label(self.ventana,text="Ingrese la contraseña del usuario")
        self.password_label.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.05)
        self.password_variable=StringVar()
        self.password_textbox= Entry(self.ventana)
        self.password_textbox.place(relx=0.15,rely=0.2,relwidth=0.7,relheight=0.05)

        self.inicio_secion = Button(self.ventana,command=lambda: usuarios.obtener_secion_boton(self),text="iniciar")
        self.inicio_secion.place(relx=0.2,rely=0.35,relwidth=0.2,relheight=0.05)

        self.cancelar_secion= Button(self.ventana,command=lambda:usuarios.cancelar_secion_boton(self),text="cancelar")
        self.cancelar_secion.place(relx=0.6,rely=0.35,relwidth=0.2,relheight=0.05)
        self.ventana.mainloop()
    def obtener_secion_boton(self):

        s = socket.socket()
        s.connect(('localhost', 8000))
        vec=["obtener_secion"],[self.usuario_textbox.get()],[self.password_textbox.get()]
        mensaje=codificar_mensaje(vec)

        s.send(mensaje.encode())
        '''peso esperado (un objeto vacio deberia pesar almenos 20bytes) '''
        respuesta = s.recv(1024).decode()
        s.close()
        if respuesta=="aceptado":
            self.secion_usuario=usuario_secion(self.usuario_textbox.get(),self.password_textbox.get())
            messagebox.showinfo(message="bienvenido "+ self.secion_usuario.usuario, title="secion iniciada")
            print(self.secion_usuario.usuario)
            print(self.secion_usuario.password)
            print(self.secion_usuario.pc_ip)
            print(self.secion_usuario.pc_name)
            print(self.secion_usuario.expiracion_secion<datetime.date.today()+datetime.timedelta(days=0))
            print(self.secion_usuario.usuario_privilegios)
        elif respuesta=="el usuario a exedido el numero de conecciones":
            messagebox.showerror(message=respuesta, title="Advertencia")
        elif respuesta=="contraseña no coinciden":
            messagebox.showerror(message=respuesta,title="advertencia")
        elif respuesta=="no existe el usuario":
            messagebox.showerror(message=respuesta, title="advertencia")

    def cancelar_secion_boton(self):
        sys.exit(0)
        '''debe cerrar todo otro dia vere'''
s=usuarios()
