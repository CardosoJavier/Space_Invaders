from settings import Settings
from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """ Class to build aliens """

    def __init__(self, x, y):
        Sprite.__init__(self)
        
        # game settings instance
        self.settings = Settings()

        """ Alien image, rect, coordinates """
        self.image = self.settings.alien_image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        """ movement control variables """
        self.move_direction = 1
        
    
    def update(self):

        # Creates mask
        self.mask = pygame.mask.from_surface(self.image)
        
        """ Change alien direction """
        screen_rect = self.settings.screen.get_rect()
        self.rect.x += self.move_direction

        if self.rect.right >= screen_rect.right:
            self.move_direction *= -1

        if self.rect.left <= 0:
            self.move_direction *= -1
        
        
