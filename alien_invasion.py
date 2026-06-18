import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        # # Passer en full screen   
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")
    def _check_event(self):
        # Boucle d'evenement
        # un evenement est une action de l'utilisateur
          for event in pygame.event.get():
                # liste d'evenement recent
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)
    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    def _update_screen(self):
         # Redessiner l'écran pendant chaque passage au travers la boucle.
         # mettre à jour l'écran
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # Afficher un alien
            self.aliens.draw(self.screen)
            # Afficher le vaisseau
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
    def _update_bullets(self):
        """
        mettre à jour la position des balles au fur et à mesure de l'éxecution du code
        """
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def run_game(self):
        """
        Start the main loop for the game.
        """
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self.update_aliens()
            self._update_screen()
            self.clock.tick(60)
    def _fire_bullet(self):
        """
        Cree une nouvelle balle et l'ajoute dans le groupe des balles
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _create_fleet(self):
        """Creer une flotte d'alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height
        cols = (screen_width - 2 * alien_width) // (2*alien_width)
        rows = (screen_height - 2 * alien_height - 2*self.ship.rect.height) // (alien_height)
        for row in range(rows):
            for col in range(cols):
                x = alien_width + col * 2 * alien_width
                y = alien_height + row * alien_height
                self._create_alien(x, y)
    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)
    def update_aliens(self):
        """cette methode met à jour les aliens à chaque passage à travers la boucle"""
        self.aliens.update()
        self._check_fleet_edges()
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()