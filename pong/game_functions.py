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


def update_screen(ai_settings, screen, paddle, ball):
    screen.fill(ai_settings.bg_color)
    paddle.blitme()
    ball.draw_ball()

    #  Make the most recently drawn screen visible
    pygame.display.flip()

def update_ball(ai_settings, paddle, ball):
    check_collision(paddle, ball, ai_settings)
    ball.update(ai_settings)

def check_collision(paddle, ball, ai_settings):
    if ball.rect.colliderect(paddle.rect):
        ai_settings.ball_x_direction *= -1