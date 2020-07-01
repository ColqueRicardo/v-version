import socket
from io import open
import pickle
import sys

'r="C:/Users/ricar/Desktop/Nuevo documento de texto.txt"'
r="archivo_recivido.txt"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost',8000))
s.listen(1)
i=0
iteraciones=0

'while True:'
c = open(r, "wb")
conexion, direccion= s.accept()
w=True
while w:
    peticion =conexion.recv(1024)
    if peticion == "termino".encode():
        w = False
        print("termino")
    else:
        iteraciones += 1
        print("iteraciones: ", iteraciones,"peticion: ",peticion)
        c.write(peticion)

i+=1
c.close()

conexion.close()



