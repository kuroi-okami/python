import pygame
from sys import exit
from src.games.space_invaders.settings import Settings


class SpaceInvaders:

    def __init__(self):
        pygame.init()
        self._settings = Settings()
        self._screen = self._configure_screen()

    def _configure_screen(self):
        screen = pygame.display.set_mode(self._settings.resolution)
        pygame.display.set_caption(self._settings.title)
        icon = pygame.image.load(self._settings.icon)
        pygame.display.set_icon(icon)

        return screen

    def run(self):
        while True:
            self._event_handler()
            self._update_screen()

    #  Need to have an event registry, and event classes
    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def _update_screen(self):
        self._screen.fill(self._settings.background)
        # TODO: Could just set this on a callback timer
        pygame.display.update()


if __name__ == '__main__':
    SpaceInvaders().run()
