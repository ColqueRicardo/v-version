import socket
from io import open
import pickle
import sys
r="C:/Users/ricar/Desktop/prueba v2.docx"
r2="C:/Users/ricar/Desktop/pruebav2"
r3=r2+"/v2.docx"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''s.bind(('localhost',8000))'''
s.bind(('localhost',8000))
s.listen(10)
conexiones=[]
i=0
while True:
    conexion, direccion= s.accept()
    conexiones.append(conexion)
    peticion =(pickle.loads(conexiones[i].recv(1024)))
    print(peticion)
    peticion2=conexiones[i].recv(peticion*1.1)
    print(sys.getsizeof(peticion2))
    print(peticion2)
    c = open(r3, "wb")
    c.write(peticion2)
    c.close()
    conexiones[i].close()
    i += 1