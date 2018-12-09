# -*- coding: utf-8 -*-

import sys
import pygame

def check_events(ship):
    #respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move the ship to the right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                #move the ship to the left
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
                
def update_screen(invaders_settings, screen, ship):
    #update the images on the screen and flip to the new screen
    screen.fill(invaders_settings.bg_colour)
    ship.blitme()
                
    # make the most recently drawn screen visible
    pygame.display.flip()
    