# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:30:43 2024

@author: josea
"""
class Cristian:
    #Inicializar un nuevo nodo con un valor especifico
    #Parametros: v: Cualquier valor a almacenar en el nodo
    
    #referencia al hijo izquierdo del nodo
    def _init_(self, v):
        self.homo = None #referencia al hijo izquierdo del nodo
        self.hetero = None #referencia al hijo derecho del nodo
        self.data = v #dato o valor almacenado en el nodo 
        
def  Inorder(taro):
        """
        Realiza el recorrido inorden del arbol binario 
        Imprime los nodos en el orden: I - R - D
        Parametros:
            taro: Nodo raiz del arbol o subarbol a recorrer
            """
        if taro: #si el nodo actual no es nilo recorrer subarbol izquierdo
            Inorder(taro.homo)
            
            #visitar el nodo raiz
            print(taro.data, end = " ")
            
            #recorrer el subarbol a la derecha
            Inorder(taro.hetero)

def  Preorder(taro):
        """
        Realiza el recorrido preorden del arbol binario 
        Imprime los nodos en el orden: R - I - D
        Parametros:
            taro: Nodo raiz del arbol o subarbol a recorrer
            """
        if taro: 
          
            #visitar el nodo raiz
            print(taro.data, end = " ") 
            
        #si el nodo actual no es nilo recorrer subarbol izquierdo
            Preorder(taro.homo)
           
            #recorrer el subarbol a la derecha
            Preorder(taro.hetero)
            
           
            
def  Posorder(taro):
        """
        Realiza el recorrido postorden del arbol binario 
        Imprime los nodos en el orden: I - D - R
        Parametros:
            taro: Nodo raiz del arbol o subarbol a recorrer
            """
        if taro: #si el nodo actual no es nilo recorrer subarbol izquierdo
            Posorder(taro.homo)
           
            #recorrer el subarbol a la derecha
            Posorder(taro.hetero)
            
             
            #visitar el nodo raiz
            print(taro.data, end = " ")
            
            
#funcion principa; que se ejecuta al correr el scrip
if __name__ == "_main_" :
            
    #construccion manual del arbol binario
    groot = Cristian(12) #nodo raiz del arbol
    
    #construccion del subarborl izquierdo
    groot.homo = Cristian(7) #nodo izquiedo de la raiz 12
    groot.homo.homo = Cristian(4) #nodo izquirdo de la raiz 7
    groot.homo.homo.homo = Cristian(2) #nodo izquiedo de la raiz 4
    #subarbol izquierdo nodos derechos e izquierdos del derecho
    groot.homo.hetero = Cristian(9) #nodo derecho de la raiz 7
    groot.homo.hetero.homo = Cristian(8) #nodo izquierdo de la raiz 9
    groot.homo.hetero.hetero = Cristian(11) #nodo derecho de la raiz 9
    
    #construccion del subarbol derecho
    groot.hetero = Cristian(21) #Nodo derecho de la raiz 12
    groot.hetero.homo = Cristian(16) #nodo izquierdo de la raiz 21
    groot.hetero.homo.hetero = Cristian (19) #nodo derecho de la raiz 16
    groot.hetero.hetero = Cristian(25) #nodo derecho de la raiz 21
    
    #llamada a las funciones de recorrido
    print("recorrido en inorder:", end = " ")
    Inorder(groot)
    print("recorrido en preorder:", end = " ")
    Preorder(groot)
    print("recorrido en posorder:", end = " ")
    Posorder(groot)