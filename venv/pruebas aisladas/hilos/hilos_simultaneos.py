import threading
import time

def crear_hilo(hilo_numero,timer):
    hilos=threading.Thread(name=str(hilo_numero),target=tarea,args=(hilo_numero,timer,0))
    return hilos
def tarea(numero,timers,indice):
    while True:
        indice+=1
        print("este hilo es el: " + str(threading.current_thread()),indice)
        'timers.sleep(0.5)'
        if indice ==10:
            break;
class prueba():
    def __init__(self):
        print("inicio")
        self.hilos=[]
        self.timer=[]
        '''
        self.hilo1=threading.Thread(name="hilo%s" %2,target=tarea,args=(10,))
        self.hilo1.start()'''

        'multiples hilos simultaneos (+5)'
        for i in range(2):

            self.timer.append(time)
            self.hilos.append(crear_hilo(i,self.timer[i]))
            self.hilos[i].start()
        print("asdidossdhnjoikdsaffbhnkjlkasdj bnkskadmj")
p=prueba()
