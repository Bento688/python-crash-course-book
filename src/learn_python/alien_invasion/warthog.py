"""Warthog class"""

import pygame

class Warthog:
    """A class representing the warthog background"""

    def __init__(self, ai_game):
        """
        Initialize a warthog persona that acts as a background character

        It should translucent and follow the background color of the game
        """

        # create the new color tuple
        bg_color = ai_game.settings.bg_color + (30,)

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the warthog image and get its rect.
        self.image = pygame.image.load('images/warthog.png')
        self.rect = self.image.get_rect()

        # manipulate position and color
        self.rect.center = self.screen_rect.center
        # self.image.fill(bg_color, special_flags=pygame.BLEND_RGBA_MIN)
        self.image.fill(bg_color, special_flags=pygame.BLEND_RGBA_MULT)

    def blitme(self):
        """Draw the warthog at its current location."""
        self.screen.blit(self.image, self.rect)


