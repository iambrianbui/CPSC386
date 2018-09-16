import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from plane import Plane
import game_functions as gf

def run_game():
    #  Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Sky Intruders")

    #  Make a ship
    plane = Plane(ai_settings, screen)
    #  Make a group to store bullets in
    bullets = Group()

    #  Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, plane, bullets)
        plane.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, plane, bullets)

        #  What for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #  Redraw the screen during each pass through the loop/
        screen.fill(ai_settings.bg_color)
        plane.blitme()

        #  Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()