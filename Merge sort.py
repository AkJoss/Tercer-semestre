# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:49:41 2024

@author: josea
"""
import random

def Merge_Sort(A):
    #Verificar si la lista tiene mas de un elemento(sino, ya esta
    #ordenada)
    n = len(A)
    if n > 1:
        #Encontrar el punto medio de la lista 
        medio = n // 2 #Siempre agarro la parte entera
        #Dividir la lista en dos mitades
        izquierda = A[:medio]
        derecha = A[medio:]
        
        #llamar a merge sort en ambas mitades
        Merge_Sort(izquierda)
        Merge_Sort(derecha)
        
        #inicializamos los indices para recorrer cada mitad y la
        #lista principal
        #i: derecha
        #j: derecha
        #k: original
        i = 0
        j = 0
        k = 0
        
        #combinamos las dos mitades en una sola lista ordenada
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                A[k] = izquierda[i]
                i += 1
            else:
                A[k] = derecha[j]
                j += 1
            k += 1
        
            #Agregar los elementos restantes a la izquierda si los hay
        while i < len(izquierda):
            A[k] = izquierda[i]
            i += 1
            k += 1
            
            #Agregar los elementos restantes a la derecha si los hay
        while j < len(derecha):
            A[k] = derecha[j]
            j +=1
            k += 1
        #print(A)
        
#ejemplo de uso
#arreglo = [2, 124, 23, 5, 89, -1, 44, 643, 34]
arr = [random.randint(1, 500) for i in range(30000)]
Merge_Sort(arr)

print("Lista ordenada usando Merge Sort: \n", arr)
