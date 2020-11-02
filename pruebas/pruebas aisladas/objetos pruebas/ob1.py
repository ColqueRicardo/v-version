class arbol():

    def __init__(self):
        self.años=1
        self.vec=[]
        self.vec.append("fsaf")
        print("se a creado")
    def asignar(self,año):
        self.años=año
    def crece(self):
        self.años=self.años+1
    def muere(self):
        self.años=-1
        print("murio" + str(self.años))
    def mostrar(self):
        print(self.años)
    def obtener(self):
        return self.años
    def obtener_vec(self):
        print(self.vec)
'''a=arbol()
a.asignar(4)
a.crece()
print("años")
a.mostrar()
a.muere()
a.mostrar()'''