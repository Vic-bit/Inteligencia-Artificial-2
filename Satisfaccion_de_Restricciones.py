import random
from collections import Counter

class Maquina():
    def __init__(self, desocupada):
        self.desocupada=desocupada
        self.tiempo=0
        self.variables={}


class Backtraking(): #return solution o failure
    def __init__(self, variables, dominio, restricciones_precedencia, restricciones_recursos, maquinas):
        #self.variables=variables
        #self.dominio=dominio
        #self.asignamiento=asignamiento
        #self.restricciones_precedencia=restricciones_precedencia
        #self.restricciones_recursos=restricciones_recursos

        asignamiento=[]
        tiempo_limite=60
        asignamiento_temporal={}
        resultado=self.vuelta_atras_recursiva(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas, asignamiento_temporal)
        print(resultado)


    def vuelta_atras_recursiva(self, variables, dominio, asignamiento,restricciones_precedencia, restricciones_recursos, maquinas, asignamiento_temporal):
        #if len(asignamiento)>0:
        #    sum=0
        #    asignamiento_temporal={}
        #    for i in range(0, len(asignamiento)):
        #        if asignamiento[i] not in asignamiento_temporal:
        #            sum=variables[asignamiento[i]]+sum
        #            asignamiento_temporal[asignamiento[i]]=sum
            #print(asignamiento_temporal)
        
        if len(asignamiento)==len(variables):
            asignamiento_completo={}
            #for maq in restricciones_recursos.values():
            #    if maq.variables.values() != asignamiento_completo.values():
            #        asignamiento_completo.update(maq.variables)
            for i in range(0, len(maquinas)):
                asignamiento_completo.update(maquinas[i].variables)

            print(asignamiento_completo)
            return asignamiento
        var=self.seleccionar_variable_sin_asignar(variables, asignamiento, restricciones_precedencia)
        print(var)
        #asignamiento.append(var)
        for i in range(0, len(dominio)):
            if self.consistente(variables, var, i, asignamiento, restricciones_precedencia, restricciones_recursos, tiempo_limite)==True:
                asignamiento.append(var)
                resultado = self.vuelta_atras_recursiva(variables, dominio, asignamiento,restricciones_precedencia, restricciones_recursos, maquinas, asignamiento_temporal)
                if resultado != False:
                    return resultado
                asignamiento.pop(asignamiento.index(var))
        else:
            resultado = self.vuelta_atras_recursiva(variables, dominio, asignamiento, restricciones_precedencia, restricciones_recursos, maquinas, asignamiento_temporal)
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


    def consistente(self, variables, var, i, asignamiento, restricciones_precedencia, restricciones_recursos, tiempo_limite):

        for rp in range(0, len(restricciones_precedencia)):
            if var == restricciones_precedencia[rp][1]:
                if restricciones_precedencia[rp][0] not in asignamiento:
                    return False

        #tiempo=i
        #for j in range(0, len(asignamiento)):
        #    tiempo=tiempo+variables[asignamiento[j]]
        #tiempo = tiempo + variables[var]
        #if tiempo>tiempo_limite:
        #    return False

        tiempo=i
        asignamiento_auxiliar=[]
        for j in range(0, len(asignamiento)):
            asignamiento_auxiliar.append(asignamiento[j])
        asignamiento_auxiliar.append(var)

        #for j in range(0, len(asignamiento_auxiliar)):
        #    if asignamiento_auxiliar[j] not in restricciones_recursos[asignamiento_auxiliar[j]].variables.keys:
        #        restricciones_recursos[asignamiento_auxiliar[j]].variables[asignamiento_auxiliar[j]]=variables[asignamiento_auxiliar[j]]
        #        restricciones_recursos[asignamiento_auxiliar[j]].tiempo=variables[asignamiento_auxiliar[j]]
        for j in restricciones_recursos.values():   #Ver el tema de que la se libera la máquina
            if tiempo>= j.tiempo:                   #Según la máquina en cuestion es el tiempo
                j.desocupada=True        

        if var not in restricciones_recursos[var].variables.keys() and restricciones_recursos[var].desocupada==True:
            restricciones_recursos[var].variables[var]=tiempo#variables[var]+tiempo
            restricciones_recursos[var].tiempo=variables[var]+tiempo
            restricciones_recursos[var].desocupada=False
        else:

            return False

        #print(restricciones_recursos[var].variables)

            #if tiempo==restricciones_recursos[asignamiento_auxiliar[j]].tiempo:
            #    restricciones_recursos[asignamiento_auxiliar[j]].desocupada=True
        

        #for j in range(0, len(asignamiento_auxiliar)):
        #    if tiempo==restricciones_recursos[asignamiento_auxiliar[j]].tiempo:
        #        restricciones_recursos[asignamiento_auxiliar[j]].desocupada=True
        #    if asignamiento_auxiliar[j] not in restricciones_recursos[asignamiento_auxiliar[j]].variables: 
        #        restricciones_recursos[asignamiento_auxiliar[j]].variables=asignamiento_auxiliar[j]
        #    else:
        #        return False
        #    if restricciones_recursos[asignamiento_auxiliar[j]].desocupada==True:
        #            restricciones_recursos[asignamiento_auxiliar[j]].desocupada=False 
        #            restricciones_recursos[asignamiento_auxiliar[j]].tiempo=tiempo
        #    else: 
        #        return False

        
        #if restricciones_recursos[var].desocupada==False:
            #return False

        return True

        #for r in variables.keys():
        #    if var == restricciones_recursos[r]:
        #for m in range(0, len(restricciones_recursos)):
        #    if restricciones_recursos[var][m].desocupada==False:
        #        return False

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

    #T1 ocupa la máquina 1
    #T2 ocupa las máquinas 2 y 3
    #T3 ocupa la máquina 4
    #T4 ocupa las máquinas 1 y 3

    M1 = Maquina(True)
    M2 = Maquina(True)
    maquinas=[M1,M2]
    restricciones_recursos={"T1" : M1, "T2" : M1, "T3" : M2, "T4" : M2} #2 máquinas de diferente tipo cada una

    res=Backtraking(variables, dominio, restricciones_precedencia, restricciones_recursos, maquinas)

