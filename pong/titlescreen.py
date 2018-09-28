import pygame.ftfont


class TitleScreen:

    def __init__(self, ai_settings, screen, msg):
        #  Init button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #  Set the dimensions and properties of the button
        self.width, self.height = 250, 64
        self.title_color = (0, 100, 50)
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)

        #  Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.screen_rect.centerx, self.screen_rect.centery - 200]

        #  Difficulty text
        self.diffrect = pygame.Rect(0, 0, 128, 64)
        self.diffrect.center = [self.screen_rect.centerx, self.screen_rect.centery + 200]

        self.prep_msg(msg, "Difficulty: ")

    def prep_msg(self, msg, diff):
        #  Turn the msg into a rendered image and center the text
        self.msg_image = self.font.render(msg, True, self.white, self.title_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.diff_image = self.font.render(diff, True, self.white, self.title_color)
        self.diff_image_rect = self.diff_image.get_rect()
        self.diff_image_rect = self.diffrect.center

    def draw_title(self):
        #  Draw blank button and then draw message
        self.screen.fill(self.title_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        self.screen.fill(self.title_color, self.diffrect)
        self.screen.blit(self.diff_image, self.diff_image_rect)
