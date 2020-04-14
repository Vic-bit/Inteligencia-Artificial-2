import random
from collections import Counter


class Maquina():
    def __init__(self, desocupada):
        self.desocupada=desocupada
        self.tiempo=0
        self.variables={}


class Backtraking():
    def __init__(self, variables, dominio, restricciones_precedencia, restricciones_recursos, maquinas, contador): 
        self.contador=contador
        
        asignamiento=[]
        resultado=self.vuelta_atras_recursiva(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas)
        if type(resultado)==bool:
            print("No se pudo completar la asignación")
        else:
            for i in range(0, len(resultado)):
                print("La tarea ", resultado[i][0]," se realiza en el tiempo ", resultado[i][1]) 


    def vuelta_atras_recursiva(self, variables, dominio, asignamiento,restricciones_precedencia, restricciones_recursos, maquinas):
        if len(asignamiento)==len(variables):
            asignamiento_completo={}
            for i in range(0, len(maquinas)):
                asignamiento_completo.update(maquinas[i].variables)
            asignamiento_ordenado=sorted(asignamiento_completo.items(), key=lambda x: x[1])
            return asignamiento_ordenado

        self.contador=self.contador+1
        if self.contador>100:
            return False

        var=self.seleccionar_variable_sin_asignar(variables, asignamiento, restricciones_precedencia)

        for i in range(0, len(dominio)):
            if self.consistente(variables, var, i, asignamiento, restricciones_precedencia, restricciones_recursos)==True:
                asignamiento.append(var)
                resultado = self.vuelta_atras_recursiva(variables, dominio, asignamiento,restricciones_precedencia, restricciones_recursos, maquinas)
                if resultado != False:
                    return resultado
                asignamiento.pop(asignamiento.index(var))
        else:
            resultado = self.vuelta_atras_recursiva(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas)
            if resultado != False:
                return resultado
        return False    


    def seleccionar_variable_sin_asignar(self, variables, asignamiento, restricciones_precedencia): #elijo la variable mas restringida
    #    aleatorio=[]
    #    for i in variables.keys():
    #        aleatorio.append(i)
    #    for i in range(0, len(restricciones_precedencia)):
    #        aleatorio.append(restricciones_precedencia[i][0])
    #    flag=False
    #    while flag==False:
    #        var=random.choice(aleatorio)
    #        if var not in asignamiento:
    #            flag=True
    #    return var
    
        r = restricciones_precedencia
        a = [i[1][0] for i in r.items()]
        count = Counter(a).items()
        count = sorted(count, key=lambda x: x[1])
        count = [i[0] for i in count if i[0] not in asignamiento]
        count = count + [i[0] for i in variables.items() if i[0]
                         not in count and i[0] not in asignamiento]
        return count[0]


    def consistente(self, variables, var, i, asignamiento, restricciones_precedencia, restricciones_recursos):

        for rp in range(0, len(restricciones_precedencia)):
            if var == restricciones_precedencia[rp][1]:
                if restricciones_precedencia[rp][0] not in asignamiento:
                    return False

        tiempo=i   
        tiempo_limite=len(dominio)
        if tiempo+variables[var]>tiempo_limite:
            return False

        if tiempo>=restricciones_recursos[var].tiempo:
            restricciones_recursos[var].desocupada=True

        if var not in restricciones_recursos[var].variables.keys() and restricciones_recursos[var].desocupada==True:
            restricciones_recursos[var].variables[var]=tiempo
            restricciones_recursos[var].tiempo=variables[var]+tiempo
            restricciones_recursos[var].desocupada=False
        else:
            return False

        return True


if __name__ == '__main__':
    variables={"T1": 5, "T2": 15, "T3": 10, "T4": 30}
    tiempo_limite=60
    asignamiento=[]
    dominio=[]
    for i in range(0, tiempo_limite):
        dominio.append(i)

    #T2 debe realizarse antes que T3
    #T4 debe realizarse antes que T1
    #T4 debe realizarse antes que T3
    restricciones_precedencia={0 : ("T2","T3"), 1 : ("T4","T1"), 2 : ("T4","T3")}

    M1 = Maquina(True)
    M2 = Maquina(True)
    maquinas=[M1,M2]
    #T1 ocupa la máquina 1
    #T2 ocupa la máquina 1
    #T3 ocupa la máquina 2
    #T4 ocupa la máquina 2
    restricciones_recursos={"T1" : M1, "T2" : M1, "T3" : M2, "T4" : M2} #2 máquinas de diferente tipo cada una

    res=Backtraking(variables, dominio, restricciones_precedencia, restricciones_recursos, maquinas,0)

