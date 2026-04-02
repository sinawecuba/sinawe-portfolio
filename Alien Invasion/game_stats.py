class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        # Store a reference to the game settings.
        self.ai_settings = ai_settings
        
        # Initialize stats that can change during gameplay.
        self.reset_stats()

        # Start the game in an inactive state, waiting for the player
        # to press "Play".
        self.game_active = False

        # High score should never reset during the game session.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Reset the number of ships available to the player.
        self.ships_left = self.ai_settings.ship_limit

        # Reset the player's score to zero.
        self.score = 0

        # Reset the game level to 1.
        self.level = 1
