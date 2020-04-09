import random
import numpy as np
from NodoA import NodoA

class Aestrella():
    def __init__(self, almacen, inicio, fin):
        raiz=NodoA(None, inicio)
        nodoobjetivo=NodoA(None, fin)    #Inicializo todo
        listaAbierta=[]
        listaCerrada=[]
        listaAbierta.append(raiz)
        hijos=[]
        hijos.append(raiz)  #??
        camino=[]
        camino.append(raiz.posicion)
        
        it=0
        nolistaCerrada=False
        while(len(listaAbierta)>0):          #flag==False and it<100):
            if it==0:                           #Ver este if si está de más
                nodoActual=listaAbierta[0]
            else:
                if nodoActual.posicion==raiz.posicion:
                    nodoActual=hijos[1]
                else:
                    nodoActual = hijos[0]
                camino.append(nodoActual.posicion)
                hijos.clear()
            listaCerrada.append(nodoActual)

            if nodoActual.posicion==nodoobjetivo.posicion:  #Condicion de salida
                self.set_valor(True)
                for p in range(0, len(self.get_camino(nodoActual))):  # Sin el -1 no me reconoce nada
                    print(self.get_camino(nodoActual)[p].posicion)                   
                self.set_dist(nodoActual.gn)
                break
            if it==0:
                valor_fin=0
            else:
                valor_fin = almacen[nodoobjetivo.posicion]
            n=nodoActual.posicion[0]
            m=nodoActual.posicion[1]    #Recorro los nodos adyacentes, que no se salgan y no sean un muro
            o=nodoActual.posicion[2]
            n4=nodoActual.posicion[3]
            n5=nodoActual.posicion[4]
            n6=nodoActual.posicion[5]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for l in range(-1, 2):
                        for p in range(-1, 2):
                            for q in range(-1, 2):
                                for r in range(-1, 2):
                                    if n + i > -1 and m + j > -1 and o+l>-1 and n+i < almacen.shape[0] and m+j <almacen.shape[1] and o+l <almacen.shape[2] and n4 + p > -1 and n5 + q > -1 and n6+r>-1 and n4+p < almacen.shape[3] and n5+q <almacen.shape[4] and n6+r <almacen.shape[5]:
                                        
                                        #if n + i == n or m + j == m:
                                        if almacen[n + i, m + j, o + l, n4+p,n5+q,n6+r] == 0 or almacen[n+i,m+j,o+l, n4+p,n5+q,n6+r]==valor_fin:
                                            for k in range(0, len(listaCerrada)):               #Si están en la lista cerrada no los recorre
                                                if (n+i,m+j,o+l, n4+p,n5+q,n6+r) == listaCerrada[k].posicion:
                                                    nolistaCerrada = False
                                                    break
                                                else:
                                                    nolistaCerrada = True
                                            if nolistaCerrada==True:
                                                nodoAdyacente = NodoA(nodoActual, (n + i, m + j, o+l, n4+p,n5+q,n6+r))
                                                hijos.append(nodoAdyacente)
                                                self.Distancia(nodoActual, nodoAdyacente, n, m, o, n4, n5, n6, i, j, l, p, q, r, fin)
                                                nolistaCerrada=False
                                                for k in range(0, len(listaAbierta)):
                                                    if (n+i,m+j,o+l, n4+p,n5+q,n6+r) == listaAbierta[k].posicion:
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
            #    hijos.pop(0)                                    #Problema de un solo hijo
            hijos.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            listaAbierta.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            it=it+1


    def get_camino(self, nodoActual):
        path = []
        while nodoActual is not None:
            path.append(nodoActual)
            nodoActual = nodoActual.padre
        return path


    def Distancia(self, nodoActual,nodoAdyacente,n,m,o,n4,n5,n6,i,j,l,p,q,r,fin):        #Ver el inicio y fin
        if n + i == n or m + j == m or o+l==o or n4+p==n4 or n5+q==n5 or n6+r==n6:
            nodoAdyacente.gn=1+nodoActual.gn
        else:
            nodoAdyacente.gn=1.4+nodoActual.gn
        nodoAdyacente.hn = abs(n + i - fin[0]) + abs(m + j - fin[1]) +abs(o+l-fin[2])+abs(n4 + p - fin[3]) + abs(n5 + q - fin[4]) +abs(n6+l-fin[5])
        nodoAdyacente.fn = nodoAdyacente.gn + nodoAdyacente.hn
        return 1


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




if __name__ == '__main__':
    N=10
    almacen=np.zeros((N,N,N,N,N,N))
    inicio = tuplaAleatoria(N,6) 
    fin = tuplaAleatoria(N, 6)  

    porcentajeObstaculos=N*N*N*50/100   #Hacer una funcion
    while porcentajeObstaculos>0:
        obs1 = random.randrange(0, N)
        obs2 = random.randrange(0, N)
        obs3 = random.randrange(0, N)
        obs4 = random.randrange(0, N)
        obs5 = random.randrange(0, N)
        obs6 = random.randrange(0, N)
        almacen[obs1,obs2,obs3,obs4,obs5,obs6]=1
        porcentajeObstaculos=porcentajeObstaculos-1
    #print(almacen)

    busqueda=Aestrella(almacen,inicio,fin)
    print(busqueda.get_valor())
    

    if busqueda.get_valor()==True:
        print("Ha llegado al objetivo!!!!!!!!!!!!!!!!!")
    else:
        print("No lo ha conseguido")
