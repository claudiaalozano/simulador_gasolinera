import time
import threading

def crear_hilos():
    for i in range(50):
        hilo = threading.Thread(target=llenar_tanque)
        hilo.start()

def llenar_tanque():
    global cantidad
    cantidad = 0
    while cantidad < 100:
        cantidad += 1
        time.sleep(0.1)
        print("Cantidad: ", cantidad)
