import random
import time

def seleccionJugador1():
    random.seed(time.time())
    jugadorinicial=random.randint(0,1)
    print("Empieza ",end="")    
    if jugadorinicial==0:
        print(p1.get("nombre") + "!\n")
    else:
        print(p2.get("nombre") + "!\n")
    return jugadorinicial