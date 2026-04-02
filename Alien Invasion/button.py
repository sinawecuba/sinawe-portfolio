import pygame.font                             # Import pygame's font module for text rendering


class Button:
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen                    # Store reference to game screen
        self.screen_rect = screen.get_rect()    # Get screen rectangle for positioning

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50       # Button width and height
        self.button_color = (0, 255, 0)         # Button background color (green)
        self.text_color = (255, 255, 255)       # Text color (white)
        self.font = pygame.font.SysFont(None, 48)  # Use default font, size 48

        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # Create rectangular button
        self.rect.center = self.screen_rect.center              # Center button on screen

        # The button message only needs to be prepped once.
        self.prep_msg(msg)                       # Prepare the button’s text image

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        # Render the text (msg) as an image with given font, colors
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()   # Get rect for text image
        self.msg_image_rect.center = self.rect.center     # Center text on button

    def draw_button(self):
        # Draw blank button, then draw message.
        self.screen.fill(self.button_color, self.rect)          # Draw button rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect)   # Draw text image on top
