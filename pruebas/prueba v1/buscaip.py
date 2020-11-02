import os
import sys
import platform
import threading, subprocess
from datetime import datetime
import socket
'''
IPXHILOS = 1
ip = socket.gethostbyname(socket.gethostname())
ipDividida = ip.split('.')

try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    comienzo = 0
    fin = 100
except:
    print("[!] Error")
    sys.exit(1)

if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"
'''

class Hilo(threading.Thread):
    def __init__(self, inicio, fin,red):
        self.ip=[]
        self.red = red
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fin = fin

    def run(self):
        if (platform.system() == "Windows"):
            ping = "ping -n 1"
        else:
            ping = "ping -c 1"

        for subred in range(self.inicio, self.fin):
            direccion = self.red + str(subred)
            response = os.popen(ping + " " + direccion)
            for line in response.readlines():
                if ("ttl" in line.lower()):
                    self.ip.append(direccion)
                    '''print(direccion, "está activo")'''
                    break

class gestor():
    def __init__(self,iphilo,comienzog,fing):
        self.comienzo_deb=comienzog
        self.comienzo=comienzog
        self.fin=fing
        self.iphilo=iphilo
        self.cantidadhilo=((self.fin-self.comienzo)//self.iphilo)
        self.hilo = []
        self.ips=[]
        self.iplocal = socket.gethostbyname(socket.gethostname())
        self.ipDividida = self.iplocal.split('.')
        self.estado=True
        try:
            self.red = self.ipDividida[0] + '.' + self.ipDividida[1] + '.' + self.ipDividida[2] + '.'

        except:
            self.estado=False

        try:
            for i in range(self.cantidadhilo):
                self.finAux = self.comienzo + self.iphilo
                if (self.finAux >self.fin):
                    self.finAux = self.fin
                h =Hilo(self.comienzo, self.finAux,self.red)
                h.start()
                self.hilo.append(h)
                self.comienzo =self.finAux
        except Exception as e:
            self.estado=False
            print("[!] Error creando hilos:", e)
            sys.exit(2)

        for hilo in self.hilo:
            hilo.join()

    def esperar(self):
        for h in self.hilo:
            if h.is_alive():
                print("nada")
            else:
                print("hola")

    def obtener_ips(self):
        self.ips=[]
        for h in self.hilo:
            self.ips=self.ips + h.ip
        return self.ips

'''tiempoInicio = datetime.now()

print("a empezado:",tiempoInicio)

g=gestor(5,0,100)

print("numeros de hilos: ",g.cantidadhilo)

print("[*] El escaneo se está realizando desde", g.red + str(g.comienzo_deb ), "hasta", g.red + str(g.fin))

g.obtener_ips()
print("cantidad de ips:",len(g.ips))
'print(g.ips)'
'print(socket.gethostbyaddr(socket.gethostname()))'
las=0
for ip in g.ips:
    try :
        las+=1
        print("la ip N°: ",las)
        print(socket.gethostbyaddr(ip))
        print(ip)
    except:
        print("la ip:",ip,"da problemass")
'print(socket.gethostbyaddr("192.168.2.15"))'
tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)'''