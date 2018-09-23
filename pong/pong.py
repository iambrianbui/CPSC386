import sys

import pygame

from settings import Settings
from paddle import Paddle
import game_functions as gf


#  Init game and create a screen object
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    #  Make a paddle
    paddle = Paddle(ai_settings, screen)

    #  Start the main loop for the game.
    while True:
        #  Watch for keyboard and mouse events
        gf.check_events(paddle)
        paddle.update()
        gf.update_screen(ai_settings, screen, paddle)


run_game()
