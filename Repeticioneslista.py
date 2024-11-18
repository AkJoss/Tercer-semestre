# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:44:01 2024

@author: josea
"""
cobalto = [1,2,-7,4,5,8]

def contador(gatito):  
    ash_fabito = 0 #Esto es un contador
    for datito in gatito:
        ash_fabito += 1
    return ash_fabito

def invertir(perrito):
    entomatada = contador(perrito)
    i = entomatada - 1
    inversa = []
    while i >= 0:
        inversa.append(perrito[i])
        i -= 1
    return inversa

def par_impar(tornillos):
    pares = []
    impares = []
    for i in range(contador(tornillos)):
        if tornillos[i] % 2 == 0:
           pares.append(tornillos[i])
        else:
           impares.append(tornillos[i])
    return pares, impares

def matzimo_array(sobig):
    matzimo = sobig[0]
    i = 1
    for i in range (contador(sobig)):
        if matzimo < sobig[i]:
            matzimo = sobig[i]
            #print(sobig[i])
            
            return matzimo
    
def minimo_array(sobig):
    minimo = sobig[0]
    i = 1
    for i in range (contador(sobig)):
        if minimo > sobig[i]:
            minimo = sobig[i]
            #print(sobig[i])
            
            return minimo
#listota = [1,9,5,3,6,4]
#listota = [1.1,1.6,1.2,1.7,1.3,1.4]
#listota = [-10,-5,-6,-7,-1,-2]
#print("El matzimo es:", matzimo_array(listota))
#print("El minimo es:", minimo_array(listota)) 

def sumar_array(limon, naranja):
    perro = []
    if contador(naranja) == contador(limon):
        for i in range(contador(naranja)):
            perro.append(naranja[i] + limon[i])
            
        return perro

l1 = [5,4,-1,3,0]
l2 = [-1,5,8,9,10]

#print(sumar_array(l1,l2))

def duplicates(pelitos):
    yolo = []
    for dato in pelitos:
        encontrado = 0
        for unico in yolo:
            if dato == unico:
                encontrado = 1
                break
        if not encontrado:
                yolo.append(dato)
    return yolo
    
pepino = [1,5,6,4,1,5,7,8]
print("La lista otiginal es:", pepino)
print("\nLa lista sin repeticiones es:", duplicates(pepino))
       
#lista = [1,2,3,4,5,6,7]
#pares, impares= par_impar(lista)
#print("La lista es:", lista)
#print("Los pares son:", pares)
#print("Los impares son", impares)

#guayaba = contador(cobalto)
#print("La cantidad es:", guayaba)
#inv = invertir(cobalto)
#print("La lista original es:", cobalto)
#print("La cantidad es:", inv)


