import pygame                         # Import pygame for graphics and game functionality
from pygame.sprite import Sprite      # Import Sprite class (base class for all game objects)


class Alien(Sprite):                  # Define Alien class, inherits from Sprite
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()                       # Initialize parent Sprite class
        self.screen = screen                                # Store reference to game screen
        self.ai_settings = ai_settings                      # Store reference to settings

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load("images/alien.bmp")  # Load alien image from file
        self.rect = self.image.get_rect()                   # Get rectangle (size & position) of the image

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width                       # Set initial x position (one alien-width from left)
        self.rect.y = self.rect.height                      # Set initial y position (one alien-height from top)

        # Store the alien's exact position.
        self.x = float(self.rect.x)                         # Store precise horizontal position as float

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()                # Get screen boundaries
        if self.rect.right >= screen_rect.right:            # If alien touches right edge
            return True
        elif self.rect.left <= 0:                           # If alien touches left edge
            return True

    def update(self):
        """Move the alien right or left."""
        # Move alien horizontally depending on fleet direction
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x                                # Update rectangle x-position

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)             # Draw alien image at its rect position
