import random
import numpy as np
from NodoA import NodoA

class Aestrella():
    def __init__(self, espacioArticular, inicio, fin):
        raiz=NodoA(None, inicio)
        nodoobjetivo=NodoA(None, fin)    #Inicializo todo
        listaAbierta=[]
        listaCerrada=[]
        listaAbierta.append(raiz)
        hijos=[]
        hijos.append(raiz)
        
        it=0
        nolistaCerrada=False
        while(len(listaAbierta)>0):       
            if it==0:                           #Ver este if si está de más
                nodoActual=listaAbierta[0]
            else:
                if nodoActual.posicion==raiz.posicion:
                    nodoActual=hijos[1]
                else:
                    nodoActual = hijos[0]
                hijos.clear()
            listaCerrada.append(nodoActual)

            if nodoActual.posicion==nodoobjetivo.posicion:  #Condicion de salida
                self.set_valor(True)
                for p in range(0, len(self.get_camino(nodoActual))): 
                    print(self.get_camino(nodoActual)[p].posicion)                   
                self.set_dist(nodoActual.gn)
                break
            
            n1=nodoActual.posicion[0]
            n2=nodoActual.posicion[1]
            n3=nodoActual.posicion[2]
            n4=nodoActual.posicion[3]
            n5=nodoActual.posicion[4]
            n6=nodoActual.posicion[5]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for l in range(-1, 2):
                        for p in range(-1, 2):
                            for q in range(-1, 2):
                                for r in range(-1, 2):
                                    if n1 + i > -1 and n2 + j > -1 and n3+l>-1 and n1+i < espacioArticular.shape[0] and n2+j <espacioArticular.shape[1] and n3+l <espacioArticular.shape[2] and n4 + p > -1 and n5 + q > -1 and n6+r>-1 and n4+p < espacioArticular.shape[3] and n5+q <espacioArticular.shape[4] and n6+r <espacioArticular.shape[5]:
                                        if espacioArticular[n1 + i, n2 + j, n3 + l, n4+p, n5+q, n6+r] == 0 or espacioArticular[n1+i, n2+j, n3+l, n4+p, n5+q, n6+r]== espacioArticular[nodoobjetivo.posicion]:
                                            for k in range(0, len(listaCerrada)):            
                                                if (n1+i, n2+j, n3+l, n4+p, n5+q, n6+r) == listaCerrada[k].posicion:
                                                    nolistaCerrada = False
                                                    break
                                                else:
                                                    nolistaCerrada = True
                                            if nolistaCerrada==True:
                                                nodoAdyacente = NodoA(nodoActual, (n1+i, n2+j, n3+l, n4+p, n5+q, n6+r))
                                                hijos.append(nodoAdyacente)
                                                self.distancia(nodoActual, nodoAdyacente, n1, n2, n3, n4, n5, n6, i, j, l, p, q, r, fin)
                                                nolistaCerrada=False
                                                for k in range(0, len(listaAbierta)):
                                                    if (n1+i, n2+j, n3+l, n4+p, n5+q, n6+r) == listaAbierta[k].posicion:
                                                        nolistaAbierta=False
                                                        break
                                                    else:
                                                        nolistaAbierta=True
                                                if nolistaAbierta==True:
                                                    listaAbierta.append(nodoAdyacente)
                                                    nolistaAbierta=False
            for i in range(0,len(hijos)):
                for j in range(0, len(listaAbierta)):
                    if hijos[i].posicion==listaAbierta[j].posicion:
                        if hijos[i].gn>listaAbierta[j].gn:
                            hijos[i].padre=listaAbierta[j].padre

            listaAbierta.pop(0)
            #if len(hijos)>1:
            #    hijos.pop(0)                              
            hijos.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            listaAbierta.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            it=it+1


    def get_camino(self, nodoActual):
        camino = []
        while nodoActual is not None:
            camino.append(nodoActual)
            nodoActual = nodoActual.padre
        return camino


    def distancia(self, nodoActual,nodoAdyacente,n1,n2,n3,n4,n5,n6,i,j,l,p,q,r,fin):        #Ver el inicio y fin
        if n1 + i == n1 or n2 + j == n2 or n3+l==n3 or n4+p==n4 or n5+q==n5 or n6+r==n6:
            nodoAdyacente.gn=1+nodoActual.gn
        else:
            nodoAdyacente.gn=1.4+nodoActual.gn
        nodoAdyacente.hn = abs(n1+i-fin[0]) + abs(n2+j-fin[1]) + abs(n3+l-fin[2])+abs(n4+p-fin[3]) + abs(n5+q-fin[4]) + abs(n6+r-fin[5])
        nodoAdyacente.fn = nodoAdyacente.gn + nodoAdyacente.hn


    def set_valor(self, valor):
        self.valor=valor


    def get_valor(self):
        return self.valor


    def set_dist(self,dist):
        self.dist=dist


    def get_dist(self):
        return self.dist


def tuplaAleatoria(N, cantComponentes):
    tuplaAleatoria = []
    for i in range(1,cantComponentes+1):
        a=random.randrange(0,N)
        tuplaAleatoria.append(a)
    return tuple(tuplaAleatoria)


def obstaculosAleatorios(porcentajeObstaculos):
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
    espacioArticular=np.zeros((N,N,N,N,N,N))
    #inicio = tuplaAleatoria(N,6) 
    #fin = tuplaAleatoria(N, 6)  
    inicio=(1,0,9,7,4,2)
    fin=(5,5,5,5,5,5)
    porcentajeObstaculos=100
    
    busqueda=Aestrella(obstaculosAleatorios(porcentajeObstaculos),inicio,fin) 

    if busqueda.get_valor()==True:
        print("Ha llegado al objetivo")
    else:
        print("No lo ha conseguido")
