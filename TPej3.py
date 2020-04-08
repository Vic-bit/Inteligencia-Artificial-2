import numpy as np
from Aestrella import Aestrella
from almacen import generar_almacen
from almacen import lista_coordenadas
from almacen import seleccionar_producto_aleatorio


if __name__ == '__main__':
    almacen=generar_almacen(3,2)

    lista_productos=seleccionar_producto_aleatorio(almacen,2)
    print("Los productos son: ", lista_productos)

    coordenadas_productos=lista_coordenadas(almacen,lista_productos)

    busqueda=Aestrella(almacen, coordenadas_productos[0],coordenadas_productos[1])

    print("La distancia entre los 2 puntos es: ", busqueda.get_dist())

    if busqueda.get_valor()==True:
        print("Ha llegado al objetivo")
    else:
        print("No lo ha conseguido")