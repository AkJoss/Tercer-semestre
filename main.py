# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:27:02 2024

@author: josea
"""

import pygame
import sys
import random
from player import Player
from enemy import Enemy

#inicializar pygame
pygame.init()

#Definir constantes para el tamaño de la pantalla
WIDTH = 800
HEIGHT = 600

FONT = pygame.font.SysFont("Fixedsys", 40)

#Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adios AMLO")

#Establecer el reloj para controlar los FPS
clock = pygame.time.Clock()

#sistema de vidas y puntos
lifes = 5
points = 0

#tiempo entre que aparece un enemigo y otro
past_time = 0
future_time = 1000 #milisegundos

#Crear una instancia del jugador
player = Player(WIDTH//2,HEIGHT-50)

#Crear listas paraalmacenar los enemigos
enemies = []
bullets = []

#bucle principal del juego
running = True
while running and lifes > 0:
    #controlar los FPS
    delta_time = clock.tick(60) #limitar a 60 FPS
    past_time += delta_time
    
    #generar nuevos enemigos cada cierto tiempo
    if past_time > future_time: 
        enemies.append(Enemy(random.randint(0, WIDTH - 50), 100))
        past_time = 0
    
    #actualizamos las balas
    bullets_to_remove = [] #lista de balas a eliminar
    for bullet in bullets:
        bullet.update()
        #eliminamos las balas que salen de la pantalla
        if bullet.rect.bottom < 0:
            bullets_to_remove.append(bullet)
    
    #actualizar enemigos
    enemies_to_remove = []
    for enemy in enemies:
        enemy.update(delta_time)
        #verifiar colisiones entre el jugador y los enemigos
        if enemy.rect.colliderect(player.rect) and not enemy.is_exploding:
            lifes -= 1
            enemy.is_exploding = True
            enemy.image = enemy.explosion_image
            enemy.explosion_time = 0
        #eliminar enemigos que salen de la pantalla
        elif enemy.rect.top > HEIGHT and not enemy.is_exploding:
            enemies_to_remove.append(enemy)
        #eliminar enemigos despues de que la explosion hay terminado
        elif enemy.is_exploding and enemy.explosion_time >= enemy.explosion_duration:
            enemies_to_remove.append(enemy)
        
    #Verficar colisiones entre balas y enemigos
    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect) and not enemy.is_exploding:
                #reducimos la vida del enemigo
                enemy.hit()
                if enemy.is_exploding and enemy.explosion_time == 0:
                    points += 1
                if bullet not in bullets_to_remove:
                    bullets_to_remove.append(bullet)
                break
                
    #eliminar las balas marcadas
    for bullets in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)
                
    #eliminar los enemigos marcados
    for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)
    #dibujar el fondo
    screen.fill(((0,0,0)))
    
    #dibujar las balas
    for bullet in bullets:
        bullet.draw(screen)
        
    #dibujr los enemigos
    for enemy in enemies:
        enemy.draw(screen)
        
    #dibujar al jugador
    player.draw(screen)
    
    #texto de las vidas y puntos
    life_text = FONT.render(f"Vida: {lifes}", True,"white")
    points_text = FONT.render(f"Puntos: {points}", True, "white")
    
    #dibujar el texto de vidas y puntos
    screen.blit(life_text, (20,20))
    screen.blit(points_text, (20,60))
    
    #actualizar la pantalla
    pygame.display.update()
"""
    #manejar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #obtener las teclas presionadas
    keys = pygame.key.get_pressed()
    
    #actualizar la posicion del jugador
    player.update(keys, WIDTH, HEIGHT)
    
    #verificar si el jugador dispara
    if keys[pygame.K_SPACE]:
        bullet = player.shoot()
        if bullet:
            bullets.append(bullet)
    
    #actualizary dibujar las balas
    for bullet in bullets[:]:#iterar sobre una copia de la lista
        bullet.update()
        bullet.draw(screen)
    
    #verificar las colisiones entre las balas y los enemigos
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                points += 1
                break
        #eliminamos las balas que salen dela pantalla
        if bullet.rect.bottom > 0:
            bullets.remove(bullet)
    
    #Actualizar y dibujar los enemigos
    for enemy in enemies[:]:
        enemy.update()
        enemy.draw(screen)
        
        #Verificar colisiones entre el jugador y los enemigos
        if enemy.rect.colliderect(player.rect):
            lifes -= 1
            enemies.remove(enemy)
            
        #eliminar enemigos que salen de la pantalla y sumar puntos
        elif enemy.rect.top > HEIGHT:
            enemies.remove(enemy)
            points += 1
        
        
    #dibujar el fondo
    screen.fill((255,255,255))
    
    #dibujar al jugador
    player.draw(screen)
    
"""
#salir de pygame
pygame.quit
sys.exit()
    
    
        
    