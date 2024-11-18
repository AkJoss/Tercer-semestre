# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:39:27 2024

@author: Alumno
"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Pila:
    def __init__(self):
        self.superior = None
    
    def apilar (self,dato):
        print(f"Agregando {dato} a la cima de la pila")
        #si no hay datos, agregar elemento en el elemento superior        
        if self.superior == None:
            self.superior = Nodo(dato)
            return 0 
        
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
        
    def desapilar(self):
        #si no hay datos en el nodo superior, regeresamos
        if self.superior == None:
            print("No hay ningun elemento en la pila para desapilar")
            return 0
        print(f"Desapilar {self.superior.dato}")
        self.superior = self.superior.siguiente 
    
    def imprimir(self):
        print("Imprimiendo la fila")
        #Recorrer la pila e imprimir valores
        nodo_temporal = self.superior 
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}",end = ",")
            nodo_temporal = nodo_temporal.siguiente 
            print("")

#Uso de la pila
pila = Pila()
pila.apilar("Leon S. Kennedy")
pila.apilar("Bob Esponja")
pila.apilar("Henry Cavil")
pila.imprimir()
pila.desapilar()
pila.imprimir()
pila.desapilar()
pila.imprimir()
pila.apilar("Nicolas Maduro")
pila.imprimir()    