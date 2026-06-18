class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # parametres du vaisseau
        self.ship_speed = 2
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Nombres des balles acceptés
        self.bullets_allowed = 3
        self.fleet_direction = 1  # 1 = droite, -1 = gauche
        self.alien_speed=2
        self.fleet_drop_speed = 10