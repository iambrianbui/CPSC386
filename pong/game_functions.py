import sys

import pygame

def check_events(ai_settings, stats, sb, play_button, p1paddle, p2paddle, title_screen):

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
            check_difficulty(ai_settings, title_screen, mouse_x, mouse_y)


def check_keydown_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = True
    elif event.key == pygame.K_s:
        p1paddle.moving_down = True
    elif event.key == pygame.K_a:
        p1paddle.moving_left = True
    elif event.key == pygame.K_d:
        p1paddle.moving_right = True

    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, p1paddle, p2paddle):
    if event.key == pygame.K_w:
        p1paddle.moving_up = False
    elif event.key == pygame.K_s:
        p1paddle.moving_down = False
    elif event.key == pygame.K_a:
        p1paddle.moving_left = False
    elif event.key == pygame.K_d:
        p1paddle.moving_right = False


def update_screen(ai_settings, screen, stats, sb, p1paddle, p2paddle, ball, play_button, title_screen):
    screen.fill(ai_settings.bg_color)
    if stats.game_active:
        p1paddle.blitme()
        p2paddle.blitme()
        ball.draw_ball()
        sb.show_score()

    else:
        play_button.draw_button()
        title_screen.draw_title()

    #  Make the most recently drawn screen visible
    pygame.display.flip()

def update_ball(ai_settings, stats, sb, screen, p1paddle, p2paddle, ball):
    check_collision(p1paddle, p2paddle, ball, ai_settings)
    ball.update(ai_settings)
    check_point_scored(ai_settings, stats, sb, screen, ball)


def check_collision(p1paddle, p2paddle, ball, ai_settings):
    if ball.rect.colliderect(p1paddle.rect) or  ball.rect.colliderect(p2paddle.rect):
        ai_settings.ball_x_direction *= -1
        # paddlehit = pygame.mixer.Sound('sounds\pongpaddle.wav')
        # paddlehit.play()
    if ball.rect.colliderect(p1paddle.uprect) or ball.rect.colliderect(p1paddle.downrect) or \
            ball.rect.colliderect(p2paddle.uprect) or ball.rect.colliderect(p2paddle.downrect):
        ai_settings.ball_y_direction *= -1


def check_bot_top(screen, ball):
        screen_rect = screen.get_rect()
        return ball.rect.bottom >= screen_rect.bottom or ball.rect.top <= 0


def check_point_scored(ai_settings, stats, sb, screen, ball):
    screen_rect = screen.get_rect()
    if ball.rect.right >= screen_rect.right:
        stats.p1score += 1
        reset_game(ai_settings, stats, sb, screen, ball)
    elif ball.rect.left <= screen_rect.left:
        stats.p2score += 1
        reset_game(ai_settings, stats, sb, screen, ball)
    elif check_bot_top(screen, ball):
        if ball.rect.right > screen_rect.centerx:
            stats.p1score += 1
            reset_game(ai_settings, stats, sb, screen, ball)
        elif ball.rect.left < screen_rect.centerx:
            stats.p2score += 1
            reset_game(ai_settings, stats, sb, screen, ball)


def reset_game(ai_settings, stats, sb, screen, ball):
    # point = pygame.mixer.Sound('sounds\pongpoint.wav')
    # point.play()
    sb.prep_score(ai_settings)
    ball.reset_ball()
    check_game_over(ai_settings, stats)


def check_game_over(ai_settings, stats):
    if stats.p1score >= ai_settings.score_limit or stats.p2score >= ai_settings.score_limit:
        stats.game_active = False
        pygame.mouse.set_visible(True)


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


def check_difficulty(ai_settings, title_screen, mouse_x, mouse_y):
    if title_screen.easyrect.collidepoint(mouse_x, mouse_y):
        ai_settings.ai_difficulty = 0.7
    elif title_screen.medrect.collidepoint(mouse_x, mouse_y):
        ai_settings.ai_difficulty = 0.9
    elif title_screen.hardrect.collidepoint(mouse_x, mouse_y):
        ai_settings.ai_difficulty = 1.0
