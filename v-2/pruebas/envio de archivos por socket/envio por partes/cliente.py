import socket
import pickle
import sys

paso=8
r="archivo.txt"
c=open(r,"rb")
fin= (sys.getsizeof(c.read()))
iteraciones=fin//paso
c.seek(0)
w=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost',8000))

tamaños=0
validador=True
while validador:
    s.send(c.read(paso))
    w+=paso
    c.seek(w)

    print("fin",fin,"w",w)
    if w>fin:
        validador=False
        s.send("termino".encode())
print("tamaños: ",tamaños,"cantidad de iteraciones: ",iteraciones)
s.send(("termino").encode())
s.close()
