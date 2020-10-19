from tkinter import *
import tkinter as tk
from tkinter import  ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter import simpledialog
import pickle
from tkinter import messagebox

class interfaz:
    def __init__(self):

        self.floyd_clase = floyd()

        self.vent=Tk()
        self.x_max=self.vent.winfo_screenwidth()
        self.y_max=self.vent.winfo_screenheight()
        self.vent.geometry(str(self.x_max)+"x"+ str(self.y_max)+"+0+0")

        self.label_nodos=Label(self.vent,text="ingrese la cantidad de nodos")
        self.label_nodos.place(x=15,y=5,width=150,height=15)
        self.cant_nodo= Entry(self.vent)
        self.cant_nodo.place(x=15,y=30,width=100,height=15)
        self.boton_nodo = Button(self.vent,text="continuar",command=self.continuar_nodos)
        self.boton_nodo.place(x=15, y=45, width=75, height=30)

        self.menu = Menu(self.vent)
        self.opciones = Menu(self.menu, tearoff=0)
        self.opciones.add_command(label="guardar datos", command=self.guardar)
        self.opciones.add_command(label="cargar datos", command=self.cargar)
        self.menu.add_cascade(label="opciones", menu=self.opciones)
        self.vent.config(menu=self.menu)

        self.vent.mainloop()
    def guardar(self):
        filename = filedialog.askdirectory()
        if filename!="":
            answer = simpledialog.askstring("como desea llamarlo", "",parent=self.vent)
        if filename!="" and (answer!=None):
            try:
                x= str(filename)+"/"+str(answer)+".matriz"
                file= open(x, "wb")

                w = []
                for i in range(int(self.cant_nodo.get())):
                    w.append([])
                    for j in range(int(self.cant_nodo.get())):
                        if i != j:
                            try:
                                if int(self.matriz[i][j].get()) >= 0:
                                    w[i].append(int(self.matriz[i][j].get()))
                                else:
                                    w[i].append("-")
                            except:
                                w[i].append("-")
                        else:
                            w[i].append("-")

                file.write(pickle.dumps(w))
                file.close()
            except:
                messagebox.showinfo(message="no hay datos que guardar", title="--")
        else:
            self.cant_nodo.insert(0,"sadiosdj")

    def cargar(self):

        fname = askopenfilename(filetypes=(("matriz_dts", "*.matriz"),
                                           ("All files", "*.*")))
        if fname!="":
            c = open(fname, "rb")
            matriz= pickle.loads(c.read())
            c.close()
            self.cant_nodo.delete(0,END)
            self.cant_nodo.insert(0,len (matriz[0]))

            try:
                for i in range(len(self.matriz[0])):
                    for j in range(len(self.matriz[0])):
                        self.matriz[i][j].destroy()
                self.vent.update()

            except:
                ''
            tam = (int(self.vent.winfo_screenheight()) * 0.8) // int(len(matriz[0]))
            if tam > 50:
                tam = 50
            self.matriz = []
            y = 100
            x_l = 100
            y_l = 100
            for i in range(len(matriz[0])):
                Label(self.vent, text="nodo" + str(i + 1)).place(x=x_l, y=25, width=tam, height=tam)
                Label(self.vent, text="nodo" + str(i + 1)).place(x=25, y=y_l, width=tam, height=tam)
                x_l += tam
                y_l += tam
                x = 100
                self.matriz.append([])
                for j in range(len(matriz[0])):
                    if i == j:
                        self.matriz[i].append(Entry(self.vent))
                        self.matriz[i][j].place(x=x, y=y, width=tam, height=tam)
                        self.matriz[i][j].insert(0, "-")
                        self.matriz[i][j].configure(justify=CENTER, state=DISABLED)
                        x += tam
                    else:
                        self.matriz[i].append(Entry(self.vent))
                        self.matriz[i][j].place(x=x, y=y, width=tam, height=tam)
                        self.matriz[i][j].configure(justify=CENTER)
                        self.matriz[i][j].insert(0,matriz[i][j] )
                        x += tam

                y += tam

        self.inicio_B = Button(self.vent, text="metodo de floyd", command=self.metood_floyd)
        self.inicio_B.place(x=400, y=15, width=150, height=15)

    def continuar_nodos(self):
        if self.cant_nodo.get()!="":
            try:
                for i in range(len(self.matriz[0])):
                    for j in range(len(self.matriz[0])):
                        self.matriz[i][j].destroy()
                self.vent.update()

            except:
                ''


            tam= (int(self.vent.winfo_screenheight())*0.8)//int(self.cant_nodo.get())
            if tam>50:
                tam=50
            self.matriz=[]
            y = 100
            x_l=100
            y_l=100

            for i in range(int(self.cant_nodo.get())):
                Label(self.vent,text="nodo"+str(i+1)).place(x=x_l,y=25,width=tam,height=tam)
                Label(self.vent, text="nodo" + str(i + 1)).place(x=25, y=y_l, width=tam, height=tam)
                x_l+=tam
                y_l+=tam
                x=100
                self.matriz.append([])
                for j in range(int(self.cant_nodo.get())):
                    if i==j:
                        self.matriz[i].append(Entry(self.vent))
                        self.matriz[i][j].place(x=x, y=y, width=tam, height=tam)
                        self.matriz[i][j].insert(0,"-")
                        self.matriz[i][j].configure(justify=CENTER,state=DISABLED)
                        x += tam
                    else:
                        self.matriz[i].append(Entry(self.vent))
                        self.matriz[i][j].place(x=x, y=y, width=tam, height=tam)
                        self.matriz[i][j].configure(justify=CENTER)
                        self.matriz[i][j].insert(0,"-")
                        x += tam

                y += tam

        self.inicio_B= Button (self.vent,text="metodo de floyd",command=self.metood_floyd)
        self.inicio_B.place(x=400,y=15,width=150,height=15)



    def metood_floyd(self):
        'floyd'
        w=[]
        for i in range(int(self.cant_nodo.get())):
            w.append([])
            for j in range(int(self.cant_nodo.get())):
                if i!=j:
                    try:
                        if int(self.matriz[i][j].get())>=0:
                            w[i].append(int(self.matriz[i][j].get()))
                    except:
                        w[i].append(-1)
                else:
                    w[i].append(-1)
        try:
            self.floyd_clase.vent_floyd.deiconify()
            self.floyd_clase.iniciar(w)
        except:
            self.floyd_clase = floyd()
            self.floyd_clase.vent_floyd.deiconify()
            self.floyd_clase.iniciar(w)



