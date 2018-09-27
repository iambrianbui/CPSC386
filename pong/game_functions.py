import sys

import pygame

def check_events(ai_settings, stats, sb, play_button, p1paddle, p2paddle):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, p1paddle, p2paddle)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, p1paddle, p2paddle)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, sb, play_button, mouse_x, mouse_y)


def check_keydown_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = True
    elif event.key == pygame.K_s:
        p1paddle.moving_down = True

    elif event.key == pygame.K_UP:
        p2paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        p2paddle.moving_down = True

    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = False
    elif event.key == pygame.K_s:
        p1paddle.moving_down = False

    elif event.key == pygame.K_UP:
        p2paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        p2paddle.moving_down = False


def update_screen(ai_settings, screen, stats, sb, p1paddle, p2paddle, ball, play_button):
    screen.fill(ai_settings.bg_color)
    p1paddle.blitme()
    p2paddle.blitme()
    ball.draw_ball()

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    #  Make the most recently drawn screen visible
    pygame.display.flip()

def update_ball(ai_settings, stats, sb, screen, p1paddle, p2paddle, ball):
    check_collision(p1paddle, p2paddle, ball, ai_settings)
    ball.update(ai_settings)
    check_point_scored(ai_settings, stats, sb, screen, ball)


def check_collision(p1paddle, p2paddle, ball, ai_settings):
    if ball.rect.colliderect(p1paddle.rect):
        ai_settings.ball_x_direction *= -1
    elif ball.rect.colliderect(p2paddle.rect):
        ai_settings.ball_x_direction *= -1


def check_point_scored(ai_settings, stats, sb, screen, ball):
    screen_rect = screen.get_rect()
    if ball.rect.right >= screen_rect.right:
        stats.p1score += 1
        reset_game(ai_settings, stats, sb, screen, ball)
    elif ball.rect.left <= screen_rect.left:
        stats.p2score += 1
        reset_game(ai_settings, stats, sb, screen, ball)


def reset_game(ai_settings, stats, sb, screen, ball):
    sb.prep_score(ai_settings)
    ball.reset_ball()


def check_play_button(ai_settings, stats, sb, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        #  Hide the cursor
        pygame.mouse.set_visible(False)

        #  Reset stats
        stats.reset_stats()
        stats.game_active = True

        #  Reset the scoreboard
        sb.prep_score(ai_settings)