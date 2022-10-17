import pygame
from settings import Settings
from pygame.sprite import Sprite
from explosion import Explosion 

class Bullet(Sprite):
    """ Class to build bullets """
    
    def __init__(self, x, y):

        Sprite.__init__(self)

        # settings instance
        self.settings = Settings()

        # manages bullet image
        self.image = self.settings.ship_bullet
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    """ manege bullet graphics """
    def update(self, alien_group = pygame.sprite.Group(), explosion_group = pygame.sprite.Group()):

        # bullet speed
        self.rect.y -= self.settings.bullet_speed

        # destroy bullet
        if self.rect.bottom < 0:
            self.kill()
        
        # collision detection
        if pygame.sprite.spritecollide(self, alien_group, True, pygame.sprite.collide_mask):
            self.kill()
            self.settings.explosion_fx2.play()
            # create explosion
            explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            explosion_group.add(explosion)