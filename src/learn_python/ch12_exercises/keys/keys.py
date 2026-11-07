"""A pygame instance that prints out the key that is pressed"""

import sys

import pygame
from pygame.event import Event


class Keys:

    # constructor
    def __init__(self):
        """Initialize the instance, and create resources."""

        # init the necessary resources
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Keys")

        self.font = pygame.font.Font(None, 74)

        # holder for current key
        self.key = None

    def run_loop(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self._print_key()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypressed and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keypress(event)
            if event.type == pygame.KEYUP:
                # reset
                self.key = None

    def _check_keypress(self, event: Event):
        """Emit the current key pressed to the holder."""
        if event.key == pygame.K_q:
            # exit on 'q'
            sys.exit()
        if event.unicode:
            self.key = event.unicode
        else:
            # Fallback to key name if it's a special key like Return, Space, etc.
            self.key = pygame.key.name(event.key)

    def _print_key(self):
        """Print the current pressed key"""
        self.screen.fill((30, 30, 30))

        if self.key:
            # Render the text surface
            text_surface = self.font.render(self.key, True, (255, 255, 255))
            
            # Get the rect of the text surface and set its center to the middle of the screen
            text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            
            # Draw (blit) the text onto the screen at the calculated center
            self.screen.blit(text_surface, text_rect)


if __name__ == "__main__":
    keys = Keys()
    keys.run_loop()
