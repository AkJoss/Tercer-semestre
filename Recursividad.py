# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:13:23 2024

@author: josea
"""
#factorial sin recursividad
import time
def factorial_1(n):
    tamal = 1
    for i in range(2, n+1):
        tamal = tamal * i 
    return tamal

#Factorial con recursividad
def factorial_2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_2(n-1)
    
    
#Ejemplo de uso
numerito = 1558
inicio = time.time()
print(f"El factorial de {numerito} es {factorial_2(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio}s")