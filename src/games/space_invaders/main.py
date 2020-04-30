import pygame
from sys import exit
from src.games.space_invaders.settings import Settings
from src.games.space_invaders.models.invaders.invaders import (
    Invader,
    InvaderType,
    Fleet,
)
from enum import Enum, auto
from threading import Timer
import logging


class GameState:
    inactive = auto()
    active = auto()


class SpaceInvaders:
    def __init__(self):

        self._state = GameState.inactive
        pygame.init()
        self._settings = Settings()
        self._screen = self._configure_screen()
        self.fleets = [
            Fleet(9, InvaderType.invaderA, (40, 40), 20),
            Fleet(9, InvaderType.invaderB, (40, 100), 20),
            Fleet(9, InvaderType.invaderC, (40, 160), 20),
        ]

    def _configure_screen(self):
        logging.info("Configuring screen with settings: %s", self._settings)
        screen = pygame.display.set_mode(self._settings.resolution)
        pygame.display.set_caption(self._settings.title)
        icon = pygame.image.load(self._settings.icon)
        pygame.display.set_icon(icon)

        return screen

    def run(self):
        logging.info("Commencing runtime")
        while True:
            self._event_handler()
            self._update_screen()

    #  Need to have an event registry, and event classes
    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Handling request for graceful exit")
                self.timer.cancel()
                exit()
            if event.type == pygame.KEYDOWN:
                if self._state == GameState.inactive:
                    if event.key == pygame.K_RETURN:
                        self._draw_fleets()
                        self.timer = Timer(1, self._move_fleet)
                        self.timer.start()
                        self._state = GameState.active
                elif self._state == GameState.active:
                    logging.warn("Not implemented")

    def _update_screen(self):
        pygame.display.update()

    def _move_fleet(self):
        logging.info("Callback to move fleet handled")
        self._screen.fill(self._settings.background)

        [x.shift_origin((20, 0)) for x in self.fleets]
        self._draw_fleets()

        self.timer = Timer(1, self._move_fleet)
        self.timer.start()

    def _draw_fleets(self):
        [x.draw(self._screen) for x in self.fleets]


if __name__ == "__main__":
    SpaceInvaders().run()
