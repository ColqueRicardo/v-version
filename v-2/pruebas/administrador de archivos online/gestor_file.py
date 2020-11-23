import sys
from timeit import timeit
from time import time

class archivo():
    def __init__(self,nombre):
        'el valor contenido solo asigna un id del contenido del archivo de la clase archivo_contenido'
        self.id=""
        self.visible=1
        w=self.sacar_extencion(nombre)
        self.nombre=w[0]
        self.extencion=w[1]
        self.contenido=-1
        del w
    def asigna_contenido(self,contenido):
        self.contenido=contenido
    def asignar_id(self,id):
        self.id=id
        return self
    def borrar(self):
        'borrar xd'
        self.visible=0
    def sacar_extencion(self,nombre):
        'saca nombre y extencion'
        w = []
        w.append("")
        w.append("")
        i = len(nombre)
        while w[1] =="" and i > 0:
            if nombre[i - 1:i] == ".":
                w[0]=nombre[0:i-1]
                w[1]=nombre[i:len(nombre)]

                break
            i -= 1

        if w[1] == "":
            w[1] = "none"
        return w
class archivo_contenido():
    def __init__(self):
        self.archivo_contenido= []
    def cantidad_archivos(self):
        return len(self.archivo_contenido)
    def agregar(self,contenido):
        self.archivo_contenido.append(contenido)
        return len(self.archivo_contenido)-1
    def obtener_contenido(self,id):
        return self.archivo_contenido[id]


class carpeta():
    def __init__(self,nombre):
        self.id=""
        self.visible=1
        self.nombre=nombre
        self.contenido=[]
        self.gestior_id=0

    def asignar_id(self,id):
        self.id=id
        return self
    def borrar(self):
        'borrar xd'
        self.visible=0
    def agregar_contenido(self,contenido):
        band=True
        if type(contenido)==archivo:
            for i in self.contenido:
                if (type(i)==type(contenido)) and i.visible==1 :
                    if i.nombre+"."+i.extencion==contenido.nombre+"."+contenido.extencion:
                        band=False
        else:
            for i in self.contenido:
                if (type(i)==type(contenido)) and i.visible==1:
                    if i.nombre==contenido.nombre:
                        band=False
        if band:
            self.contenido.append(contenido.asignar_id(self.gestior_id))
            self.gestior_id+=1
            return self.gestior_id-1
        else:
            return (-1)

    def busqueda_carpeta(self, ruta):
        try:
            parcial=self.contenido.copy()
            for i in ruta:
                'si falla es porque se modifico la direccion o ruta actual para que no sea integro'
                parcial = parcial.contenido[i]
            return parcial
        except:
            'print("no se encontro o ruta desconocida")'
            return None
    def busqueda_carpeta_nombre(self, ruta):
        try:
            parcial=self.contenido.copy()
            'la ruta solo posee los nombres de carpetas o archivos, encuenta y devuelve un archivo o una carpeta'
            for i in ruta:
                for j in parcial:
                    if type(j)==carpeta:
                        if j.nombre==i:
                            parcial=j.contenido
                            break
                    if type(j)==archivo:
                        if (j.nombre+"."+j.extencion) == i:
                            parcial=j
                            break
            retur=[]
            for i in parcial.contenido:
                if type(i) == carpeta:
                    retur.append(i.nombre)
                if type(i)==archivo:
                    retur.append(j.nombre+"."+j.extencion)
            if retur!=[]:
                return parcial
            else:
                return retur
        except:
            'print("no se encontro o ruta desconocida")'
            return None

def recorrer(c):
    for i in c.contenido:
        if type(i)==carpeta:
            print("nombre: " ,i.nombre,"id: ",i.id)
            recorrer(i)
        if type(i)==archivo:
            print("nombre: ", i.nombre,".",i.extencion,"id: ",i.id)


def busqueda_completa(c,v,w,s):
    p=None
    for i in c.contenido:
        if i.id==v[w]:
            if type(i) == carpeta:
                'print("nombre: ", i.nombre, "id: ", i.id)'
                p=busqueda_completa(i,v,w+1,s)
            if type(i) == archivo:
                print("encontrado: nombre: ", i.nombre, ".", i.extencion, "id: ", i.id)
                return i
    return p
def busqueda_id(dir_actual,v):
    try:
        for i in v:
            if type(dir_actual)== carpeta:
                dir_actual = dir_actual.contenido[i]
            if type(dir_actual)== archivo:
                return dir_actual
                'print("encontrado:", dir_actual.nombre, dir_actual.extencion)'
    except:
        'print("no se encontro o ruta desconocida")'
        return None
''' cargar y recorrer una 2 carpetas  con 13 archivos cada una
c=carpeta("master")
c.asignar_id(0)


for i in range(10):
    c.agregar_contenido(archivo(str(i)+".exe"))
c.agregar_contenido(carpeta("carpeta  1"))
c.agregar_contenido(carpeta("carpeta  2"))
for i in c.contenido:
    if type(i)==carpeta:
        for l in range(5):
            i.agregar_contenido(archivo(str(l)+".jpg"))

'print("nombre: ", c.nombre, "id: ", c.id)'
recorrer(c)

'''
'v=[]'
'archivo existente'
'''v.append(11)
v.append(0)'''
'archivo inexistente'
'''v.append(12)
v.append(2)'''
'''
'primer metodo'
start_time = time()
s=(busqueda_completa(c,v,0,None))
if s!=None:
    print(s.nombre,".",s.extencion)
else:
    print("archivo no encontrado")
elapsed_time = time() - start_time
print("termino",elapsed_time)
'''

'segundo de busqueda '
'''
start_time = time()
s=busqueda_id(c,v)
if s!=None:
    print(s.nombre,".",s.extencion)
else:
    print("no se encontro")
elapsed_time = time() - start_time
print("termino",elapsed_time)
'''