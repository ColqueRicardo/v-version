from timeit import timeit
from time import time
import xml.etree.ElementTree as ET


'''for i in range(0,100):
    print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))'''
# Start counting.

start_time = time()
# Take the original function's return value.
# Calculate the elapsed time.

bd=ET.Element("base")
ventana=ET.SubElement(bd,"ventana", name="ventana-consultas")
ventana_hide=ET.SubElement(ventana,"ventana-hide",)
ventana_hide.set("option-hide","false")
ET.dump(bd)
tree = ET.ElementTree(bd)
tree.write("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")


estructura_xml = ET.parse("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")
# Obtiene el elemento raíz:
raiz = estructura_xml.getroot()

'''for ventana in raiz.findall('ventana'):
    print(ventana)
    print("espacio1")
    print(ventana.get("option-hide"))

print("nada")
'''
for ventana in raiz.iter('ventana'):
    print("get: "+str(ventana.get("option-hide")))
    ventana.set("option-hide","0")
    print(ventana.get("option-hide"))

estructura_xml.write("C:/Users/ricar/Desktop/pruebas v1/pruebasv1.xml")



'''v=[]
for i in range(100):
    v.append("gkaseqwoeqwpwkq"*10000)
    v[i]="gkaseqwoeqwpwkq"'''

elapsed_time = time() - start_time
print(time())
print(start_time)
print("Elapsed time: %0.10f seconds." % elapsed_time)
