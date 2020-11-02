import socket

s = socket.socket()
'''esto si nesecita la direccion para conectarse y el puerto'''
s.connect(('192.168.2.23',8000))
mensaje="hola servidor"
s.send(mensaje.encode('utf-8'))
'''peso esperado'''
respuesta= s.recv(1024)
print(respuesta)
s.close()