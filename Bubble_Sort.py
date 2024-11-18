# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:44:02 2024

@author: josea
"""
import time
import random

def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        #print(f"Pasada,", i)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #intercambiar
                #print (arr)
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
                #print(f"Se intercambia {arr[j]} por {arr[j+1]}")
                #print (arr)
        #print(f"Fin de pasada,", i)
    return arr

#ejemplo de uso
#arr = [5,3,8,4,2]
arr = [random.randint(1,100) for i in range(50000)]
#medir el tiempo de ejecución
start_time = time.time()
print(Bubble_Sort(arr))
print(Bubble_Sort(arr))
#Termine de ordenar el arreglo
end_time = time.time()
#mostrar el tiempo de ejecución
print(f"Ordenar {len(arr)} numeros lleva:\n ")
print("Tiempo de ejecucion: {:.9f} segundos".format(end_time - start_time))
