import random
from collections import Counter


class Maquina():
    def __init__(self,tipo, desocupada):
        self.tipo=tipo
        self.desocupada=desocupada
        self.tiempo=0
        self.tareas={}


class Backtraking():
    def __init__(self, tareas, dominio, restricciones_precedencia, restricciones_maquinas, maquinas, contador): 
        self.contador=contador
        
        asignamiento=[]
        resultado=self.vuelta_atras_recursiva(tareas, dominio, asignamiento, restricciones_precedencia, restricciones_maquinas, maquinas)
        if type(resultado)==bool:
            print("No se pudo completar la asignación")
        else:
            print("El periodo de inicio de cada tarea es: ")
            for i in range(0, len(resultado)):
                print("La tarea ", resultado[i][0]," se realiza en el tiempo ", resultado[i][1])
                if i>1 and resultado[i][1] >= resultado[i-1][1] and tareas[resultado[i][0]] >= tareas[resultado[i-1][0]]:
                    j=i
                if i==len(resultado)-1:
                    tiempo_final=resultado[i][1]+tareas[resultado[j][0]]
            print("El trabajo estará terminado en el tiempo: ", tiempo_final)


    def vuelta_atras_recursiva(self, tareas, dominio, asignamiento,restricciones_precedencia, restricciones_maquinas, maquinas):
        if len(asignamiento)==len(tareas):
            asignamiento_completo={}
            for i in range(0, len(maquinas)):
                asignamiento_completo.update(maquinas[i].tareas)
            asignamiento_ordenado=sorted(asignamiento_completo.items(), key=lambda x: x[1])
            return asignamiento_ordenado

        self.contador=self.contador+1
        if self.contador>100:
            return False

        var=self.seleccionar_variable_sin_asignar(tareas, asignamiento, restricciones_precedencia)

        for i in range(0, len(dominio)):
            if self.consistente(tareas, var, i, asignamiento, restricciones_precedencia, restricciones_maquinas)==True:
                asignamiento.append(var)
                resultado = self.vuelta_atras_recursiva(tareas, dominio, asignamiento,restricciones_precedencia, restricciones_maquinas, maquinas)
                if resultado != False:
                    return resultado
                asignamiento.pop(asignamiento.index(var))
        else:
            resultado = self.vuelta_atras_recursiva(tareas, dominio, asignamiento, restricciones_precedencia, restricciones_maquinas, maquinas)
            if resultado != False:
                return resultado
        return False    


    def seleccionar_variable_sin_asignar(self, tareas, asignamiento, restricciones_precedencia): #elijo la variable mas restringida
        r = restricciones_precedencia
        a = [i[1][0] for i in r.items()]
        count = Counter(a).items()
        count = sorted(count, key=lambda x: x[1], reverse=True)
        count = [i[0] for i in count if i[0] not in asignamiento]
        count = count + [i[0] for i in tareas.items() if i[0]
                         not in count and i[0] not in asignamiento]
        return count[0]


    def consistente(self, tareas, var, i, asignamiento, restricciones_precedencia, restricciones_maquinas):
        for rp in range(0, len(restricciones_precedencia)):
            if var == restricciones_precedencia[rp][1]:
                if restricciones_precedencia[rp][0] not in asignamiento:
                    return False

        tiempo=i   
        tiempo_limite=len(dominio)
        if tiempo+tareas[var]>tiempo_limite:
            return False

        if tiempo>=restricciones_maquinas[var].tiempo:
            restricciones_maquinas[var].desocupada=True

        if var not in restricciones_maquinas[var].tareas.keys() and restricciones_maquinas[var].desocupada==True:
            restricciones_maquinas[var].tareas[var]=tiempo
            restricciones_maquinas[var].tiempo=tareas[var]+tiempo
            restricciones_maquinas[var].desocupada=False
        else:
            return False

        return True


if __name__ == '__main__':
    tareas={"T1": 5, "T2": 15, "T3": 10, "T4": 30}
    #tareas={"T1": 5, "T2": 15, "T3": 10, "T4": 30, "T5": 35, "T6": 25, "T7": 20}
    tiempo_limite=0
    for keys,values in tareas.items():
        print("La tarea ",keys, " tiene una duración de ",values)
        tiempo_limite=tiempo_limite+values
    print("El tiempo límite es de: ", tiempo_limite)
    print(" ")
    asignamiento=[]
    dominio=[]
    for i in range(0, tiempo_limite):
        dominio.append(i)
    restricciones_precedencia={0 : ("T2","T3"), 1 : ("T4","T1"), 2 : ("T4","T3")}
    #restricciones_precedencia={0 : ("T2","T3"), 1 : ("T4","T1"), 2 : ("T4","T3"), 3 : ("T5","T6"), 4 : ("T6","T7"), 5 : ("T2","T5")}
    for i in range(0, len(restricciones_precedencia)):
        print("La tarea ", restricciones_precedencia[i][0], " debe realizarse antes de que la tarea " , restricciones_precedencia[i][1])
    print(" ")

    M1 = Maquina("Maquina_1",True)
    M2 = Maquina("Maquina_2",True)
    #M3 = Maquina("Maquina_3",True)
    maquinas=[M1,M2]
    restricciones_maquinas={"T1" : M1, "T2" : M1, "T3" : M2, "T4" : M2} 
    #restricciones_maquinas={"T1" : M1, "T2" : M1, "T3" : M2, "T4" : M2, "T5" : M3, "T6" : M3, "T7" : M1} 
    for keys,values in restricciones_maquinas.items():
        print("La tarea", keys, " usa la ", values.tipo)
    print("---------------------------------------------------------")

    res=Backtraking(tareas, dominio, restricciones_precedencia, restricciones_maquinas, maquinas,0)