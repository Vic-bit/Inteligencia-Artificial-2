import random
import numpy as np
from A_estrella_ej2 import A_estrella_ej2 


def tuplaAleatoria(N, cantComponentes):
    tuplaAleatoria = []
    for i in range(1,cantComponentes+1):
        a=random.randrange(0,N)
        tuplaAleatoria.append(a)
    return tuple(tuplaAleatoria)


def obstaculosAleatorios(espacioArticular, porcentajeObstaculos):
    cantidadObstaculos=N*N*N*N*N*N*porcentajeObstaculos/100
    while cantidadObstaculos>0:
        obs1 = random.randrange(0, N)
        obs2 = random.randrange(0, N)
        obs3 = random.randrange(0, N)
        obs4 = random.randrange(0, N)
        obs5 = random.randrange(0, N)
        obs6 = random.randrange(0, N)
        if espacioArticular[obs1,obs2,obs3,obs4,obs5,obs6]==0:
            espacioArticular[obs1,obs2,obs3,obs4,obs5,obs6]=1
            cantidadObstaculos=cantidadObstaculos-1
    return espacioArticular


if __name__ == '__main__':
    N=10
    grados=360/N
    print("Discretizado cada ", grados, "°")
    espacioArticular=np.zeros((N,N,N,N,N,N))
    inicio = tuplaAleatoria(N,6) 
    fin = tuplaAleatoria(N, 6)
    print("Posición articular inicial: ", inicio)
    print("Posición articular final: ", fin)
    porcentajeObstaculos=50
    print("Porcentaje de obstáculos: ", porcentajeObstaculos)
    obstaculosAleatorios(espacioArticular, porcentajeObstaculos)
    busqueda=A_estrella_ej2(espacioArticular ,inicio,fin) 

    if busqueda.get_valor()==True:
        print("Ha llegado al objetivo")
    else:
        print("No lo ha conseguido")
