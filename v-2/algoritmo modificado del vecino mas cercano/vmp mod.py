from tkinter import *
import tkinter as tk
import random
import pickle
import sys
import time
import threading

class vmp():
    def __init__(self):

        'iteraciones'
        self.cantidad_iteraciones=100

        self.rango_maximo=200
        self.cantidad_nodos=10
        self.vent=Tk()
        self.vent.geometry("1250x750")
        self.canvas= Canvas(self.vent,bg="white")
        self.canvas.place(x=250,y=0,width=1000,height=750)

        self.b = Button(self.vent, command=self.vent_matriz, text="mostrar matriz")
        self.b.place(x=50, y=100, width=150, height=50)
        self.boton_maquina_type = Button(self.vent, command=self.inicio_mt , text="comenzar "+str(self.cantidad_iteraciones)+" pruebas")
        self.boton_maquina_type.place(x=50, y=150, width=150, height=50)
        '''self.resultado = Text(self.vent)
        self.resultado.place(x=25, y=200, relheight=0.5, width=200)'''

        'self.hilo_mainloop=threading.Thread(name="mainloop",target= self.vent.mainloop())'
        self.hilo_creador= threading.Thread(name="creador",target=self.maquina_type1)


        self.vent.mainloop()
    def inicio_mt(self):
        'self.hilo_creador.start()'
        self.maquina_type1()
    def maquina_type1(self):
        suma_vmp=0
        suma_vmp_mod=0
        mejora_nodos=0
        self.iteraciones_actual = 1
        cantidad_aplicada=0
        for i in range(self.cantidad_iteraciones):

            t=random.randint(4,self.cantidad_nodos)
            self.generador_matriz(random.randint(0,t-1),t)
            self.mostrar_nodos()
            self.proceso_tsp()
            a=self.camino_final()
            suma_vmp+=a[0]
            suma_vmp_mod+= a[1]
            mejora_nodos+=(a[0]-a[1])/a[2]
            if (a[0] != a[1]):
                cantidad_aplicada+=1
            '''if(a[0]!=a[1]) and self.iteraciones_actual>450 and a[2]<7:
                break'''
            print("iteracion: ",self.iteraciones_actual)
            print("----------------------------")
        print("datos generales: ")
        print("cantidad de pruebas: ",self.cantidad_iteraciones)
        print("rango posible para los nodos generados: ", self.rango_maximo)
        'print("---------------------------------------------")'
        print("total de unidades reccorridas por el algoritmo Heurístico del vecino más próximo: ",suma_vmp)
        print("total de unidades reccorridas por la modificacion: ",suma_vmp_mod)
        print("total de unidades ahorradas: ",suma_vmp-suma_vmp_mod)
        print("se aplico en un total de: ", cantidad_aplicada, "casos, es decir", 100*(cantidad_aplicada/self.cantidad_iteraciones),"%")
        print("promedio de mejora por todas las iteraciones: ",(suma_vmp-suma_vmp_mod)/self.cantidad_iteraciones)
        print("promedio de mejora solo en las modificaciones",(suma_vmp-suma_vmp_mod)/cantidad_aplicada )
        print("porcentaje de mejora en funcion de su camino reccorrido: ",(1- (suma_vmp_mod/suma_vmp))*100,"%")
        print("mejora en funcion de sus nodos", mejora_nodos/cantidad_aplicada)
    def generador_matriz(self,nodo_inicio,tamaño_matriz):
        'inicio de matriz distancias'
        self.matriz = []
        'definicion de nodo inicio'
        self.nodo_inicio = nodo_inicio
        self.tamaño = tamaño_matriz
        'generacion aleatorea de una matriz'

        for i in range(self.tamaño):
            self.matriz.append([])
            for j in range(self.tamaño):
                self.matriz[i].append(random.randint(0, self.rango_maximo))
        'guardar matriz'
        '''
        r2 = "C:/Users/ricar/OneDrive/Desktop/Nueva carpeta (3)/prueba.txt"
        c = open(r2, "wb")
        c.write(pickle.dumps(self.matriz))
        c.close()
        '''
        'cargar matriz'
        '''
        r2 = "C:/Users/ricar/OneDrive/Desktop/Nueva carpeta (3)/prueba.txt"
        c = open(r2, "rb")
        self.matriz = pickle.loads(c.read())
        c.close()'''

    def mostrar_nodos(self):
        self.canvas.delete("all")
        tam=750//self.tamaño
        columnas=int((self.tamaño**(0.5))//1)
        l=0
        x=0
        y=75
        'vector de nodos random.randint(0,tam/2)'
        self.canvas.create_text(150, 20, fill="black", font="Times 12 italic bold",
                                text="el nodo inicial es :"+str(self.nodo_inicio+1) + "       Iteracion actual: "+str(self.iteraciones_actual), tags=str(l))
        'define el lugar donde esta cada nodo'
        self.iteraciones_actual+=1
        self.nodos =[]
        while(l!=self.tamaño):
            if (l%columnas==0):
                y+=random.randint(tam//4,tam)
                x=random.randint(tam//4,tam)
            x+=random.randint(tam//4,tam)
            l+=1
            self.nodos.append((x,y))
            self.canvas.create_text(x, y, fill="black", font="Times 20 italic bold",
                        text=str(l),tags=str(l))

        'carga vista de la matriz en otra ventana ahora inrrelevante'
        'self.vent_matriz()'

        'creacion de las relaciones en el canvas'

        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if self.matriz[i][j]!=0:
                    self.canvas.create_line(self.nodos[i],self.nodos[j], fill="orange")

    def proceso_tsp(self):
        'proceso de tsp'
        self.caminos = []
        'despues vemos'
        'self.nodos_sin_coneccion = []'
        self.nodos_libres = []
        self.nodos_usados = []
        self.vuelta = []

        for i in range(0,self.tamaño):
            if i!=self.nodo_inicio:
                self.nodos_libres.append(i)

        self.nodos_usados.append(self.nodo_inicio)
        'print(self.nodos_libres, "libres", self.nodo_inicio," usados",self.nodos_usados)'
        'print(self.matriz)'
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
            if len(self.nodos_libres)<=2:
                self.vuelta.reverse()
                self.caminos.append(self.nodos_usados + self.vuelta)
                break
            else:
                o+=1
                if o==self.tamaño*2:
                    print("termino por o")
                    break
        self.caminos.append(self.puro_vmp())




    def camino_final(self):
        'obtiene el camino mas corto y lo marca'
        min = self.obtener_resultado(self.caminos[0])[self.tamaño]

        id = 0
        a = -1
        for i in self.caminos:
            a += 1
            '''print("camino n°",a,i,"posee un resultado total de: ",self.obtener_resultado(i) )
            print('resultado',self.obtener_resultado(i)[self.tamaño],"min",min)'''
            if self.obtener_resultado(i)[self.tamaño] <= min:
                min = self.obtener_resultado(i)[self.tamaño]
                id = a

        print(self.caminos[id], "final", self.obtener_resultado(self.caminos[id]))
        print(self.caminos[len(self.caminos) - 1], "vmp", self.obtener_resultado(self.caminos[len(self.caminos) - 1]))

        for i in range(self.tamaño):
            self.canvas.create_line(self.nodos[self.caminos[id][i]], self.nodos[self.caminos[id][i + 1]], fill="blue")
        regreso=[]
        regreso.append(self.obtener_resultado(self.caminos[len(self.caminos) - 1])[self.tamaño])
        regreso.append (self.obtener_resultado(self.caminos[id])[self.tamaño])
        regreso.append(self.tamaño)
        return regreso


        'carga todo en un formato para el txt pero ahora no importa, '
        '''
        print(self.caminos[id], "final", self.obtener_resultado(self.caminos[id]))
        print(self.caminos[len(self.caminos) - 1], "vmp", self.obtener_resultado(self.caminos[len(self.caminos) - 1]))
        
        
            
        resultado="El camino optimo esta dado por el recorrido :\n"

        for i in range(self.tamaño+1):
            resultado+="nodo "+str(self.caminos[id][i]+1) + ", "
        resultado+="con un resultado total de :"+str(self.obtener_resultado(self.caminos[id])[self.tamaño])+"\n"

        resultado+="en comparacion con su vmp puro = "+ str(self.caminos[len(self.caminos) - 1])+ "vmp" +str( self.obtener_resultado(self.caminos[len(self.caminos) - 1]))

        self.resultado.insert(tk.END,resultado)'''
    def puro_vmp(self):
        v=[]
        v.append(self.nodo_inicio)
        nodos_libres=[]
        for i in range(0,self.tamaño):
            if i!=self.nodo_inicio:
                nodos_libres.append(i)
        'print(nodos_libres)'
        for i in range(0,self.tamaño-2):
            v.append(self.obtener_sgte_camino(nodos_libres,v[len(v)-1]))
            nodos_libres.remove(v[len(v)-1])
            'print(nodos_libres)'
        v.append(nodos_libres[0])
        '''if (self.matriz[v[len(v)-1]][0]>self.matriz[v[len(v)-1]][1]):
            v.append(nodos_libres[1])
            v.append(nodos_libres[0])
        else:
            v.append(nodos_libres[0])
            v.append(nodos_libres[1])'''
        v.append(self.nodo_inicio)
        return v


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
        if(nodo_actual==0):

            sgte=vector[1]

        else:
            sgte=vector[0]

        for i in range(len(vector)):
            'print("vector [",i,"]",vector[i])'
            if(self.matriz[nodo_actual][vector[i]]<self.matriz[nodo_actual][sgte]) and (self.matriz[nodo_actual][vector[i]]!=0):
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
                if (self.matriz[pivote][i]<self.matriz[pivote][min]) and (self.nodo_inicio!=i) and  (self.matriz[pivote][i]!=0) :
                    min=i
            vector.remove(min)
            camino.append(min)
            pivote=min

            if len(camino)==tamaño+1:
                x=False
        return camino
    def vent_matriz(self):
        vent=Tk()
        vent.geometry("750x750")
        for i in range(self.tamaño):
            for j in range(self.tamaño):

                if j!=i:
                    x=str(self.matriz[i][j])
                    a=Entry(vent)
                    a.grid(row=i,column=j)
                    a.insert(0,x)
                else:
                    Label(vent,text="---").grid(row=i,column=j)

vmp()