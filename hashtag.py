# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:35:53 2024

@author: josea
"""
class HashTable:
    def __init__(self, size):
        #metodo constructor paera inicializar tabla hash
        self.size = size
        self.table = [None] * size #crear una lista de tamaño size
        
    def isEmpty(self):
        #metodo para verificar si la tabla hash 
        #esta vacia
        for i in range(self.size):
            #recorrer cada posicion de la tabla
            if self.table[i] is not None: 
                return False
            #si encontramos una posicion no vacia, la tabla
            #no esta vacia
        return True
    
    def size(self):
        #metodo para obtener el numeor de elementos en la tabla hash
        
        ratero = 0
        for i in range(self.size):
            #recorremos cada posicion de la tabla
            if self.table[i] is not None:
                #si la posicion no esta vacia, aumentamos un contador
                #contador
                ratero += 1
            return ratero #devolver el numero total de elemntos
        
        def hashfunction(self, key):
            #metodo para calcular el inidice a partir de la clave
            if isinstance(key, int):
                #si la clave es un entero, usamos el modulo del
                #tamaño de la tabla
                return key % self.size
            elif isinstance(key, str):
                #si la clave es una cadena, sumamos los valores
                # ASCII
                total = 0
                for char in key:
                    total += ord(char)
                return total % self.size
            
            def add(self, key, value):
                #metodo para agregar una clave(llave) y su valor 
                #a la tabla hash
                index = self.hashfunction(key)#calculamos el 
                #indice usando la funcion hash
                self.table[index] = (key, value)
                #almacenamos el par key-value en el index calculado
                
            def getByKey(self, key):
                #Este es un metodo para obetener un valor a partir de la clave
                index = self.hashfunction(key)
                if self.table[index] is not None:
                    #si en ese indice hay un elemento
                    if self.table[index][0] == key:
                        #y la clave coincide, devolvemos el valor a asociar
                        return self.table[index][1]
                    #sino encotnramos la clave, devolvemos None
                    return None
                
            def getByValue(self, value):
                #metodo para obtener una clave a partir de su valor
                for i in range(self.size):
                    #recorrer cada posicion de la tabla
                    if self.table[i][1] == value:
                        #y el valor coincide, devolvemos la clave
                        #asociada
                        return self.table[i][0]
                #sino encontramos el valor, devolvemos None
                return None
#Creamos una tabla de valor definido
hash_table = hash_table(5)

#agregar dos claves que generar el mismo indice
hash_table.add(1, "valor1") #hashfunction(1) % 5 -->
hash_table.add(6, "valor2") #hashfunction(6) % 5 -->

#obtenemos los valores de ambas claves
print(hash_table.getByKey(1)) #--> Devolver "valor 1"
print(hash_table.getByKey(6)) #--> Devolver "valor 2"
                    