import socket
import  time
import  threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',8000))
s.listen(1)
a=[]
i=0
while True:
    a.append(0)
    a[i], direccion= s.accept()
    print("se a conectado")
    print(a[i])

    print(direccion)
    peticion = a[i].recv(1024)

    print(peticion)
    mensaje="hola cliente"
    a[i].send(mensaje.encode('utf-8'))
    'a[i].close()'
    i += 1
    if len(a)>4:
        break
print(len(a))
print(a)

'''
def imprime(io):
    while  True:
        print(io)
        time.sleep(1)

b=[]
for i in range(10):

    b.append(threading.Thread(name="movimiento",target=imprime,args={i}))
    b[i].start()
    '''