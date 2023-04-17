import time
import threading
import queue

class Gasolinera():
    def crear_hilos():
        for i in range(50):
            hilo = threading.Thread(target=llenar_tanque)
            hilo.start()
    
    def coche_hilo(coche_id):
        print(f"Car {coche_id} arrived at the gas station.")
        time.sleep(15)
        print(f"Car {coche_id} is waiting for a dispenser.")
        while True:
            for i, lock in enumerate(dispenser_locks):
                if lock.acquire(blocking=False):
                    print(f"Car {coche_id} is refueling at dispenser {i}.")
                    time.sleep(15)
                    lock.release()
                    print(f" {coche_id} El coche ha terminado de repostar {i}.")
                    return

def llenar_tanque():
    global cantidad
    cantidad = 0
    while cantidad < 100:
        cantidad += 1
        time.sleep(0.1)
        print("Cantidad: ", cantidad)
