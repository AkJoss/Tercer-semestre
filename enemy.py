# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:23:38 2024

@author: josea
"""
import pygame

#definimos la clase enemi para los enemigos
class Enemy:
    def __init__(self, x, y):
        #inicializar la posicion del enemigo
        self.rect = pygame.Rect(x, y, 50 ,50)
        self.speed = 1
        self.color = "darkmagenta"
        
    #metodo para actualizar el enemigo
    def update(self):
        self.rect.y += self.speed
        
    #metodo para dibujar al enemigo en la pantalla
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
