import threading
import time
def s(a):
    while True:
        print(a)

z=threading.Thread(name="1",target=s,args="1")
x=threading.Thread(name="2",target=s,args="2")
x.start()
z.start()