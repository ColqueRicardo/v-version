
'''
import os
import sys
import platform
from datetime import datetime
import socket



ip = socket.gethostbyname(socket.gethostname())
ipDividida = ip.split('.')

try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    print(red)
    comienzo = 0
    fin = 100

except:
    print("[!] Error")
    sys.exit(1)

if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

tiempoInicio = datetime.now()
print("[*] El escaneo se está realizando desde", red + str(comienzo), "hasta", red + str(fin))
asa=1
for subred in range(comienzo, fin + 1):

    direccion = red + str(subred)
    response = os.popen(ping + " " + direccion)
    for line in response.readlines():
        if ("ttl" in line.lower()):

            print(subred)
            print(direccion, "está activo")
            break

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)'''
import os
import sys
import platform
import threading, subprocess
from datetime import datetime
import socket

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


class Hilo(threading.Thread):

    def __init__(self, inicio, fin):
        self.ip=[]
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fin = fin

    def run(self):
        for subred in range(self.inicio, self.fin):
            direccion = red + str(subred)
            response = os.popen(ping + " " + direccion)
            for line in response.readlines():
                if ("ttl" in line.lower()):
                    self.ip.append(direccion)
                    '''print(direccion, "está activo")'''

                    break

class gestor():
    def __init__(self,cantidadhilos,redip,comienzog,fing,ipxhilosg):
        self.cantidadhilo=cantidadhilos
        self.comienzo=comienzog
        self.fin=fing
        self.iphilo=ipxhilosg
        self.hilo = []
        self.ips=[]
        try:
            for i in range(self.cantidadhilo):
                self.finAux = self.comienzo + self.iphilo
                if (self.finAux >self.fin):
                    self.finAux = self.fin
                h =Hilo(self.comienzo, self.finAux)
                h.start()
                self.hilo.append(h)
                self.comienzo =self.finAux
        except Exception as e:
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

tiempoInicio = datetime.now()
print("[*] El escaneo se está realizando desde", red + str(comienzo), "hasta", red + str(fin))
NumeroIPs = fin - comienzo
numeroHilos = int((NumeroIPs / IPXHILOS))
print("numeros de hilos: ",numeroHilos)

g=gestor(numeroHilos,red,comienzo,fin,IPXHILOS)
g.obtener_ips()
g.obtener_ips()

g.obtener_ips()
print(len(g.ips))
print(g.ips)
'print(socket.gethostbyaddr(socket.gethostname()))'

'''for ip in g.ips:
    try :

        print(socket.gethostbyaddr(ip))
        print(ip)
    except:
        print("la ip:",ip,"da problemass")
'''
'print(socket.gethostbyaddr("192.168.2.15"))'
tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)