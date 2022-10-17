import pygame
from settings import Settings
from pygame.sprite import Sprite
from explosion import Explosion

""" Class to build spaceship object """
class Ship(Sprite):

    """ Class needs the spaceship initial position """
    def __init__(self, x, y, health):
        
        # Sprite class init
        Sprite.__init__(self)

        """ Ship settings """
        # game settings instance
        self.settings = Settings()

        # ship image, rect, and initial position
        self.image = self.settings.ship_image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        # flags to move ship
        self.move_right = False
        self.move_left = False

        """ Ship health """
        self.health_start = health
        self.health_remaining = health
    

    """ Handles ship graphics"""
    def update(self, explosion_group = pygame.sprite.Group()):

        game_over = 0

        """ Ship movements """
        # move to the right
        if self.move_right and self.rect.right < self.settings.width:
            self.rect.x += self.settings.ship_speed
        
        # move to the left
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        
        """ Ship health color """
        green = (124,252,0)
        red = (255, 0, 0)
        pygame.draw.rect(self.settings.screen, red, (self.rect.x, (self.rect.bottom+10), self.rect.width, 15))

        # Creates mask
        self.mask = pygame.mask.from_surface(self.image)

        # makes a new green rect over the red rect
        if self.health_remaining > 0:
            pygame.draw.rect(self.settings.screen, green, (self.rect.x, (self.rect.bottom+10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))

        # draw explosion
        elif self.health_remaining <= 0:
            """explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)"""
            self.settings.explosion_fx1.play()
            self.kill()

            # end game 
            game_over = -1
        return game_over