import time
import threading
import queue
import random


class Gasolinera():
    def __init__(self,n_surtidores):
        self.cola = []
        self.pila = [True] * n_surtidores
        self.n_surtidores = n_surtidores
        self.tiempo_repostaje = 0
        self.tiempo_pago = 3

    def surtidor(self):
         for surtidor in self.surtidores:
            if not surtidor.ocupado:
                return surtidor
              
    def run(self, coche, n_surtidores):
        self.cola.append(coche)
        print(f'Coche {coche} ha llegado a la gasolinera\n')
        for i in enumerate(n_surtidores):
                    # Comprobamos si hay algún coche en la cola y si hay surtidores disponibles
                        if self.cola and True in self.pila:
                            coche = self.cola.pop(0)
                            surtidor = self.pila.index(True)
                            self.pila[surtidor] = False
                            
                            self.tiempo_repostaje = random.randint(10, 15)
                            print(f'Coche {coche} ha llegado al surtidor {surtidor}. Tiempo de repostaje: {self.tiempo_repostaje} minutos.')
                            
                            self.tiempo_pago = 3
                            surtidor = self.pila.index(False)
                            print(f'Coche {coche} ha terminado de repostar en el surtidor {surtidor}. Pasando al tiempo de pago.')
                    
                            
                        
                        elif not self.cola and False in self.pila and self.tiempo_repostaje == 0 and self.tiempo_pago > 0:
                            self.tiempo_pago -= 1
                
                            if self.tiempo_pago == 0:
                                surtidor = self.pila.index(False)
                                self.pila[surtidor] = True
                                print(f'Coche {coche} ha terminado de repostar. Pasando al tiempo de pago es : {self.tiempo_repostaje + 3}.')
                    
                    
                        
    

class Coche(threading.Thread):
    def __init__(self, gasolinera, coche, n_surtidores):
        threading.Thread.__init__(self)
        self.gasolinera = gasolinera
        self.coche = coche
        self.n_surtidores = n_surtidores
        self.lock = threading.Lock()
        self.lock.acquire()

    def run(self):
        self.gasolinera.run(self.coche, self.n_surtidores)
        self.lock.acquire()
        return

if __name__ == '__main__':
    n_surtidores = 3
    gasolinera = Gasolinera(n_surtidores)
    n_surtidores = [threading.Lock() for i in range(n_surtidores)]
    coches = [Coche(gasolinera, i, n_surtidores) for i in range(10)]
    for coche in coches:
        coche.start()
    for coche in coches:
        coche.join()

    print('Todos los coches han terminado de repostar.')

