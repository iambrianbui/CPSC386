import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, ai_settings, screen, p1paddle):
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #  Create a ball rect at (0, 0) then set correct position
        self.rect = pygame.Rect(600, 1, ai_settings.ball_width, ai_settings.ball_height)

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.ball_color
        self.speed_factor = ai_settings.ball_speed_factor


    #  Check if the ball hits the bottom or top walls
    def check_bot_top(self, ai_settings):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            ai_settings.ball_y_direction *= -1
            # wallhit = pygame.mixer.Sound('sounds\pongwall.wav')
            # wallhit.play()


    #  Move the ball
    def update(self, ai_settings):
        self.check_bot_top(ai_settings)

        self.y += (self.speed_factor * self.ai_settings.ball_y_direction)
        self.x += (self.speed_factor * self.ai_settings.ball_x_direction)
        #  Update the rect position
        self.rect.y = self.y
        self.rect.x = self.x


    #  Actually draw the ball
    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    #  Reset the ball location
    def reset_ball(self):
        self.y = 1
        self.x = 600
        self.rect.y = self.y
        self.rect.x = self.x
