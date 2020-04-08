import random
from almacen import generar_almacen_aleatorio
from almacen import lista_coordenadas
from Aestrella import Aestrella
from NodoA import NodoA

class Genoma():
    def __init__(self, listagen):
        self.listagen=listagen
        self.costo=0
        self.probabilidad=0


class Algoritmo_Genetico():
    def __init__(self, tamaño, orden):
        self.tamaño=tamaño

        poblacion=self.poblacion_inicial(self.tamaño)


        it=0
        while it<200:

            self.idoneidad(poblacion,orden)

            nueva_generacion=[]

            for i in range(0, 4):

                x=self.seleccion(poblacion)
                y=self.seleccion(poblacion)

                hijos=self.cruce_basado_ciclos(x,y)

                r=random.random()
                if r<0.15:
                    hijos=self.mutar_intercambio(hijos)

                #for j in range(0, len(hijos)):
                #    nueva_generacion.append(hijos[j])
                nueva_generacion.append(hijos[0])
                nueva_generacion.append(hijos[1])

            poblacion=nueva_generacion

            print("-----------------")

            it=it+1
        print("Termino el algoritmo")
        self.idoneidad(poblacion, orden)
        self.set_mejor_individuo(poblacion)

        self.get_mejor_individuo()
        print(self.get_mejor_individuo().costo)
        print(self.get_mejor_individuo().listagen)


    def poblacion_inicial(self, tamaño):
        poblacion=[]
        #maximo = almacen[2::].max()  # maximo valor de la matriz
        for i in range(0,tamaño):
            listagen = []
            while len(listagen) < tamaño:
                a = random.randrange(1, tamaño+1)
                if a not in listagen:
                    listagen.append(a)
                    individuo=Genoma(listagen)
            poblacion.append(individuo)
        return poblacion


    def idoneidad(self, poblacion, orden):
        for j in range(0, len(poblacion)):
            almacen = generar_almacen_aleatorio(1, 1, poblacion[j].listagen)
            coordenadas = lista_coordenadas(almacen, orden)
            for i in range(0, len(coordenadas)):
                if i == 0:  # Respecto a la bahía de carga
                    AE1 = Aestrella(almacen, (0, 0), coordenadas[i])
                    dm = AE1.get_dist()
                    #dm = abs(0 - coordenadas[i][0]) + abs(0 - coordenadas[i][1])
                else:
                    AE2 = Aestrella(almacen, coordenadas[i - 1], coordenadas[i])
                    dm = AE2.get_dist()
                    #dm = abs(coordenadas[i - 1][0] - coordenadas[i][0]) + abs(coordenadas[i - 1][1] - coordenadas[i][1])
                poblacion[j].costo = poblacion[j].costo + dm
        return poblacion[j].costo


    def seleccion(self, poblacion):
        fitness_total=0
        for i in range(0, len(poblacion)):
            fitness_total=fitness_total+poblacion[i].costo
        lista_fitness_menor=[]
        for i in range(0, len(poblacion)):
            lista_fitness_menor.append((1-poblacion[i].costo/fitness_total))
        sum=0
        for i in range(0, len(poblacion)):
            sum=sum+lista_fitness_menor[i]
        for i in range(0, len(poblacion)):
            poblacion[i].probabilidad=lista_fitness_menor[i]/sum
            print("Costo: ",poblacion[i].costo, "y Probabiidad: ", poblacion[i].probabilidad)
        indice = [0, 1, 2, 3, 4, 5, 6, 7]
        pesos = [poblacion[0].probabilidad, poblacion[1].probabilidad, poblacion[2].probabilidad, poblacion[3].probabilidad,
                 poblacion[4].probabilidad, poblacion[5].probabilidad, poblacion[6].probabilidad, poblacion[7].probabilidad]
        resultado = []  # Lista que almacena el resultado

        for i, p in zip(indice, pesos):
            resultado += [i] * int(p * 100)
        indice_elegido=random.choice(resultado)
        return poblacion[indice_elegido]


    def cruce_basado_ciclos(self,x,y):
        indices = []
        ciclos = []
        diccionario1 = {}
        diccionario2 = {}
        cont = 0
        while len(indices) < len(x.listagen):
            ciclos.append([])
            flag = True
            for i in range(0, len(x.listagen)):
                if i not in indices:
                    indices.append(i)
                    ciclos[cont].append(i)
                    diccionario1[i] = x.listagen[i]
                    diccionario2[i] = y.listagen[i]
                    break
            it = 0
            while flag == True:
                for i in range(0, len(x.listagen)):
                    if x.listagen[i] == diccionario2[ciclos[cont][it]]:
                        if i not in indices:
                            indices.append(i)
                            ciclos[cont].append(i)
                            diccionario1[i] = x.listagen[i]
                            diccionario2[i] = y.listagen[i]
                            break
                        else:
                            flag = False
                            break
                it = it + 1
            cont = cont + 1

        dic_hijo_1 = {}
        dic_hijo_2 = {}
        for i in range(0, len(ciclos)):
            for j in range(0, len(ciclos[i])):
                for k in range(0, len(x.listagen)):
                    if i % 2 == 0:
                        dic_hijo_1[ciclos[i][j]] = diccionario1[ciclos[i][j]]
                        dic_hijo_2[ciclos[i][j]] = diccionario2[ciclos[i][j]]
                    else:
                        dic_hijo_1[ciclos[i][j]] = diccionario2[ciclos[i][j]]
                        dic_hijo_2[ciclos[i][j]] = diccionario1[ciclos[i][j]]
        hijo_1_lista = []
        hijo_2_lista = []
        for i in range(0, len(x.listagen)):
            hijo_1_lista.append(dic_hijo_1[i])
            hijo_2_lista.append(dic_hijo_2[i])
        hijo_1=Genoma(hijo_1_lista)
        hijo_2=Genoma(hijo_2_lista)
        hijos= [hijo_1, hijo_2]
        return hijos


    def mutar_intercambio(self, hijos):
        r1 = random.randrange(0, len(hijos[0].listagen))
        r2 = random.randrange(0, len(hijos[0].listagen))
        r3 = random.randrange(0, len(hijos[1].listagen))
        r4 = random.randrange(0, len(hijos[1].listagen))
        a=hijos[0].listagen[r1]
        b=hijos[0].listagen[r2]
        hijos[0].listagen[r1]=b
        hijos[0].listagen[r2]=a
        c=hijos[1].listagen[r3]
        d=hijos[1].listagen[r4]
        hijos[1].listagen[r3]=d
        hijos[1].listagen[r4]=c
        return hijos

    def set_mejor_individuo(self, poblacion):
        for i in range(1, len(poblacion)):
            if poblacion[i].costo>=poblacion[i-1].costo:
                minimo=poblacion[i-1].costo
        for i in range(0 , len(poblacion)):
            if poblacion[i].costo==minimo:
                self.individuo=poblacion[i]

    def get_mejor_individuo(self):
        return self.individuo

