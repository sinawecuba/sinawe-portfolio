import pygame                              # Import pygame for game functionality
from pygame.sprite import Sprite           # Import Sprite class (base for bullet objects)


class Bullet(Sprite):                      # Define Bullet class, inherits from Sprite
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()                 # Initialize parent Sprite class
        self.screen = screen                           # Store reference to screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(                       # Create a rectangle for the bullet
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx          # Align bullet horizontally with ship’s center
        self.rect.top = ship.rect.top                  # Start bullet from the ship’s top edge

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)                    # Use float for smooth vertical movement

        self.color = ai_settings.bullet_color          # Set bullet color from settings
        self.speed_factor = ai_settings.bullet_speed_factor  # Set bullet speed from settings

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor                    # Move bullet upward by reducing y-value
        # Update the rect position.
        self.rect.y = self.y                           # Sync rect position with decimal value

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)  # Render bullet as a rectangle
