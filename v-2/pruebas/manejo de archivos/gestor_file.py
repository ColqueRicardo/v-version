from io import  open
r="C:/Users/ricar/Desktop/prueba v2.docx"
r2="C:/Users/ricar/Desktop/pruebav2"
r3=r2+"/v2.docx"
'a -->bits, b-->str, c-->para escritura'
a= open(r,"rb")
b=open(r,"r")
lectura=a.read()
'''print(type(b.read()))
print(type(True), type(a.read()))'''

c=open(r3,"wb")
c.write(lectura)
c.close()

c=open(r3,"rb")
print(c.read())
print(lectura)
