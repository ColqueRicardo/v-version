import binascii
import socket
import struct
import sys

class prueba():
    def __init__(self):
        self.t=1
        self.s=10
def armonizar(p):
    v=[]
    s=""
    v.append(p.t)
    's+=str(type(v[0]))'
    v.append(p.s)
    's+=str(type(v[1]))'
    s='I I'
    return s,v

# Create a TCP/IP socket

values = (1, b'ab', 2.7)

values=prueba()
armonizador , values=armonizar(values)
packer = struct.Struct(armonizador)
packed_data = packer.pack(*values)

print('values =', values)
i=0
for i in range (2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.connect(server_address)

    try:
        # Send data

        if i==0:
            print("1")
            print(armonizador.encode())
            sock.send(armonizador.encode())
            i+=1
        else:
            print("2")
            print('sending {!r}'.format(binascii.hexlify(packed_data)))
            sock.sendall(packed_data)
    finally:
        print('closing socket')
        sock.close()
