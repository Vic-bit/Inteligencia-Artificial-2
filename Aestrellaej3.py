import numpy as np


class NodoA():
    def __init__(self, padre= None, posicion=None):
        self.padre=padre
        self.posicion=posicion
        self.gn=0
        self.hn=0
        self.fn=0


class Aestrellaej3():
    def __init__(self, almacen, inicio, fin):
        nodo_actual=NodoA(None, inicio)
        nodo_objetivo=NodoA(None, fin)
        lista_abierta=[]
        lista_cerrada=[]
        lista_abierta.append(nodo_actual)
        
        it=0
        flag=False
        while(len(lista_abierta)>0):
            lista_cerrada.append(lista_abierta[0])
            lista_abierta.pop(0)

            if nodo_actual.posicion == nodo_objetivo.posicion:
                print("Llegooo")
                for i in range(0, len(self.get_camino(nodo_actual))):
                    print(self.get_camino(nodo_actual)[i].posicion) #print
                self.set_dist(nodo_actual.gn)
                break
            
            if it>100:
                break

            hijos=self.vecinos(almacen, lista_cerrada, nodo_actual)

            #for i in range(0, len(hijos)):
            #    for j in range(0, len(lista_cerrada)):
            #        if hijos[i].posicion==lista_cerrada[j].posicion:
            #            flag=False
                        #break
            #        else:
            #            flag=True
            #    if flag==True:
                    #for l in range(0, len(lista_abierta)):
                    #    if hijos[i].posicion == lista_abierta[l].posicion:
                    #        if hijos[i].gn>lista_abierta[l].gn:
                    #            break
                    #    else:      
            #        lista_abierta.append(hijos[i]) 
            
            for node in hijos:
                if node in lista_cerrada:
                    continue
                elif node in lista_abierta:
                    pass
                else:
                    # Por algún motivo se guardan con hash diferente entre los 2 sets
                    for i in lista_cerrada:
                        if i.posicion == node.posicion:
                            break
                    else:
                        lista_abierta.append(node)
                         

            lista_abierta.sort(key=lambda nodo_actual: nodo_actual.fn) #2/2 se añade
            nodo_actual=lista_abierta[0]
            #print(lista_abierta)
            it=it+1
        print("the end")
        for i in range(0, len(lista_cerrada)):
            print(lista_cerrada[i].posicion)
        

    def vecinos(self, almacen, lista_cerrada, nodo_actual):
        hijos=[]
        n=lista_cerrada[len(lista_cerrada)-1].posicion[0]
        m=lista_cerrada[len(lista_cerrada)-1].posicion[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if n+i>-1 and m+j>-1 and n+i < almacen.shape[0] and m+j <almacen.shape[1]:
                    if n+i==n or m+j==m:
                        if almacen[n+i, m+j]==0 or almacen[n+i,m+j]==3:
                            ubicacion=(n+i,m+j)
                            if ubicacion!=(n,m):
                                nodo_adyacente=NodoA(lista_cerrada[len(lista_cerrada)-1],ubicacion)
                                self.distancia(lista_cerrada,nodo_actual , nodo_adyacente, n, m, i, j, fin) 
                                hijos.append(nodo_adyacente)
        return hijos


    def distancia(self, lista_cerrada, nodo_actual, nodo_adyacente, n, m, i, j, fin):
        nodo_adyacente.gn=1+nodo_actual.gn
        nodo_adyacente.hn = abs(n + i - fin[0]) + abs(m + j - fin[1])
        nodo_adyacente.fn = nodo_adyacente.gn + nodo_adyacente.hn


    def get_camino(self, nodo_actual):
        path = []
        while nodo_actual is not None:
            path.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        return path


    def set_valor(self, valor):
        self.valor=valor


    def get_valor(self):
        return self.valor


    def set_dist(self,dist):
        self.dist=dist


    def get_dist(self):
        return self.dist


if __name__ == '__main__':
    #almacen=generar_almacen(3,2)
    almacen=np.array([[0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0],
             [2,0,0,1,0,3,0],
             [0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0]])
    print(almacen)
    #lista_productos=seleccionar_producto_aleatorio(almacen,2)
    lista_productos=[2,3]
    print("Los productos son: ", lista_productos)

    #coordenadas_productos=lista_coordenadas(almacen,lista_productos)
    inicio=(2,0)
    fin=(2,5)
    busqueda=Aestrellaej3(almacen, inicio, fin) 