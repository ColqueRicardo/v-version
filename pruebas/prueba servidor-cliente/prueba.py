import pickle
import io

def codificar_mensaje(mensaje):
    mensaje_codificado=""
    for i in range (len(mensaje)):
        mensaje_codificado=mensaje_codificado  + str(mensaje[i])+"\n"
    return mensaje_codificado.encode()

def decoficar_mensaje(mensaje):
    i=0
    lasti=0
    vec=[]
    mensaje=str(mensaje).replace("'","").replace("[","").replace("]","").replace('"',"")
    while i<len(str(mensaje)):
        if str(mensaje)[i:i+1]=="\n":
            vec.append(str(mensaje)[lasti:i])
            lasti=i+1
        i=i+1
    return vec

'''
print("empieza")
vec=[]
vec.append("hola1")
vec.append("hola2")
vec.append("hola3")
s=gestor_mensaje()
s.codificar_mensaje(vec)

a=s.decoficar_mensaje(s.mensaje_codificado)

for i in range (len(a)):
    print(a[i]==vec[i])
'''