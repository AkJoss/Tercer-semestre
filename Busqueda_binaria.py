# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:58:35 2024

@author: josea
"""
def Busqueda_Binaria(arr, goal):
    #Definir un inicio y un fin
    inicio = 0
    fin = len (arr)
    acum = 0
    index = []
    while inicio <= fin:
        #calcular el indice del elemento central
        medio = (inicio + fin) // 2
        #Compara el elemento central con el objetivo
        if arr[medio] == goal:
            acum += 1
            index.append(medio)
            #return f"El elemento {goal} se encontro en la posicion {medio}"
        elif arr[medio] < goal:
            inicio = medio + 1 
            #Ajusta el inicio para buscar a la derecha
        else:
            fin = medio - 1
            #Ajusta el fin para buscar en la mitad izquierda
        if acum == 0:
            return f"El valor {goal} no se encontro"
        else:
            return f"EL elemento {goal} se encontro en las posiciones {index}"
listota = [5,14,11,8,6,2,9,4,8,2,1,5,7]
listota.sort()
print(listota)  
nada = 8
print(Busqueda_Binaria(listota, nada))

