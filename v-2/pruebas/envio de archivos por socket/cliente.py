import socket
import pickle
import sys
r="C:/Users/ricar/Desktop/prueba v2.docx"
r2="C:/Users/ricar/Desktop/pruebav2"
r3=r2+"/v2.docx"
c=open(r,"rb")
lectura=c.read()
t=sys.getsizeof(lectura)
'''mensaje=[]
mensaje.append(c.read())
mensaje.append(r3)
mensaje=pickle.dumps(mensaje)
tamaño=sys.getsizeof(mensaje)'''

s = socket.socket()
s.connect(('localhost',8000))
s.send(pickle.dumps(t))
print(t)
s.send(lectura)
print(type(lectura))
'''peso esperado'''
s.close()