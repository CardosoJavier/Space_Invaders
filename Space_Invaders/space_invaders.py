import pygame
import sys
import random
from alien_bullet import Alien_Bullet
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


""" Game class with all settings """
class Space_Invaders():

    def __init__(self):

        # init pygame
        pygame.init()

        # settings instance of the game
        self.settings = Settings()

        # screen creation
        pygame.display.set_caption("Space Invaders")
        self.screen = self.settings.screen
    
        """ Spaceship instance """
        self.ship = Ship(int(self.settings.width / 2), self.settings.height - 120, self.settings.ship_health)
        self.ship_group = pygame.sprite.Group()
        self.ship_group.add(self.ship)

        # Spaceship bullet group
        self.ship_bullet_group = pygame.sprite.Group()

        """ Aliens group """
        self.aliens_group = pygame.sprite.Group()
        self.create_Aliens()

        # alien bullet group
        self.alien_bullet_group = pygame.sprite.Group()
        self.bullet_cooldown = 1000 # miliseconds
        self.last_shoot = pygame.time.get_ticks()

        """ Explosion group """
        self.explosion_group = pygame.sprite.Group()

        """ Count down for 3 seconds laps """
        self.countDown = self.settings.countDown_screen
        self.last_count = pygame.time.get_ticks()

        """ Font settings """
        self.font1 = pygame.font.SysFont(None, 100)
        self.font2 = pygame.font.SysFont(None, 60)

        """ Game over controls """
        self.game_over = self.settings.game_over

        """ fps """
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.bg_image = pygame.image.load('./images/space2.jpg')
        
        
    
    """ Run game and look for events """
    # run game method
    def run_game(self):

        # loop to run game
        running = True
        while running:
            
            # fps
            # self.clock.tick(self.fps)

            # load bg image
            self.screen.blit(self.bg_image,(0,0))

            if self.countDown == 0:
                
                # player wins check
                if len(self.aliens_group) == 0:
                    self.game_over = 1

                if self.game_over == 0:
                # update elements (motion)
                    self.game_over = self.ship.update(self.explosion_group)  # checks for ship health
                    self.ship_bullet_group.update(self.aliens_group, self.explosion_group)
                    self.aliens_group.update()
                    self.alien_bullet_group.update(self.ship_group, self.ship, self.explosion_group)

                    # alien shots
                    self.shooting_alien()
                
                else:

                    # prayer dies
                    if self.game_over == -1:
                        self._draw_text("Gave Over!",(255,255,255), int(self.settings.width / 2 - 180), int(self.settings.height / 2 + 50))

                    if self.game_over == 1:
                        self._draw_text("You Won!",(255,255,255), int(self.settings.width / 2 - 180), int(self.settings.height / 2 + 50))
            
            # update explosions
            self.explosion_group.update()
            
            # load elements to screen
            self.ship_group.draw(self.screen)
            self.ship_bullet_group.draw(self.screen)
            self.aliens_group.draw(self.screen)
            self.alien_bullet_group.draw(self.screen)
            self.explosion_group.draw(self.screen)

            # check for keyword events
            self._check_events()

            if self.countDown > 0:
                self._draw_text('Get Ready!', (255,255,255), int(self.settings.width / 2 - 180), int(self.settings.height / 2 + 50))
                self._draw_text(str(self.countDown),(255,255,255), int(self.settings.width / 2 - 10), int(self.settings.height / 2 + 140))

                # decrease counter
                count_timer = pygame.time.get_ticks()

                if count_timer - self.last_count > 1000:
                    self.countDown -= 1
                    self.last_count = count_timer

            # load and update all elements
            pygame.display.flip()
            

    
    # draw text into screen
    def _draw_text(self,text, color_txt, x, y):
        
        img = self.font1.render(text, True, color_txt)
        self.screen.blit(img, (x,y))

    # get keyword and mouse events
    def _check_events(self):

        for event in pygame.event.get():

            # close game with default method
            if event.type == pygame.QUIT:
                sys.exit()
            
            # manages all pressed keys
            elif event.type == pygame.KEYDOWN:
                self._keyDown(event)
            
            # manages all released keys
            elif event.type == pygame.KEYUP:
                self._keyUp(event)
    

    """ manage pressed keys """
    # manage pressed keys
    def _keyDown(self, event):

        # exit game when q key is pressed
        if event.key == pygame.K_q:
            sys.exit()
        
        # move to the right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.move_right = True
        
        # move to the left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.move_left = True

        # shoot laser
        if event.key == pygame.K_SPACE:
            
            # limit number of bullets in the screen
            if len(self.ship_bullet_group) < self.settings.bullet_limit:
                
                self.settings.laser_fx.play( )
                # create and add bullet instance
                bullet = Bullet(self.ship.rect.centerx, self.ship.rect.top)
                self.ship_bullet_group.add(bullet)  


    # manages released keys
    def _keyUp(self, event):

        # stop moving to the right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.move_right = False
        
        # stop moving to the left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.move_left = False
    
    """ Alien actions """

    def create_Aliens(self):
        """ creates alien fleet """
        for row in range(self.settings.aliens_rows):
            for index in range(self.settings.aliens_cols):

                # create a new alien
                alien = Alien(400 + index * 200, 100 + row * 200)
                self.aliens_group.add(alien)
    
    def shooting_alien(self):
        """ selects an alien to shot """
        actual_time = pygame.time.get_ticks()

        if (actual_time - self.last_shoot) > self.bullet_cooldown:

            # selects a random alien
            attacking_alien = random.choice(self.aliens_group.sprites())

            # generate bullet
            alienBullet = Alien_Bullet(attacking_alien.rect.centerx, attacking_alien.rect.bottom)

            # add bullet to group
            self.alien_bullet_group.add(alienBullet)

            # restart cooldown
            self.last_shoot = actual_time
    
    def loadify(img):
        return pygame.image.load(img).convert_alpha()
        
        
        



""" Game instance """
if __name__ == '__main__':
    ai_game = Space_Invaders()
    ai_game.run_game()