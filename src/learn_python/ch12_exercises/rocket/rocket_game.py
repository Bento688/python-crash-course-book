"""
The Rocket game from exercise 12-4

The goal is to be able to control the rocket using:

Left ( ← ): H
Down ( ↓ ): J
Up ( ↑ ): K
Right ( → ): L

"""

import sys

import pygame

from learn_python.ch12_exercises.rocket.rocket import Rocket
from learn_python.ch12_exercises.rocket.settings import Settings


class RocketGame:
    """Overall class to create the Rocket game."""

    def __init__(self):
        """Initialize the game, and create initial game resources"""

        # initialize settings & rocket
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.rocket = Rocket(self)

    def run_game(self):
        """Start the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_l:
            self.rocket.moving_right = True
        if event.key == pygame.K_h:
            self.rocket.moving_left = True
        if event.key == pygame.K_k:
            self.rocket.moving_up = True
        if event.key == pygame.K_j:
            self.rocket.moving_down = True
        if event.key == pygame.K_q:
            # exit on 'q'
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_l:
            self.rocket.moving_right = False
        if event.key == pygame.K_h:
            self.rocket.moving_left = False
        if event.key == pygame.K_k:
            self.rocket.moving_up = False
        if event.key == pygame.K_j:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Constantly redraw the screen in the main loop."""

        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    game = RocketGame()
    game.run_game()
