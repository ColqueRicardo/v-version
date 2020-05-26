import socket

's= socket.socket()'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''s.bind(('localhost',8000))'''
s.bind(('localhost',8000))
s.listen(10)
conexiones=[]
i=0
while True:
    conexion, direccion= s.accept()

    conexiones.append(conexion)
    print(conexion==conexiones[i])
    peticion = conexiones[i].recv(1024)

    print(peticion.decode(),"conexion: ",i)
    mensaje="hola cliente"
    conexiones[i].send(mensaje.encode('utf-8'))
    conexiones[i].close()
    i += 1