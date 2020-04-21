import numpy as np
import random
from almacen import generar_almacen
from almacen import seleccionar_producto_aleatorio
from almacen import lista_coordenadas
from Recocido_Simulado import Recocido_Simulado


if __name__ == '__main__':
    N=3                            #Cantidad de elementos en la lista
    almacen=generar_almacen(3,2)
    temperatura_inicial=100
    print("La temperatura incial es: ", temperatura_inicial)
    temperatura_final=0.001
    print("La temperatura final es: ", temperatura_final)
    constante_enfriamiento=0.99
    print("El coeficiento de enfriamiento es: ", constante_enfriamiento)
    lista_productos=seleccionar_producto_aleatorio(almacen,N)
    print("La lista inicial es: ", lista_productos)

    Recocido_Simulado(almacen,lista_productos,temperatura_inicial,temperatura_final,constante_enfriamiento)