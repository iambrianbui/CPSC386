import sys

import pygame

def check_events(p1paddle, p2paddle):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, p1paddle, p2paddle)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, p1paddle, p2paddle)


def check_keydown_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = True
    elif event.key == pygame.K_s:
        p1paddle.moving_down = True

    elif event.key == pygame.K_UP:
        p2paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        p2paddle.moving_down = True

def check_keyup_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = False
    elif event.key == pygame.K_s:
        p1paddle.moving_down = False

    elif event.key == pygame.K_UP:
        p2paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        p2paddle.moving_down = False


def update_screen(ai_settings, screen, p1paddle, p2paddle, ball):
    screen.fill(ai_settings.bg_color)
    p1paddle.blitme()
    p2paddle.blitme()
    ball.draw_ball()

    #  Make the most recently drawn screen visible
    pygame.display.flip()

def update_ball(ai_settings, p1paddle, p2paddle, ball):
    check_collision(p1paddle, p2paddle, ball, ai_settings)
    ball.update(ai_settings)

def check_collision(p1paddle, p2paddle, ball, ai_settings):
    if ball.rect.colliderect(p1paddle.rect):
        ai_settings.ball_x_direction *= -1
    elif ball.rect.colliderect(p2paddle.rect):
        ai_settings.ball_x_direction *= -1
