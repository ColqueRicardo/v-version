import socket
import sys
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/clase bd/usuario_gestor.py")
from usuario_gestor import gestor_usuarios
from prueba import *

gestor_usuarios= gestor_usuarios()
print("empieza")
s= socket.socket()
s.bind(('localhost',8000))
s.listen(1)


while True:
    conexion, direccion= s.accept()
    '''tengo q medir lo q se envia'''
    peticion=conexion.recv(1024)
    peticion=peticion.decode()

    print(decoficar_mensaje(str(peticion)))
    peticion =decoficar_mensaje(str(peticion))

    if peticion[0]=="obtener_secion":
        resolucion= gestor_usuarios.iniciar_secion(peticion[1],peticion[2])
    del peticion
    conexion.send(resolucion.encode('utf-8'))
    conexion.close()
