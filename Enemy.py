# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:23:38 2024

@author: josea
"""
import pygame
import random

class Enemy:
    def __init__(self):
        self.x = random.randint(0,750)
        self.y = random.randint(-100,-40)
        self.width = 50
        self.heigth = 40
        self.color = (142, 36, 170)
        self.velocity = random.randint(1, 5)
        self.health = 3
        
    def move(self):
        self.y += self.velocity
        if self.y > 600: #si el enemigo cruza el limite inferior de la pantalla se regresa
            self.y = random.randint (1, 3)
            self.x = random.randint(0, 750)
            
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))
        
    def collides_with(self, bullet):
        #comprueba si la bala esta dentro del ancho y alto del enemigo
        return(
                self.x < bullet.x < self.x + self.width and
                self.y < bullet.y < self.y + self.heigth
            )
        