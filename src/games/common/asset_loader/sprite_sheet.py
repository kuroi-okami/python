from abc import ABC, abstractmethod
from typing import Tuple


class SpriteSheet(ABC):
    def __init__(self):
        self.sprite_sheet = None

    @abstractmethod
    def get_strip_n(
        self: "SpriteSheet",
        position: Tuple[int, int, int, int],
        resolution: Tuple[int, int],
    ):
        """
            position:
                X Origin
                Y Origin
                X Offset
                Y Offset
        """
        ...
