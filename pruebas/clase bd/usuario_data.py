import socket
import pickle
import datetime
import io
import sys


class datos_usuarios():
    def __init__(self,usuario,password,privilegios):
        self.usuario = usuario
        self.password = password
        self.usuario_privilegios = privilegios
        self.last_connection = datetime.date.today()
        self.max_connections=1
        self.connectiosn_actuales=0

        '''self.usuario_privilegios--> 1°-->privilegios de crear usuarios,bd,etc
                                       2°-->privilegios de insert
                                       3°-->privilegios de update
                                       4°-->privilegios de delete°'''

    def __del__(self):
        del self.usuario
        del self.password
        del self.last_connection
        del self.usuario_privilegios

def serializar(ruta,objeto):
    with open(ruta,"wb") as f:
        pickle.dump(objeto, f)

def deserializar(ruta):
    with open(ruta, "rb") as f:
        b = pickle.load(f)
    return b

'''
usuario=datos_usuarios()
usuario.instanciar_usuario("rc","123456789","1111")
print(usuario)
serializar("C:/Users/ricar/Desktop/pruebas v1/base/usuarios/usuarios",usuario)
usu=deserializar("C:/Users/ricar/Desktop/pruebas v1/base/usuarios/usuarios")
print(usu)
'''