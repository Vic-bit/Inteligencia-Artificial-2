from NodoA import NodoA


class A_estrella_ej3():
    def __init__(self, almacen, inicio, fin):
        nodo_actual=NodoA(None, inicio)
        nodo_objetivo=NodoA(None, fin)
        lista_abierta=[]
        lista_cerrada=[]
        lista_abierta.append(nodo_actual)
        
        it=0
        nolista_abierta=False
        nolista_cerrada=False
        while(len(lista_abierta)>0):
            lista_cerrada.append(lista_abierta[0])
            


            if nodo_actual.posicion == nodo_objetivo.posicion:
                camino=""
                salto_de_linea="\n"
                for i in range(0, len(self.get_senda(nodo_actual))):
                    self.get_senda(nodo_actual)[i].posicion
                    camino=camino+salto_de_linea+str(self.get_senda(nodo_actual)[i].posicion)
                self.set_valor(True)
                self.set_camino(camino)
                self.set_dist(nodo_actual.gn)
                break
            
            if it>500:
                break
            
            if it==0:
                valor_fin=0
            else:
                valor_fin = almacen[nodo_objetivo.posicion]

            hijos=[]
            n=lista_cerrada[len(lista_cerrada)-1].posicion[0]
            m=lista_cerrada[len(lista_cerrada)-1].posicion[1]
            for i in range(-1,2):
                for j in range(-1,2):
                    if n+i>-1 and m+j>-1 and n+i < almacen.shape[0] and m+j <almacen.shape[1]:
                        if n+i==n or m+j==m:
                            if almacen[n+i, m+j]==0 or almacen[n+i,m+j]==valor_fin:
                                ubicacion=(n+i,m+j)
                                if ubicacion!=(n,m):
                                    for k in range(0, len(lista_cerrada)):           
                                        if (n+i,m+j) == lista_cerrada[k].posicion:
                                            nolista_cerrada = False
                                            break
                                        else:
                                            nolista_cerrada = True
                                    if nolista_cerrada==True:
                                        nodo_adyacente=NodoA(lista_cerrada[len(lista_cerrada)-1],ubicacion)
                                        self.distancia(lista_cerrada,nodo_actual , nodo_adyacente, n, m, i, j, fin) 
                                        hijos.append(nodo_adyacente)
                                        
                                        if it==0:
                                            lista_abierta.append(nodo_adyacente)
                                        else:
                                            for k in range(0, len(lista_abierta)):
                                                if (n+i,m+j) == lista_abierta[k].posicion:
                                                    nolista_abierta=False
                                                    break
                                                else:
                                                    nolista_abierta=True
                                            if nolista_abierta==True:
                                                lista_abierta.append(nodo_adyacente)
            for i in range(0,len(hijos)):
                for j in range(0, len(lista_abierta)):
                    if hijos[i].posicion==lista_abierta[j].posicion:
                        if hijos[i].gn<lista_abierta[j].gn:
                            hijos[i].padre=lista_abierta[j].padre


            lista_abierta.sort(key=lambda nodo_actual: nodo_actual.fn)
            if len(lista_abierta)>1:
                lista_abierta.pop(0)
            nodo_actual=lista_abierta[0]
            it=it+1
            
        
    def distancia(self, lista_cerrada, nodo_actual, nodo_adyacente, n, m, i, j, fin):
        nodo_adyacente.gn=1+nodo_actual.gn
        nodo_adyacente.hn = abs(n + i - fin[0]) + abs(m + j - fin[1])
        nodo_adyacente.fn = nodo_adyacente.gn + nodo_adyacente.hn


    def get_senda(self, nodo_actual):
        senda = []
        while nodo_actual is not None:
            senda.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        return senda


    def set_valor(self, valor):
        self.valor=valor


    def get_valor(self):
        return self.valor


    def set_dist(self,dist):
        self.dist=dist


    def get_dist(self):
        return self.dist


    def set_camino(self, camino):
        self.camino=camino


    def get_camino(self):
        return self.camino
