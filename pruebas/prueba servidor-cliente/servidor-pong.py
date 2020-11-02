import socket
import sys
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/j1.py")
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/prueba servidor-cliente/prueba.py")
from prueba import *




print("empieza")
s= socket.socket()
s.bind(('localhost',8000))
s.listen(1)

i=0
while True:
    conexion, direccion= s.accept()
    peticion=conexion.recv(1024).decode()
    print(peticion)
    if peticion=="jugador 1 esperando":
        i=i+1
        print(i)
        if i==3:
            print("se envio ")
            conexion.send("se puede".encode())
    elif peticion=="arriba":
        ''
    conexion.close()

