import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from p1paddle import P1Paddle
from p2paddle import P2Paddle
from ball import Ball
import game_functions as gf


#  Init game and create a screen object
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Pong")

    #  Make play button
    play_button = Button(ai_settings, screen, "Play")

    #  Handle stats and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #  Make a paddle
    p1paddle = P1Paddle(ai_settings, screen)

    #  Make another one
    p2paddle = P2Paddle(ai_settings, screen)

    #  Make a ball
    ball = Ball(ai_settings, screen, p1paddle)



    #  Start the main loop for the game.
    while True:
        #  Watch for keyboard and mouse events
        gf.check_events(ai_settings, stats, sb, play_button, p1paddle, p2paddle)

        if stats.game_active:
            p1paddle.update()
            p2paddle.update()
            gf.update_ball(ai_settings, stats, sb, screen, p1paddle, p2paddle, ball)

        gf.update_screen(ai_settings, screen, stats, sb, p1paddle, p2paddle, ball, play_button)


run_game()
