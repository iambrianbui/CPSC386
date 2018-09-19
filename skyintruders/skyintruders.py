import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from plane import Plane
from alien import Alien
import game_functions as gf

def run_game():
    #  Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Sky Intruders")

    #  Make play button
    play_button = Button(ai_settings, screen, "Play")

    #  Create an instance to store game stats
    stats = GameStats(ai_settings)

    #  Make a ship
    plane = Plane(ai_settings, screen)
    #  Make an alien
    alien = Alien(ai_settings, screen)
    #  Make a group to store bullets in
    bullets = Group()
    #  Make a group to store aliens in
    aliens = Group()

    #  Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, plane, aliens)

    #  Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, plane, aliens, bullets)

        if stats.game_active:
            plane.update()
            gf.update_bullets(ai_settings, screen, plane, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, plane, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, plane, aliens, bullets, play_button)

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