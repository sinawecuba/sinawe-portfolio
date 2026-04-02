import pygame                        # Import pygame library for game development
from pygame.sprite import Group      # Import Group to manage collections of sprites (aliens, bullets)

from settings import Settings        # Import game settings (screen size, colors, speeds, etc.)
from game_stats import GameStats     # Import class that tracks game stats (score, lives, etc.)
from scoreboard import Scoreboard    # Import class that displays score and other stats
from button import Button            # Import class for the Play button
from ship import Ship                # Import class for the player’s ship
import game_functions as gf          # Import helper functions for handling events, updates, etc.


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()                                                       # Initialize pygame modules
    ai_settings = Settings()                                            # Create settings instance
    screen = pygame.display.set_mode(                                   # Create the main display window
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")                        # Set the game window title

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")                   # Create a Play button on screen

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)                                      # Create stats tracker (lives, score, etc.)
    sb = Scoreboard(ai_settings, screen, stats)                         # Create scoreboard to display stats

    # Set the background color.
    bg_color = (230, 230, 230)                                          # Define light gray background color

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)                                    # Create the player's ship
    bullets = Group()                                                   # Create an empty group to hold bullets
    aliens = Group()                                                    # Create an empty group to hold aliens

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)                  # Generate a fleet of alien sprites

    # Start the main loop for the game.
    while True:                                                         # Main game loop (runs forever)
        gf.check_events(                                                # Handle input events (keyboard/mouse)
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets
        )

        if stats.game_active:                                           # Only update game objects if game is active
            ship.update()                                               # Update ship’s position
            gf.update_bullets(ai_settings, screen, stats, sb,           # Update bullet positions and check hits
                             ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,            # Update alien positions and check collisions
                            ship, aliens, bullets)

        gf.update_screen(                                               # Redraw everything on the screen
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button
        )


run_game()                                                              # Start the game
