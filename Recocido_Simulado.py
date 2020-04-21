import random
import math
from NodoRS import NodoRS
from almacen import generar_almacen
from almacen import seleccionar_producto_aleatorio
from almacen import lista_coordenadas
from A_estrella_ej3 import A_estrella_ej3


class Recocido_Simulado():
    def __init__(self, almacen, lista_productos, temperatura_inicial, temperatura_final,constante_enfriamiento):
        self.temperatura=temperatura_inicial
        self.temperatura_final=temperatura_final
        self.constante_enfriamiento=constante_enfriamiento
        nodo_actual=NodoRS(lista_productos)

        self.distancia_entre_productos(almacen, nodo_actual)
        print("La distancia incial es de: ", nodo_actual.dist)

        it=0
        while it<1000:
            self.decaimiento_temperatura() 

            if self.temperatura<0.001:
                break

            nodo_siguiente=NodoRS(lista_productos)
 
            self.vecino(nodo_siguiente)

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


    def decaimiento_temperatura(self):
        self.temperatura=self.temperatura*self.constante_enfriamiento


    def vecino(self, nodo_siguiente):
        flag=False
        while flag==False:
            r1 = random.randrange(0, len(nodo_siguiente.lista_productos))
            r2 = random.randrange(0, len(nodo_siguiente.lista_productos))
            if r1!=r2:
                flag=True
        a = nodo_siguiente.lista_productos[r1]
        b = nodo_siguiente.lista_productos[r2] 
        nodo_siguiente.lista_productos[r1]=b
        nodo_siguiente.lista_productos[r2]=a


    def distancia_entre_productos(self, almacen, NodoRS):
        coordenadas = lista_coordenadas(almacen, NodoRS.lista_productos)
        for i in range(0, len(coordenadas)):
            if i == 0:  # Respecto a la bahía de carga
                AE1 = A_estrella_ej3(almacen, (0, 0), coordenadas[i])
                dm = AE1.get_dist()
            else:
                AE2 = A_estrella_ej3(almacen, coordenadas[i-1], coordenadas[i])
                dm = AE2.get_dist()
            NodoRS.dist = NodoRS.dist + dm
        return NodoRS.dist




