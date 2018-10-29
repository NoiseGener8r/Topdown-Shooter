## TODO ##



# Topdown Shooter
# By NoiseGenerator
# Licensed under GNU GPL

import pygame, random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
                
        self.image = player_image_right
        
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.new_x = 0
        self.new_y = 0
        
    def update(self):
        """ Move the player. """
        
        self.rect.x += self.new_x      
        self.rect.y += self.new_y
        
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.new_x = -6
        self.image = player_image_left  
    def go_right(self):
        """ Called when the user hits the left arrow. """
        self.new_x = -6
        self.image = player_image_right 
    def go_up(self):
        """ Called when the user hits the left arrow. """
        self.new_y = -6
        self.image = player_image_up 
    def go_down(self):
        """ Called when the user hits the left arrow. """
        self.new_y = 6
        self.image = player_image_down  
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.new_x = 0
        self.new_y = 0
