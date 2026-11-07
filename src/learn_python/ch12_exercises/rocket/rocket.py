"""Rocket class"""

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from learn_python.ch12_exercises.rocket.rocket_game import RocketGame


class Rocket:
    """A class to manage a Rocket instance"""

    def __init__(self, rocket_game: "RocketGame"):
        """Initialize the rocket and its required resources"""

        self.screen = rocket_game.screen
        self.settings = rocket_game.settings

        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()

        # align the center of the rocket to the screen's center
        self.rect.center = self.screen_rect.center

        # variables for the position of the rocket
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the position of the rocket based on the movement flag and positions."""
        # using the flags, update the position
        speed = self.settings.rocket_speed
        if self.moving_right:
            value = self.x + speed
            if self._check_new_values("h", value):
                self.x = value
        if self.moving_left:
            value = self.x - speed
            if self._check_new_values("h", value):
                self.x = value
        if self.moving_up:
            value = self.y - speed
            if self._check_new_values("v", value):
                self.y = value
        if self.moving_down:
            value = self.y + speed
            if self._check_new_values("v", value):
                self.y = value

        # don't mind the error they will just be ignored
        self.rect.x = self.x
        self.rect.y = self.y

    def _check_new_values(self, orientation, value):
        """Check if the new values are going to be within the scope"""

        right = self.screen_rect.right
        left = self.screen_rect.left
        top = self.screen_rect.top
        bottom = self.screen_rect.bottom

        if orientation == "h":
            return value >= left and value + self.rect.width <= right

        elif orientation == "v":
            return value >= top and value + self.rect.height <= bottom

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
