import numpy as np
import random
import math
from almacen import generar_almacen
from almacen import seleccionar_producto_aleatorio
from almacen import lista_coordenadas
from Recocido_Simulado import Recocido_Simulado




if __name__ == '__main__':
    N=4 #Cantidad de elementos en la lista
    almacen=generar_almacen(3,2)
    print(almacen)
    lista_productos=seleccionar_producto_aleatorio(almacen,N)
    print("La lista final es: ", lista_productos)
    print(lista_coordenadas(almacen,lista_productos))

    Recocido_Simulado(almacen,lista_productos)





#    numbers = [10, 20, 30, 40, 50, 60]
#    print("Original list: ", numbers)
#    #random.seed(4)
#    random.shuffle(numbers)
#    print("reshuffled list ", numbers)
#    print(lista_productos)
#    lista_productos_siguiente=random.shuffle(lista_productos)
#    print(lista_productos_siguiente)

    #Recocido_Simulado()





"""def generar_almacen(filas,columnas):
    almacen = []
    a = [0, 0, 0, 0]
    b = [0, 1, 1, 0]
    if columnas==1:
        c=a
        d=b
    if columnas>1:
        c=a
        d=b
        for i in range(1, columnas):
            c=c+a
            d=d+b
    for i in range(0, filas):
        for j in range(0, 6):
            if j==0 or j==5:
                #for k in range(0, columnas):
                almacen.append(c)
            else:
                #for k in range(0, columnas):
                almacen.append(d)
    return np.array(almacen)
"""

#    a=np.where(almacen==1)      #posicion de un elemento
#    print(a)
#    almacen[a]=0
#    b=np.where(almacen==2)
#    lista=[a,b]
#    print(lista)

#def array_to_point(array):
#    print(array)
#    x = array[0][0]
#    y = array[1][0]
#    return (x, y)

"""def lista_tupla_aleatoria(matriz, cant_componentes, cant_tuplas):
    filas=matriz.shape[0]
    columnas=matriz.shape[1]
    lista_aleatoria = []
    for j in range(1, cant_tuplas):
        tupla_aleatoria = []
        for i in range(1, cant_componentes + 1):
            i = random.randrange(0, N)
            tupla_aleatoria.append(i)
            tuple(tupla_aleatoria)
    return lista_aleatoria
"""