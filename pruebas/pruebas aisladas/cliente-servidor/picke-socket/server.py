import socket
import pickle

class pruebas():
    def __init__(self):
        self.prueba=["hola"],["adios"]
        self.numero=10
        self.letra="a"
        self.palabra="holaadios"


s= socket.socket()
s.bind(('localhost',8000))
s.listen(1)
print("empezo")
while True:

    conexion, direccion= s.accept()
    print("coneccion nueva\n")
    print( conexion)
    print(direccion)
    peticion = conexion.recv(1024)
    print(peticion)
    peticion=pickle.loads(peticion)
    print(peticion)
    print("imprima una palabra")
    peticion.palabra=input()
    conexion.send(pickle.dumps(peticion))
    conexion.close()