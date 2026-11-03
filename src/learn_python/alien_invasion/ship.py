"""Ship class"""

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from learn_python.alien_invasion.alien_invasion import AlienInvasion

class Ship:
    """A class to manage a ship"""

    def __init__(self, ai_game: "AlienInvasion"):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # make the surrounding background transparent for the ship
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        # Start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the ship based on the movement flag."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        # LSP error: "float" is not assignable to "int" [reportAttributeAccessIssue]
        # but the author said it's fine(?) I have no fucking clue why we do it this way.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
