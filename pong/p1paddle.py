import pygame


class P1Paddle():

    def __init__(self, ai_settings, screen):
        super(P1Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #  Load the paddle image and get its rect
        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 64

        self.center = float(self.rect.centery)

        #  Movement flag
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.paddle_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.paddle_speed_factor

        self.rect.centery = self.center
