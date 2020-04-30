from src.games.common.asset_loader.sprite_sheet import SpriteSheet
from typing import Tuple
import pygame


class SpriteSheetImpl(SpriteSheet):
    def __init__(self: 'SpriteSheet', file_name: str) -> None:
        super().__init__()
        self.file_name = file_name
        self.sprite_sheet = pygame.image.load(self.file_name).convert()

    def get_strip_n(self: 'SpriteSheet', position: Tuple[int, int, int, int], resolution: Tuple[int, int]):
        tmp_resolution = ((position[2] - position[0]), (position[3] - position[1]))
        image = pygame.Surface(tmp_resolution).convert()
        image.blit(self.sprite_sheet, (0, 0), position)
        image.set_colorkey((0, 0, 0))
        return pygame.transform.scale(image, resolution)
