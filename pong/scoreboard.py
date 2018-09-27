import pygame.font
from pygame.sprite import Group

class Scoreboard():


    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #  Font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #  Prepare the HUD
        self.prep_score()


    def prep_score(self):
        p1score = int(round(self.stats.p1score, -1))
        p2score = int(round(self.stats.p2score, -1))
        score_str = str(self.stats.p1score)

        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #  Display the score at the top center
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        self.score_rect.center = self.screen_rect.center


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)