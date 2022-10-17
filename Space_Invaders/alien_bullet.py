from pygame.sprite import Sprite
from settings import Settings
import pygame
from ship import Ship
from explosion import Explosion


class Alien_Bullet(Sprite):
    """ Class to build the bullets used by the aliens """
    def __init__(self, x, y):

        Sprite.__init__(self)

        # settings instance
        self.settings = Settings()

        # manages bullet image
        self.image = self.settings.alien_bullet_image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    """ manege bullet graphics """
    def update(self, group = pygame.sprite.Group(), ship = Ship(0,0,0), explosion_group = pygame.sprite.Group()):

        # bullet speed
        self.rect.y += self.settings.alien_bullet_speed

        # destroy bullet
        if self.rect.top > self.settings.height:
            self.kill()

        """ Bullet collision """
        # collision detection
        if pygame.sprite.spritecollide(self, group, False, pygame.sprite.collide_mask):
            self.kill()
            
            ship.health_remaining -= 1
            self.settings.explosion_fx3.play()
            # create explosion
            explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
            explosion_group.add(explosion)
            