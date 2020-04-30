from enum import Enum
import pygame


class InvaderType(Enum):
    invaderA = (255, 0, 0)
    invaderB = (0, 255, 0)
    invaderC = (0, 0, 255)


class Invader:
    def __init__(self, kind: InvaderType, resolution, origin):
        position = origin + resolution
        self.type = kind
        self.object = pygame.rect.Rect(position)

    def draw(self, screen):
        self.object = pygame.draw.rect(screen, self.type.value, self.object)

    def move(self, origin):
        self.object.move_ip(origin[0], origin[1])


class Fleet:
    def __init__(self, number: int, kind: InvaderType, origin, offset):
        self.origin = origin
        resolution = (30, 30)
        offset = (offset + resolution[0], 0)
        self.fleet = []
        for i in range(number):
            offset_origin = (
                self.origin[0] + i * offset[0],
                self.origin[1] + i * offset[1],
            )
            self.fleet.append(Invader(kind, resolution, offset_origin))

    def draw(self, screen):
        for i in range(len(self.fleet)):
            self.fleet[i].draw(screen)

    def shift_origin(self, x):
        for i in range(len(self.fleet)):
            self.fleet[i].move((x[0], x[1]))
