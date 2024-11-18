# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:34 2024

@author: josea
"""
import pygame
from bullets import Bullet
#definir la clase Player para la nave del jugadore
class Player:
    def __init__(self, x, y):
        #inicializamos la posicion del jugador
        self.rect = pygame.Rect(x, y, 25, 25)
        self.speed = 10
        self.color = "firebrick" 
        #control de disparo
        self.shoot_delay = 250 #milisegundos
        self.last_shoot_time = pygame.time.get_ticks()
        
    #metodo de actualizacion de la posicion del jugador
    def update(self, keys, screen_width, screen_height):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -=self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
        
        #metodo para disparar
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time >= self.shoot_delay:
            self.last_shoot_time = now
            return Bullet(self.rect.centerx, self.rect.top)
            
    #metodo para dibujar la nave en la pantalla
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
