import pygame as pg

from classes.physicObject import PhysicObject
from classes.player import Player


class CloudObject(PhysicObject):
    image: pg.Surface   = None
    mask: pg.Mask       = None
    effect: float       = None

    def __init__(self, coordinates: tuple):
        super().__init__(coordinates)

        self.mask = pg.mask.from_surface(self.image)

    def collide_event(self, player: Player) -> None:
        offset_x = self.rect.x - player.rect.x
        offset_y = self.rect.y - player.rect.y

        if player.mask.overlap(self.mask, (offset_x, offset_y)):
            player.add_effect(self.effect)