from NodoA import NodoA

class Aestrellaaux():
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
        while(len(listaAbierta)>0):        
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

                for i in range(0, len(self.get_camino(nodoActual))):
                    self.get_camino(nodoActual)[i].posicion #print
                self.set_dist(nodoActual.gn)
                break
            if it==0:
                valor_fin=0
            else:
                valor_fin = almacen[nodoobjetivo.posicion]
            n=nodoActual.posicion[0]
            m=nodoActual.posicion[1]    #Recorro los nodos adyacentes, que no se salgan y no sean un muro
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if n + i > -1 and m + j > -1 and n+i < almacen.shape[0] and m+j <almacen.shape[1]:
                        if n + i == n or m + j == m:
                            if almacen[n + i, m + j] == 0 or almacen[n+i,m+j]==valor_fin:
                                for k in range(0, len(listaCerrada)):               #Si están en la lista cerrada no los recorre
                                    if (n+i,m+j) == listaCerrada[k].posicion:
                                        nolistaCerrada = False
                                        break
                                    else:
                                        nolistaCerrada = True
                                if nolistaCerrada==True:
                                    nodoAdyacente = NodoA(nodoActual, (n + i, m + j))
                                    hijos.append(nodoAdyacente)
                                    self.Distancia(nodoActual, nodoAdyacente, n, m, i, j, fin)
                                    nolistaCerrada=False
                                    for k in range(0, len(listaAbierta)):
                                        if (n+i,m+j) == listaAbierta[k].posicion:
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


    def Distancia(self, nodoActual,nodoAdyacente,n,m,i,j,fin):        #Ver el inicio y fin
        if n + i == n or m + j == m:
            nodoAdyacente.gn=1+nodoActual.gn
        else:
            nodoAdyacente.gn=1.4+nodoActual.gn
        nodoAdyacente.hn = abs(n + i - fin[0]) + abs(m + j - fin[1])
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
