import socket

's= socket.socket()'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''s.bind(('localhost',8000))'''
s.bind(('',8000))
s.listen(1)

while True:
    conexion, direccion= s.accept()
    print("se a conectado")
    print( conexion)
    print(direccion)
    peticion = conexion.recv(1024)
    print(peticion)
    mensaje="hola cliente"
    conexion.send(mensaje.encode('utf-8'))
    conexion.close()