import numpy as np
from A_estrella_ej3 import A_estrella_ej3
from almacen import generar_almacen
from almacen import lista_coordenadas
from almacen import seleccionar_producto_aleatorio


if __name__ == '__main__':
    almacen=generar_almacen(3,2)
    print(almacen)

    lista_productos=seleccionar_producto_aleatorio(almacen,2)
    print("Los productos son: ", lista_productos)

    coordenadas_productos=lista_coordenadas(almacen,lista_productos)

    busqueda=A_estrella_ej3(almacen, coordenadas_productos[0],coordenadas_productos[1])

    if busqueda.get_valor()==True:
        print("Ha llegado")
        print("El camino es: ")
        print(busqueda.get_camino())
        print("La distancia entre los 2 puntos es: ", busqueda.get_dist())
    else:
        print("No lo ha conseguido")