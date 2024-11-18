# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:08:34 2024

@author: josea
"""
import random
import time
def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n-1):
        aux = arr[i]
        j = i - 1
        while j>=0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = aux
        return arr
    
#ejemplo de uso
#arr = [5,3,8,4,2]
arr = [random.randint(1,100) for i in range(50000)]
#medir el tiempo de ejecución
start_time = time.time()
print(Insertion_Sort(arr))
#Termine de ordenar el arreglo
end_time = time.time()
#mostrar el tiempo de ejecución
print(f"Ordenar {len(arr)} numeros lleva:\n ")
print("Tiempo de ejecucion: {:.6f} segundos".format(end_time - start_time))