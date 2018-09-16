import sys

import pygame
from bullet import Bullet

def update_bullets(bullets):
    #  Get rid of bullets that aren't on the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def check_keydown_events(event, ai_settings, screen, plane, bullets):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True

    elif event.key == pygame.K_LEFT:
        plane.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, plane, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, plane, bullets):
    #  Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, plane)
        bullets.add(new_bullet)


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
            check_keydown_events(event, ai_settings, screen, plane, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, plane)


#  Update the screen
def update_screen(ai_settings, screen, plane, bullets):
    #  Redraw every frame
    screen.fill(ai_settings.bg_color)
    #  Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites ():
        bullet.draw_bullet()
    plane.blitme()

    #  Show most current frame
    pygame.display.flip()
    print(str(plane.moving_right))