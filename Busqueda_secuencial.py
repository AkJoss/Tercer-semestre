# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:06:15 2024

@author: josea
"""

#Busqueda Lineal

def Busqueda_Secuencial(arr, goal):
    acum = 0
    index = []
    for i in range(len(arr)):
        if arr[i] == goal:
            acum += 1
            index.append(i)
    if acum == 0:
        return f"No se encontro el valor {goal}"
    else:  
        #return acum, index
        return f"El valor {goal} buscado se encontro {acum} vece(s) en las posiciones {index}"
            
listota = [5,14,11,8,6,2,9,4,8,2,1,5,7]
nada = 1000
#cantidad, posiciones = Busqueda_Secuencial(listota, nada))
print (Busqueda_Secuencial(listota, nada))
