import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # initialise l'horloge du jeu
        self.clock = pygame.time.Clock()
        # initialiser le parametre
        self.settings = Settings()
        # represente la surface du jeu
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
    def _check_event(self):
        # Boucle d'evenement
        # un evenement est une action de l'utilisateur
          for event in pygame.event.get():
                # liste d'evenement recent
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = False
    def _update_screen(self):
         # Redessiner l'écran pendant chaque passage au travers la boucle.
         # mettre à jour l'écran
            self.screen.fill(self.settings.bg_color)
            # Afficher le vaisseau
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()