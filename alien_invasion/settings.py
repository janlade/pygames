# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:23:51 2022

@author: jan.lade with credits to erric.matthes
"""


class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)