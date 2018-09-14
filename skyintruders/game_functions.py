import sys

import pygame

def check_keydown_events(event, plane):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        plane.moving_left = True

def check_keyup_events(event, plane):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = False
    elif event.key == pygame.K_LEFT:
        plane.moving_left = False

    #  Record key strokes
def check_events(ai_settings, screen, plane, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, plane)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, plane)

#  Update the screen
def update_screen(ai_settings, screen, plane):
    #  Redraw every frame
    screen.fill(ai_settings.bg_color)
    plane.blitme()

    #  Show most current frame
    pygame.display.flip()