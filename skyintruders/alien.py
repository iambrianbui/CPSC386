import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('image/alien.png')
        self.rect = self.image.get_rect()

        #  Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #  Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)