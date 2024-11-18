# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:48:35 2024

@author: josea
"""
import random

def Shell_Sort(A):
    #incicializar el tamano de la lista
    n=len(A)
    #Empezar con el intervalo igual a la mitad del tam de la lista
    gap = int(n/2) #n//2
    #continuar reduciendo el intervalo hasta llegar a 0
    while gap > 0:
        #recorrer la lista desde el indice igual al 
        #intervalo o gap hasta el final
        for i in range(gap, n):
            #guardar el valor actual en una varible temporal
            temp = A[i]
            #inicializar la variable j en la posicion i
            j = i
            #desplazar los elementos del subarreglo
            #ordenado si son mayores que el valor temporal
            while j >= gap and A[j-gap] > temp:
                A[j] = A[j-gap]
                j -= gap
            #insertar el valor temporal en la posicion
            #correcta
            A[j] = temp
        #print(A)
            #Reducir el gap
        gap //= 2
        
#ejemplo de uso
#arreglo = [8, 6, 7, 2, 1, 4, 5, 3]
arr = [random.randint(1, 500) for i in range(30000)]
Shell_Sort(arr)
print("Lista ordenada usando ShellSort: ", arr)