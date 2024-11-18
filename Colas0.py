# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:55:48 2024

@author: josea
"""
class Cola:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        #verificar que la cola esta vacia baby
        return len(self.items) == 0
        
    def encolar(self, item):
        #agregar un elemento al rear de la colar
        self.items.append(item)
            
    def desencolar(self):
        #eliminamos el elemento frontal
        if self.is_empty():
            raise IndexError("La cola esta vacia no se puede desencolar.")
        return self.items.pop(0)
        
    def size(self):
        #obtener el tamaño de la cola
        return len(self.items)
        
    def peek(self):
        if self.is_empty():
            raise IndexError("La cola esta vacia no se puede desencolar.")
        return self.items[0]
        
q = Cola()
print(q.is_empty())
q.encolar("Le grute")
print(q.is_empty())
print(q.size())
print(q.peek())
q.encolar("Scarlet Johanson")
print(q.size())
q.desencolar()
print(q.size())
print(q.peek())




