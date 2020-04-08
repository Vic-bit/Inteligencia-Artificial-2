from almacen import generar_almacen_aleatorio
from almacen import generar_almacen
from Algoritmo_Genetico import Algoritmo_Genetico
from Algoritmo_Genetico import Genoma


if __name__ == '__main__':
    orden=[8,7,2]
    #listaaa=[8,7,5,4,1,2,3,6]
    #almacen=generar_almacen_aleatorio(1,1,listaaa)
    #almacen=generar_almacen(1,1)
    #print(almacen)
    Algoritmo_Genetico(8, orden)

