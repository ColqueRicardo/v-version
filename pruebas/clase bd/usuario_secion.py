import socket
import pickle
import datetime
import io
import sys



class usuario_secion:
    def __init__(self,usuario,password):
        self.usuario=usuario
        self.password=password
        self.pc_name=socket.gethostname()
        self.pc_ip=socket.gethostbyname(socket.gethostname())

        self.expiracion_secion=datetime.date.today()+datetime.timedelta(days=1)
        self.ruta_archivo="C:/Users/ricar/Desktop/pruebas v1/base/seciones_particulares"
        '''self.usuario_privilegios--> 1°-->privilegios de crear usuarios,bd,etc
                                       2°-->privilegios de insert
                                       3°-->privilegios de update
                                       4°-->privilegios de delete°'''
        self.usuario_privilegios=""
    def asignar_usuario(self,usuario):
        self.usuario=usuario
    def asignar_password(self,password):
        self.password =password
    def asignar_pc_name(self):
        self.pc_name =socket.gethostname()
    def asignar_pc_ip(self):
        self.pc_ip =socket.gethostbyname(socket.gethostname())
    def asignar_privilegios(self,priv):
        self.usuario_privilegios =priv

def serializar(ruta,objeto):
    with open(ruta,"wb") as f:
        pickle.dump(objeto, f)

def deserializar(ruta):
    with open(ruta, "rb") as f:
        b = pickle.load(f)
    return b


'''
secion = usuario_secion()
secion.asignar_usuario("rc")
secion.asignar_password("123456789")
secion.asignar_pc_name()
secion.asignar_pc_ip()
secion.asignar_last_connection()
secion.asignar_ruta_bd("C:/Users/ricar/Desktop/pruebas v1/base/secion")
secion.asignar_privilegios("1111")
serializar(secion.ruta_archivo,secion)
print(secion)
'''