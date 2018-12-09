# -*- coding: utf-8 -*-
"""
.....
"""
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and create screen object
    pygame.init()
    invaders_settings = Settings()
    
    screen = pygame.display.set_mode((invaders_settings.screen_width,invaders_settings.screen_height))
    pygame.display.set_caption("Invaders")
    
    #create a ship
    ship = Ship(screen)
    
    # start the main loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(invaders_settings, screen, ship)
        
run_game()