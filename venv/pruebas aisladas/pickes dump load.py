import io
import pickle


import venv
import sys
sys.path.append("C:/Users/ricar/PycharmProjects/v-version/venv/pruebas aisladas/objetos pruebas")
from ob1 import arbol

a=arbol()
a.crece()
a.mostrar()
a.obtener_vec()

with open("C:/Users/ricar/PycharmProjects/v-version/venv/pruebas aisladas/objetos pruebas/pickled_obj", "wb") as f:
    pickle.dump(a, f)
with open("C:/Users/ricar/PycharmProjects/v-version/venv/pruebas aisladas/objetos pruebas/pickled_obj", "rb") as f:
    b = pickle.load(f)

print(a==b)
print(a,b)
a.mostrar()
b.mostrar()