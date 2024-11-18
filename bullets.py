# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:55:52 2024

@author: josea
"""

import pygame

#definir la clase Bullet para las balas
class Bullet:
    def __init__(self, x, y):
        #inicalizar la posicion de las balas
        self.rect = pygame.Rect(x-5, y-10, 10, 20)
        self.speed = 10
        self.color = "red"
        
    #metodo para actualizar la bala
    def update(self):
        self.rect.y -= self.speed
        
    #metodo para dibujar la bala en la pantalla
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
