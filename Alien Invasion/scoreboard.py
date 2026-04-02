import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen                           # Reference to game screen
        self.screen_rect = screen.get_rect()           # Screen rectangle for positioning
        self.ai_settings = ai_settings                 # Access to settings
        self.stats = stats                             # Access to game statistics

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)                 # Dark gray text
        self.font = pygame.font.SysFont(None, 48)      # Default system font, size 48

        # Prepare the initial score images (so they are ready when game starts).
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))           # Round score to nearest 10
        score_str = "{:,}".format(rounded_score)                   # Format with commas (e.g., 1,000)
        self.score_image = self.font.render(                       # Render text to an image
            score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()              # Get rectangle of the image
        self.score_rect.right = self.screen_rect.right - 20        # Place near right edge
        self.score_rect.top = 20                                   # Offset from top

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))         # Round high score
        high_score_str = "{:,}".format(high_score)                 # Format with commas
        self.high_score_image = self.font.render(                  # Render text
            high_score_str, True, self.text_color, self.ai_settings.bg_color
        )

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx    # Center horizontally
        self.high_score_rect.top = self.score_rect.top             # Align with score's top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(                       # Render level as text
            str(self.stats.level), True, self.text_color, self.ai_settings.bg_color
        )

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right              # Align to right of score
        self.level_rect.top = self.score_rect.bottom + 10          # Place just below score

    def prep_ships(self):
        """Show how many ships are left (lives)."""
        self.ships = Group()                                       # Create a group of ships
        for ship_number in range(self.stats.ships_left):           # Loop over remaining lives
            ship = Ship(self.ai_settings, self.screen)             # Create a new ship sprite
            ship.rect.x = 10 + ship_number * ship.rect.width       # Offset ships horizontally
            ship.rect.y = 10                                       # Place at top left
            self.ships.add(ship)                                   # Add to group

    def show_score(self):
        """Draw all scoring elements to the screen."""
        self.screen.blit(self.score_image, self.score_rect)        # Draw current score
        self.screen.blit(self.high_score_image, self.high_score_rect)  # Draw high score
        self.screen.blit(self.level_image, self.level_rect)        # Draw level number
        # Draw ships (remaining lives).
        self.ships.draw(self.screen)
