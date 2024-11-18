# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:20:01 2024

@author: josea
"""
import random

puchamon = []
contador = 0

for i in range(random.randint(1,20)):
    puchamon.append(random.randint(0, 30))
    contador += 1
    
print(puchamon)
print("El tamaño del array es: ", contador)
print()

def tamalitos(greñas): #Greñas es el arreglo
    contador = 0
    running = True
    if not greñas:
        return 0
    else:
        while running:
            greñas.pop(0)
            contador += 1
            #if greñas is None:
            if not greñas:
                running = False
    return contador

print(tamalitos(puchamon))