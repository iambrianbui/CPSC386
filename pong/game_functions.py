import sys

import pygame

def check_events(paddle):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)


def check_keydown_events(event, paddle):
    if event.key == pygame.K_w:
        paddle.moving_up = True
    elif event.key == pygame.K_s:
        paddle.moving_down = True

def check_keyup_events(event, paddle):
    if event.key == pygame.K_w:
        paddle.moving_up = False
    elif event.key == pygame.K_s:
        paddle.moving_down = False


def update_screen(ai_settings, screen, paddle):
    screen.fill(ai_settings.bg_color)
    paddle.blitme()

    #  Make the most recently drawn screen visible
    pygame.display.flip()