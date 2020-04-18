import numpy as np
import random
import math
from almacen import generar_almacen
from almacen import seleccionar_producto_aleatorio
from almacen import lista_coordenadas
from Recocido_Simulado import Recocido_Simulado


if __name__ == '__main__':
    N=3 #Cantidad de elementos en la lista
    almacen=generar_almacen(3,2)
 
    lista_productos=seleccionar_producto_aleatorio(almacen,N)
    print("La lista inicial es: ", lista_productos)

    Recocido_Simulado(almacen,lista_productos)