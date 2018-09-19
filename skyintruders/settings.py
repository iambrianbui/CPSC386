"""A class that handles all of the settings for Alien Invasion."""
class Settings():

    """Initialize game settings."""
    def __init__(self):
        #  Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (115, 196, 252)

        #  Ship settings:
        self.plane_limit = 3

        #  Bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #  Alien settings
        self.fleet_drop_speed = 10

        #  How much game scaling
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.plane_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 6

        #  1 is right, -1 is left
        self.fleet_direction = 1


    def increase_speed(self):
        self.plane_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
