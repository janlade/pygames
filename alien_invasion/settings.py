# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:23:51 2022

@author: jan.lade with credits to erric.matthes
"""
from pygame import mixer
import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load("images/background1.png")

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 1
        
        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 0.3
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # Background Sound
        mixer.music.load("background.wav")
        mixer.music.play(-1)