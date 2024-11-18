# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:16:29 2024

@author: alas0
"""

class HashTable:
    def __init__(self, size):
        # Método constructor para inicializar tabla hash
        self.size = size
        self.table = [None] * size  # Crear una lista de tamaño size
        
    def isEmpty(self):
        # Método para verificar si la tabla hash está vacía
        for i in range(self.size):
            # Recorrer cada posición de la tabla
            if self.table[i] is not None: 
                return False
        # Si encontramos una posición no vacía, la tabla no está vacía
        return True
    
    def get_size(self):
        # Método para obtener el número de elementos en la tabla hash
        count = 0
        for i in range(self.size):
            # Recorremos cada posición de la tabla
            if self.table[i] is not None:
                # Si la posición no está vacía, aumentamos un contador
                count += 1
        return count  # Devolver el número total de elementos
        
    def hashfunction(self, key):
        # Método para calcular el índice a partir de la clave
        if isinstance(key, int):
            # Si la clave es un entero, usamos el módulo del tamaño de la tabla
            return key % self.size
        elif isinstance(key, str):
            # Si la clave es una cadena, sumamos los valores ASCII
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
            
    def add(self, key, value):
        # Método para agregar una clave (llave) y su valor a la tabla hash
        index = self.hashfunction(key)  # Calculamos el índice usando la función hash
        self.table[index] = (key, value)  # Almacenamos el par key-value en el índice calculado
                
    def getByKey(self, key):
        # Método para obtener un valor a partir de la clave
        index = self.hashfunction(key)
        if self.table[index] is not None:
            # Si en ese índice hay un elemento
            if self.table[index][0] == key:
                # Y la clave coincide, devolvemos el valor asociado
                return self.table[index][1]
        # Si no encontramos la clave, devolvemos None
        return None
                
    def getByValue(self, value):
        # Método para obtener una clave a partir de su valor
        for i in range(self.size):
            # Recorrer cada posición de la tabla
            if self.table[i] is not None and self.table[i][1] == value:
                # Y el valor coincide, devolvemos la clave asociada
                return self.table[i][0]
        # Si no encontramos el valor, devolvemos None
        return None

# Creamos una tabla de valor definido
hash_table = HashTable(5)

# Agregar dos claves que generan el mismo índice
hash_table.add(1, "valor1")  # hashfunction(1) % 5 -->
hash_table.add(6, "valor2")  # hashfunction(6) % 5 -->

# Obtenemos los valores de ambas claves
print(hash_table.getByKey(1))  # --> Devolver "valor1"
print(hash_table.getByKey(6))  # --> Devolver "valor2"