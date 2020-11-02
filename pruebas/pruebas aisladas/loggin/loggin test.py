import logging
import socket
import sys

'basicamente sirve para dar registros de error para un mejor mantenimiento y mejor manejo de errores'

logging.basicConfig( format='%(asctime)s - %(message)s', level=logging.DEBUG ,filename='app.log', filemode='w')
logging.debug("esto es una prueba de namae: %s IP: %s",socket.gethostname(),socket.gethostbyname(socket.gethostname()))

try:
    print(0/0)
except Exception as e:

    logging.error("division sobre '0' de %s",socket.gethostname(), exc_info=True)
    print("Error OS: {0}".format(e))
    for i in range(len(sys.exc_info())):
        print(sys.exc_info()[i])
        print(i)
    print(e)
    print(e.args)
