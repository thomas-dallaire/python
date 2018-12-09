# -*- coding: utf-8 -*-
import pygame

class Ship():
    
    def __init__(self, screen):
        #initialize ship and set starting position
        self.screen = screen
        
        #load the sihp image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #update the ships position based on the movement flag
        if self.moving_right == True:
            self.rect.centerx += 1
        if self.moving_left == True:
            self.rect.centerx -= 1

        
    def blitme(self):
        #draw the ship and its cublitme
        self.screen.blit(self.image, self.rect)
            
