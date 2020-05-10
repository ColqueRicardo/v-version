import socket
import pickle
import datetime
import io
import sys
import os

from usuario_data import  datos_usuarios
from usuario_secion import usuario_secion

class gestor_usuarios():
    def __init__(self):
        if os.path.exists("C:/Users/ricar/Desktop/pruebas v1/base/usuarios/usuarios.gu"):
            self.usuario = self.actualizar().usuario


        else:
            self.usuario = []
            self.crear_usuario("rc","123456789","1111")
            print("no existe")
    def iniciar_secion(self,usuario,password):
        i= self.encontrar_usuario(usuario,password)
        print(i)
        if i>=0:
            if self.usuario[i].connectiosn_actuales<self.usuario[i].max_connections:
                self.usuario[i].connectiosn_actuales=+1
                self.guardar()
                return "aceptado"
            else:
                return "el usuario a exedido el numero de conecciones"
        elif i==-1:
            return "contraseña no coinciden"
        elif i==-2:

            return "no existe el usuario"
    def cerrar_secion(self,usuario,password):
        i=self.encontrar_usuario(usuario,password)
        if i>=0:
            self.usuario[i].connectiosn_actuales=self.usuario[i].connectiosn_actuales+1
            self.guardar()
            return "aceptado"

        elif i==-1:
            return "contraseña no coinciden"
        elif i==-2:

            return "no existe el usuario"

        self.usuario[i].connectiosn_actuales=self.usuario[i].connectiosn_actuales-1
        self.guardar()
        del secion
    def encontrar_usuario(self,usuario,password):
        exist=False
        i=0
        while not exist and i<len(self.usuario):

            if self.usuario[i].usuario == usuario:

                exist = True
            else:
                i = i + 1

        if exist:

            if self.usuario[i].password == password:
                return i
            else:
                return -1
        else:
            return -2
    def crear_usuario(self,usuario,password,privilegios):
        exist=False
        i=0
        while not exist and i<len(self.usuario):
            if self.usuario[i].usuario==usuario:
                exist=True
            i=i+1
        if not exist:
            if len(password)>8:
                usuario_data=datos_usuarios(usuario,password,privilegios)
                self.usuario.append(usuario_data)
                print(self.usuario[0])
                print("usuario creado")
                self.guardar()
            else:
                print("contraseña corta")
        else:
            print("usuario existente")
    def eliminar_usuario(self,usuario,password):
        i=self.encontrar_usuario(usuario,password)

        if i>=0:
            self.usuario.pop(i)
            self.actualizar()
            return i
        elif i==-1:
            return -1
        elif i==-2:
            return -2

    def guardar(self):
        with open("C:/Users/ricar/Desktop/pruebas v1/base/usuarios/usuarios.gu", "wb") as f:
            pickle.dump(self, f)
    def actualizar(self):
        with open("C:/Users/ricar/Desktop/pruebas v1/base/usuarios/usuarios.gu", "rb") as f:
            b  = pickle.load(f)
        return b
    'restablece las conecciones a 0'
    def restablece(self):
        for i in range(len(self.usuario)):
            self.usuario[i].connectiosn_actuales=0
            self.guardar()
    ''' 
    C:/Users/ricar/Desktop/pruebas v1/base/usuarios es la carpeta donde se guardaran los datos de los usuarios para el servidor
    C:/Users/ricar/Desktop/pruebas v1/base/secion usuario es la carpeta donde se guardaran las seciones de cada usuario (esta carpeta debera estar en cada terminal remota no en el servidor)
     '''
gu= gestor_usuarios()
gu.restablece()

'''
gu= gestor_usuarios()
gu.restablece()

'''''''gu= gestor_usuarios()
for i in range (0,len(gu.usuario)):
    print(gu.usuario[i].usuario)
    print(gu.usuario[i].password)
secion=gu.iniciar_secion("rc","123456789")
print(sys.getsizeof(secion))
print(sys.getsizeof(gu))'''
'''
gu= gestor_usuarios()
gu.crear_usuario("rc","123456789","1111")

secion = gu.iniciar_secion("rc","123456789")
if type(secion)!=int:
    print(secion)
    gu.cerrar_secion(secion)
else:
    print("no se pudo iniciar secion")
for i in range (0,len(gu.usuario)):
    print(gu.usuario[i].usuario)
    print(gu.usuario[i].password)
    print(gu.usuario[i].last_connection)
'''
'''print(gu.eliminar_usuario("rc2","12345678910"))'''

