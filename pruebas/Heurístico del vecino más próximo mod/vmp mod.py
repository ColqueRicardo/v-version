from tkinter import *
import tkinter as tk
import random
import pickle
import sys
import time

class vmp():
    def __init__(self):



        'inicio de matriz distancias'
        self.matriz=[]
        'definicion de nodo inicio'
        self.nodo_inicio=0
        self.tamaño=5
        'generacion aleatorea de una matriz'
        '''
        for i in range(tamaño):
            self.matriz.append([])
            for j in range(tamaño):
                self.matriz[i].append(random.randint(0,100))
        '''
        'guardar matriz'
        '''
        r2 = "C:/Users/ricar/OneDrive/Desktop/Nueva carpeta (3)/prueba.txt"
        c = open(r2, "wb")
        c.write(pickle.dumps(self.matriz))
        c.close()
        '''
        'cargar matriz'
        r2 = "C:/Users/ricar/OneDrive/Desktop/Nueva carpeta (3)/prueba.txt"
        c = open(r2, "rb")
        self.matriz = pickle.loads(c.read())
        c.close()

        self.vent=Tk()
        self.vent.geometry("1250x750")
        self.canvas= Canvas(self.vent,bg="black")
        self.canvas.place(x=250,y=0,width=1000,height=750)
        tam=750//self.tamaño
        columnas=int((self.tamaño**(0.5))//1)
        l=0

        x=0
        y=0
        'vector de nodos random.randint(0,tam/2)'
        self.nodos =[]
        while(l!=self.tamaño):
            if (l%columnas==0):
                y+=random.randint(tam//4,tam)
                x=random.randint(tam//4,tam)
            x+=random.randint(tam//4,tam)
            l+=1
            self.nodos.append((x,y))
            self.canvas.create_text(x, y, fill="white", font="Times 20 italic bold",
                        text=str(l),tags=str(l))

        'creacion de las relaciones'
        '''
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if self.matriz[i][j]!=0:
                    self.canvas.create_line(self.nodos[i],self.nodos[j], fill="white")'''

        '''
        v=[]
        for i in range(1,5):
           v.append(i)

        print(self.matriz)
        print(self.obtener_camino_de_vuelta(v))

        v=[]
        for i in range(0,5):
            if (i != 3):

                v.append(i)

        print(v)
        print(self.obtener_sgte_camino(v,2))'''
        'proceso de tsp'
        self.caminos = []
        'despues vemos'
        self.nodos_sin_coneccion = []
        self.nodos_libres = []
        self.nodos_usados = []
        self.vuelta = []
        for i in range(1,self.tamaño):
            self.nodos_libres.append(i)
        self.nodos_usados.append(self.nodo_inicio)
        print(self.matriz)
        o=0

        while True:
            'empieza lo molesto'

            self.nodos_usados.append(self.obtener_sgte_camino(self.nodos_libres,self.nodos_usados[len(self.nodos_usados)-1]))
            'print("usados",self.nodos_usados)'
            self.nodos_libres.remove(self.nodos_usados[len(self.nodos_usados)-1])
            'print("libres", self.nodos_libres, len(self.nodos_libres))'
            aux= self.nodos_libres.copy()
            self.vuelta= self.obtener_camino_de_vuelta(aux)
            'print("vuelta",self.vuelta)'
            'print("libres", self.nodos_libres,len(self.nodos_libres))'
            'arma los posibles caminos'
            aux=self.vuelta.copy()
            aux.reverse()
            self.caminos.append(self.nodos_usados+ aux)
            'print("-----------------------------")'
            if (self.obtener_sgte_camino(self.nodos_libres,self.nodos_usados[len(self.nodos_usados)-1])==self.vuelta[len(self.vuelta)-1]):
                self.vuelta.reverse()
                self.caminos.append(self.nodos_usados+self.vuelta)

                break
            else:
                o+=1
                if o==20:
                    print("termino por o")
                    bandera=False
        'self.puro_vmp()'


        self.b=Button(self.vent,command=self.inicio,text="calcular")
        self.b.place(x=50,y=100,width=150,height=50)
        self.resultado=Text(self.vent)
        self.resultado.place(x=25,y=200,relheight=0.5,width=200)
        self.vent.mainloop()

    def inicio(self):
        min = self.caminos[0][len(self.caminos) - 1]
        id = 0
        a = -1
        for i in self.caminos:
            a += 1
            'print("camino n°",a,i,"posee un resultado total de: ",self.obtener_resultado(i) )'
            if self.obtener_resultado(i)[len(i) - 1] <= min:
                min = i[len(i) - 1]
                id = a
        print(self.caminos[id], "final", self.obtener_resultado(self.caminos[id]))
        print(self.caminos[len(self.caminos) - 1], "vmp", self.obtener_resultado(self.caminos[len(self.caminos) - 1]))
        for i in range(self.tamaño):
            '''print("---------------")
            print(a,"len", len(self.caminos[id]))
            print(i,"i+1",i+1)'''
            self.canvas.create_line(self.nodos[self.caminos[id][i]],self.nodos[self.caminos[id][i+1]],fill="red")
            'time.sleep(0.4)'
        resultado="El camino optimo esta dado por el recorrido :\n"

        for i in range(self.tamaño+1):
            resultado+="nodo "+str(self.caminos[id][i]+1) + ", "
        resultado+="con un resultado total de :"+str(self.obtener_resultado(self.caminos[id])[self.tamaño])+"\n"

        resultado+="dado por la suma de os recorridos en los nodos =\n "
        a=0
        for i in self.obtener_resultado(self.caminos[id]):
            a+=1

            resultado+=str(i)
            if (a!=self.tamaño):
                resultado+="+"
            else:
                break
        self.resultado.insert(tk.END,resultado)
    def puro_vmp(self):
        v=[]
        v.append(self.nodo_inicio)
        nodos_libres=[]
        for i in range(1,self.tamaño):
            nodos_libres.append(i)
        for i in range(1,self.tamaño):
            v.append(self.obtener_sgte_camino(nodos_libres,v[len(v)-1]))
            nodos_libres.remove(v[len(v) - 1])

        v.append(0)
        print("camino VMP puro :",v)
        print(self.obtener_resultado(v))

    def obtener_resultado(self,vect):
        s=[]
        for i in range(len(vect)-1):
            s.append(self.matriz[vect[i]][vect[i+1]])
        sum=0
        for i in range(len(s)):
            sum+=s[i]
        s.append(sum)
        return s


    def obtener_sgte_camino(self,vector,nodo_actual):
        'pasar solo el vector con los nodos libres'
        if(nodo_actual!=0):
            sgte=vector[0]
        else:
            sgte=vector[1]

        for i in range(len(vector)):
            'print("vector [",i,"]",vector[i])'
            if(self.matriz[nodo_actual][vector[i]]<self.matriz[nodo_actual][sgte]):
                sgte=vector[i]

        'devuelve el sgte nodo a usar'
        return sgte



    def obtener_camino_de_vuelta(self,vector):
        'pasar solo los nodos que son para el camino de vuelta, sin los usados, es decir los libres'
        l=0
        camino=[]

        pivote=self.nodo_inicio
        camino.append(pivote)

        x=True
        tamaño=len(vector)
        while x:
            'print("vector",vector)'
            min=vector[0]
            for i in vector:
                if (self.matriz[pivote][i]<self.matriz[pivote][min]) and (self.nodo_inicio!=i) :
                    min=i
            vector.remove(min)
            camino.append(min)
            pivote=min

            if len(camino)==tamaño+1:
                x=False
        return camino

vmp()