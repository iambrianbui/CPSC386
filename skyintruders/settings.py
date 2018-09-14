"""A class that handles all of the settings for Alien Invasion."""
class Settings():

    """Initialize game settings."""
    def __init__(self):
        #  Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (115, 196, 252)

        #  Ship settings:
        self.plane_speed_factor = 3

        #  Bullet settings:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60