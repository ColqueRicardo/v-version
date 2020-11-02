import binascii
import socket
import struct
import sys


class prueba():
    def __init__(self):
        self.t=0


# Create a TCP/IP socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

'''unpacker = struct.Struct('I 2s f ')'''
unpacker=None
while True:
    print('\nwaiting for a connection')

    connection, client_address = sock.accept()
    try:
        print("unpacker",unpacker)
        if unpacker==None:
            estructura = connection.recv(1024)
            print("estructura",estructura.decode())
            unpacker=struct.Struct(estructura.decode())
        else:
            data = connection.recv(unpacker.size)
            print('received {!r}'.format(binascii.hexlify(data)))

            unpacked_data = unpacker.unpack(data)

            print('unpacked:', unpacked_data)



    finally:
        'connection.close()'