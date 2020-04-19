import numpy as np
from Aestrellaej3 import Aestrellaej3
from almacen import generar_almacen
from almacen import lista_coordenadas
from almacen import seleccionar_producto_aleatorio


if __name__ == '__main__':
    #almacen=generar_almacen(3,2)
    almacen=np.array([[0,0,0,0,0,0,0],
             [0,2,0,1,0,0,0],
             [0,0,0,1,0,3,0],
             [0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0]])
    print(almacen)
    #lista_productos=seleccionar_producto_aleatorio(almacen,2)
    lista_productos=[2,3]
    print("Los productos son: ", lista_productos)

    #coordenadas_productos=lista_coordenadas(almacen,lista_productos)
    inicio=(1,1)
    fin=(2,5)
    busqueda=Aestrellaej3(almacen, inicio, fin) #coordenadas_productos[0],coordenadas_productos[1])

    #print("La distancia entre los 2 puntos es: ", busqueda.get_dist())

    #if busqueda.get_valor()==True:
    #    print("Ha llegado al objetivo")
    #else:
    #    print("No lo ha conseguido")