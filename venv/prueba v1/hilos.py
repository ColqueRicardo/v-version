import threading
import time
def prueba(id,id1,id3):
    while True:
        print(id,id1,id3)
        time.sleep(1)

s1=threading.Thread(name="s",target=prueba,args={1,2,3})
s2=threading.Thread(name="s",target=prueba,args={4,5,6})
s1.start()
s2.start()