class floyd:
    def __init__(self):
        self.matriz_adjunta=[]
        self.estado_1=[]
        self.estado_2=[]
        self.vent_floyd = Tk()
        self.tam = int(int(self.vent_floyd.winfo_screenheight()) * 0.8)
        self.vent_floyd.geometry(str(self.tam) + "x" + str(self.tam))
        self.intento=1
        self.note_historial = ttk.Notebook(self.vent_floyd)
        self.note_historial.pack(fill="both", expand="yes")
        self.vent_floyd.withdraw()
    def iniciar(self,matriz):
        self.historial = Frame(self.note_historial)
        self.note_historial.add(self.historial,text=("prueba: "+str(self.intento)))
        self.intento+=1
        self.matriz = matriz
        self.tamaño = len(self.matriz[0])
        for i in range(self.tamaño):
            self.matriz_adjunta.append([])
            for j in range(self.tamaño):
                if j!=i:
                    self.matriz_adjunta[i].append(j+1)
                else:
                    self.matriz_adjunta[i].append("-")


        for w in range(self.tamaño):
            for i in range(self.tamaño):
                for j in range(self.tamaño):
                    if (j!=w or j!=i ) and (self.matriz[i][w]>=0 and self.matriz[w][j]>=0) and (j!=i):
                        if self.matriz[i][j]==-1:
                            self.matriz[i][j] = (self.matriz[i][w] + self.matriz[w][j])
                            self.matriz_adjunta[i][j] = w+1
                        elif self.matriz[i][w] + self.matriz[w][j] < self.matriz[i][j]:
                            self.matriz[i][j] = (self.matriz[i][w]+self.matriz[w][j])
                            self.matriz_adjunta[i][j]=w+1
            self.estado_1.append(self.matriz)
            self.estado_2.append(self.matriz_adjunta)


        self.note_iteraciones = ttk.Notebook(self.historial)
        self.note_iteraciones.pack(fill="both", expand="yes")
        for w in range(self.tamaño):
            self.contenedor= Frame(self.note_iteraciones,bg="blue")
            self.contenedor.place(relx=0,rely=0,relwidth=0.5,relheight=0.5)
            self.note_iteraciones.add(self.contenedor, text="iteracion: "+str(w+1))
            tam=50
            Label(self.contenedor, width=10, text="Matriz: D").grid(row=0, column=0)
            Label(self.contenedor, width=10, text="Matriz: S").grid(row=self.tamaño+2, column=0)
            Label(self.contenedor, width=10, text="---").grid(row=1 + self.tamaño, column=0)
            for i in range(self.tamaño):
                '''Label(self.contenedor, text="nodo" + str(i + 1)).place(x=x_l, y=25, width=tam, height=tam)
                Label(self.contenedor, text="nodo" + str(i + 1)).place(x=25, y=y_l, width=tam, height=tam)'''
                'matriz D'
                Label(self.contenedor, width=10, text="Nodo: " + str(i + 1)).grid(row=0, column=i + 1)
                Label(self.contenedor, width=10, text="Nodo: " + str(i + 1)).grid(row=i+1, column=0)
                Label(self.contenedor, width=10, text="---").grid(row=1 + self.tamaño, column=i +1,pady=4)
                'matriz S'
                Label(self.contenedor, width=10, text="Nodo: " + str(i + 1)).grid(row=2+self.tamaño, column=i+1)
                Label(self.contenedor, width=10, text="Nodo: " + str(i + 1)).grid(row=i + 3+self.tamaño, column=0)

                for j in range(self.tamaño):
                    if i != j:

                        'matriz d'
                        if self.estado_1[w][i][j]>0:
                            Label(self.contenedor, width=10, text=str(self.estado_1[w][i][j])).grid(row=i + 1, column=j + 1)
                        else:
                            Label(self.contenedor, width=10, text="-").grid(row=i + 1,column=j + 1)
                        'matriz adjunta'
                        if self.estado_2[w][i][j]>0:
                            Label(self.contenedor, width=10, text=str(self.estado_2[w][i][j])).grid(row=i + 3+self.tamaño, column=j + 1 )
                        else:
                            Label(self.contenedor, width=10, text="-").grid(row=i + 3 + self.tamaño, column=j + 1)
                        'Label(self.contenedor,text=str(self.estado_1[w][i][j])).place(x=x, y=y, width=tam, height=tam)'

                    else:
                        'matriz d'
                        'Label(self.contenedor, text="-").place(x=x, y=y, width=tam, height=tam)'
                        Label(self.contenedor, width=10, text="-").grid(row=i + 1, column=j + 1)
                        'matriz adjunta'
                        Label(self.contenedor, width=10, text="-").grid(row=i +3 +self.tamaño, column=j + 1)


        self.vent_floyd.mainloop()

interfaz()