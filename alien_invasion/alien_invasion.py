# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:04:34 2022

@author: jan.lade with credits to erric.matthes
"""


import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """Start the main loop for the game."""
        RUNNING = True
        while RUNNING:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                    
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # Make the mot recently drawn screen visible.
            pygame.display.flip() 
            
        pygame.quit()       
            
        
if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()