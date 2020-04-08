import numpy as np
import random
import math
#--------------Agregar a almacen-------------------
def generar_almacen(cant_filas_estanterias,cant_columnas_estanterias):
    estante=0
    almacen=np.zeros((6*cant_filas_estanterias,4*cant_columnas_estanterias))
    for l in range(0, cant_columnas_estanterias):
        for k in range(0,cant_filas_estanterias):
            for i in range(0,6):
                for j in range(0,4):
                    if j!=0 and j!=3 and i!=0 and i!=5:
                        estante=estante+1
                        almacen[i+k*6,j+l*4]=estante
    return np.array(almacen)

#--------------Agregar a almacen-------------------
def seleccionar_producto_aleatorio(almacen, cant_productos):
    maximo=almacen[2::].max()   #maximo valor de la matriz
    lista_productos= []
    while len(lista_productos)<cant_productos:
        a=random.randrange(1,maximo)
        if a not in lista_productos:
            lista_productos.append(a)
    return lista_productos

#--------------Agregar a almacen-------------------
def lista_coordenadas(almacen, lista_productos):
    lista_coodenadas= []
    for i in lista_productos:
        a=np.where(almacen == i)
        #b=a[0]
        #c=a[1]
        lista_coodenadas.append(a)
    return lista_coodenadas

#------------------------------------------------
def generar_almacen_aleatorio(cant_filas_estanterias,cant_columnas_estanterias,orden_estanterias):
    estante=-1
    almacen=np.zeros((6*cant_filas_estanterias,4*cant_columnas_estanterias))
    for l in range(0, cant_columnas_estanterias):
        for k in range(0,cant_filas_estanterias):
            for i in range(0,6):
                for j in range(0,4):
                    if j!=0 and j!=3 and i!=0 and i!=5:
                        estante=estante+1
                        almacen[i+k*6,j+l*4]=orden_estanterias[estante]
    return np.array(almacen)