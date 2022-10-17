import pygame
from pygame.sprite import Sprite
from settings import Settings

class Explosion(Sprite):
    """ Class to build the bullets used by the aliens """
    def __init__(self, x, y, size):

        Sprite.__init__(self)

        # settings instance
        self.settings = Settings()

        """ Load images """
        self.images = []
        for index in range(1,4):
            img = pygame.image.load(f"./images/explosion{index}.bmp")

            if size == 1:
                img = pygame.transform.scale(img, (60,60))

            if size == 2:
                img =pygame.transform.scale(img, (90,90))

            if size == 3:
                img =pygame.transform.scale(img, (150,150))

            self.images.append(img)


            # manages bullet image
            self.index = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.counter = 0

    """ manege bullet graphics """
    def update(self):

        # update explosion animation
        self.counter += 1

        if self.counter >= self.settings.explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        
        # delete explosion from screen
        if self.index >= len(self.images)-1 and self.counter >= self.settings.explosion_speed:
            self.kill()
            