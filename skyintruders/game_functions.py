import sys

import pygame
from bullet import Bullet
from alien import Alien

def create_fleet(ai_settings, screen, aliens):
    #  Create an alien and find the number of aliens that can fit
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #  Create the first row of aliens
    for alien_number in range(number_aliens_x):
        #  Create an alien and place it into the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

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
def update_screen(ai_settings, screen, plane, aliens, bullets):
    #  Redraw every frame
    screen.fill(ai_settings.bg_color)
    #  Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites ():
        bullet.draw_bullet()
    plane.blitme()
    aliens.draw(screen)

    #  Show most current frame
    pygame.display.flip()
    print(str(plane.moving_right))