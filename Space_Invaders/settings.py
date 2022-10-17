import pygame
import random
import pygame.font
from pygame import mixer
import pygame.font

class Settings():

    def __init__(self):
        
        """ Screen settings """
        # screen size
        self.screen = pygame.display.set_mode()
        self.width, self.height = self.screen.get_size()

        # screen background
        self.bg_image = pygame.image.load('./images/space2.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.width, self.height))

        """ Sound effects settings """
        pygame.mixer.pre_init(44100,-16,2,512)
        mixer.init()

        self.explosion_fx1 = pygame.mixer.Sound('./sounds/explosion_fx1.wav')
        self.explosion_fx1.set_volume(0.25)

        self.explosion_fx2 = pygame.mixer.Sound('./sounds/explosion_fx2.wav')
        self.explosion_fx2.set_volume(0.25)

        self.explosion_fx3 = pygame.mixer.Sound('./sounds/explosion_fx3.wav')
        self.explosion_fx3.set_volume(0.25)

        self.laser_fx = pygame.mixer.Sound('./sounds/laser_fx.wav')
        self.laser_fx.set_volume(0.25)

        """ Spaceship settings """
        self.ship_image = pygame.image.load('./images/ship1.bmp')  # ship image
        self.ship_speed = 2 # speed of the ship in pixels
        self.ship_health = 3

        # Space ship bullet settings
        self.ship_bullet = pygame.image.load('./images/ship_bullet1.bmp') # bullet image
        self.bullet_speed = 3
        self.bullet_limit = 5

        """ Alien settings """
        self.alien_image = pygame.image.load('./images/alien' + str(random.randint(1,3)) + '.bmp')
        self.aliens_rows = 2
        self.aliens_cols = 5

        # alien bullet settings
        self.alien_bullet_image = pygame.image.load('./images/alien_bullet1.bmp')
        self.alien_bullet_speed = 2

        """ Explosion settings """
        self.explosion_speed = 20
        self.countDown_screen = 3

        """ Game over controls """
        # 0 = game runs, 1 = player won, -1 = player lost
        self.game_over = 0