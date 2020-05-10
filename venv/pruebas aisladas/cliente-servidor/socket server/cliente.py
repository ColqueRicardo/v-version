import socket
import pickle

class pruebas():
    def __init__(self):
        self.prueba=["hola"],["adios"]
        self.numero=10
        self.letra="a"
        self.palabra="holaadios"

prueba=pruebas()
mensaje=pickle.dumps(prueba)

host = 'localhost'
port = 8000

obj = socket.socket()

obj.connect((host, port))

obj.send(mensaje)

respuesta= obj.recv(1024)

print(respuesta)
respuesta=pickle.loads(respuesta)
print(respuesta.palabra)

obj.close()

print("Conexión cerrada")