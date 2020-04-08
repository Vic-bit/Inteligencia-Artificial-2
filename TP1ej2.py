import numpy as np
import random
import TP1ej5TempleSimulado



class Nodo():
    def __init__(self, padre= None, posicion=None):
        self.padre = padre
        self.posicion=posicion
        self.gn=0
        self.hn=0
        self.fn=0

class Aestrella():
    def __init__(self, almacen, inicio, fin):
        raiz=Nodo(None, inicio)
        nodoobjetivo=Nodo(None, fin)    #Inicializo todo
        listaAbierta=[]
        listaCerrada=[]
        listaAbierta.append(raiz)
        hijos=[]
        hijos.append(raiz)  #??
        camino=[]
        camino.append(raiz.posicion)

        flag=False
        it=0
        nolistaCerrada=False
        while(len(listaAbierta)>0):
            if it==0:                           #Ver este if si está de más
                nodoActual=listaAbierta[0]
            else:
                nodoActual=hijos[0]
                camino.append(nodoActual.posicion)
                hijos.clear()
            listaCerrada.append(nodoActual)

            if nodoActual.posicion==nodoobjetivo.posicion:  #Condicion de salida
                print("Termino")
                self.set_valor(True)
                for p in range(0, len(self.get_camino(nodoActual))):  # Sin el -1 no me reconoce nada
                    print(self.get_camino(nodoActual)[p].posicion)
                break

            n=nodoActual.posicion[0]
            m=nodoActual.posicion[1]
            o=nodoActual.posicion[2]    #Recorro los nodos adyacentes, que no se salgan y no sean un muro
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for l in range (-1,2):
                        if n + i > -1 and n + i < almacen.shape[0] and m + j > -1 and m + j < almacen.shape[1] and o+l>-1 and o+l< almacen.shape[2]:
                            if almacen[n + i, m + j, o + l ] == 0:
                                for k in range(0, len(listaCerrada)):               #Si están en la lista cerrada no los recorre
                                    if (n+i,m+j,o+l) == listaCerrada[k].posicion:
                                        nolistaCerrada = False
                                        break
                                    else:
                                        nolistaCerrada = True
                                if nolistaCerrada==True:
                                    nodoAdyacente = Nodo(nodoActual, (n + i, m + j, o + l))
                                    hijos.append(nodoAdyacente)
                                    self.Distancia(nodoActual, nodoAdyacente, n, m, o, i, j, l, fin)
                                    nolistaCerrada=False
                                    for k in range(0, len(listaAbierta)):
                                        if (n+i,m+j,o+l) == listaAbierta[k].posicion:
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
            if len(hijos)>1:
                hijos.pop(0)                                    #Problema de un solo hijo
            hijos.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            listaAbierta.sort(key=lambda nodoAdyacente: nodoAdyacente.fn)
            
        self.set_valor(False)


    def get_camino(self, nodoActual):
        path = []
        while nodoActual is not None:
            path.append(nodoActual)
            nodoActual = nodoActual.padre
        return path


    def set_valor(self, valor):
        self.valor=valor


    def get_valor(self):
        return self.valor


    def Distancia(slef, nodoActual,nodoAdyacente,n,m,o,i,j,l,fin):        #Ver el inicio y fin
        if n + i == n or m + j == m or o +l == o:
            nodoAdyacente.gn=1+nodoActual.gn
        else:
            nodoAdyacente.gn=1.4+nodoActual.gn
        nodoAdyacente.hn = abs(n + i - fin[0]) + abs(m + j - fin[1]) + abs(o + l - fin[2])
        nodoAdyacente.fn = nodoAdyacente.gn + nodoAdyacente.hn
        return 1


def tuplaAleatoria(N, cantComponentes):
    tuplaAleatoria = []
    for i in range(1,cantComponentes+1):
        a=random.randrange(0,N)
        tuplaAleatoria.append(a)
    return tuple(tuplaAleatoria)



if __name__ == '__main__':
    N=5
    print(TP1ej5TempleSimulado.generar_almacen(3,2))
    almacen=np.zeros((N,N,N))
    inicio = print(tuplaAleatoria(N,3))
    fin = print(tuplaAleatoria(N, 3))

    porcentajeObstaculos=N*N*N*50/100
    while porcentajeObstaculos>0:
        obsx = random.randrange(0, N)
        obsy = random.randrange(0, N)
        obsz = random.randrange(0, N)
        almacen[obsx,obsy,obsz]=1
        porcentajeObstaculos=porcentajeObstaculos-1
    print(almacen)

    busqueda=Aestrella(almacen,inicio,fin)
    print(busqueda.get_valor())

    if busqueda.get_valor()==True:
        print("Ha llegado al objetivo!!!!!!!!!!!!!!!!!")
    else:
        print("No lo ha conseguido")