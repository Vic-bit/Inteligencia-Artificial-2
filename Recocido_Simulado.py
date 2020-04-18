import random
import math
from NodoRS import NodoRS
from almacen import generar_almacen
from almacen import seleccionar_producto_aleatorio
from almacen import lista_coordenadas
from Aestrella import Aestrella

class Recocido_Simulado():
    def __init__(self, almacen, lista_productos):
        self.temperatura=100
        
        nodo_actual=NodoRS(lista_productos)

        self.distancia_entre_productos(almacen, nodo_actual)
        print("La distancia incial es de: ", nodo_actual.dist)

        it=0
        while it<1000:
            self.temperatura=self.temperatura*0.99  #0.9= constante de enfriamiento

            if self.temperatura<0.001: #Tf=10
                #return nodo_actual
                break

            nodo_siguiente=NodoRS(lista_productos)
            random.shuffle(nodo_siguiente.lista_productos)

            self.distancia_entre_productos(almacen, nodo_siguiente)

            dE=nodo_siguiente.dist-nodo_actual.dist

            if dE<0:
                nodo_actual=nodo_siguiente
            else:
                r=random.random()
                if r<math.exp(-dE/self.temperatura):
                    nodo_actual=nodo_siguiente

            it=it+1
        print("La lista de productos ordenada es: ", nodo_actual.lista_productos)
        print("La distancia final es de: ", nodo_actual.dist)


    def distancia_entre_productos(self, almacen, NodoRS):
        coordenadas = lista_coordenadas(almacen, NodoRS.lista_productos)
        for i in range(0, len(coordenadas)):
            if i == 0:  # Respecto a la bahía de carga
                AE1 = Aestrella(almacen, (0, 0), coordenadas[i])
                dm = AE1.get_dist()
            else:
                AE2 = Aestrella(almacen, coordenadas[i-1], coordenadas[i])
                dm = AE2.get_dist()
            NodoRS.dist = NodoRS.dist + dm
        return NodoRS.dist
    """def distancia_manhattan(self, NodoRS):
        coordenadas=lista_coordenadas(almacen, NodoRS.lista_productos)
        for i in range(0, len(coordenadas)):
            if i==0:                                #Respecto a la bahía de carga
                dist1=Aestrella(alamacen, (0,0), lista_coordenadas(alamacen,lista_productos)[0])
                print(dist1.get_dist())
                dm = abs(0 - coordenadas[i][0]) + abs(0 - coordenadas[i][1])
            else:
                dm = abs(coordenadas[i-1][0] - coordenadas[i][0]) + abs(coordenadas[i-1][1] - coordenadas[i][1])
            NodoRS.dist = NodoRS.dist + dm
        return NodoRS.dist
     """
