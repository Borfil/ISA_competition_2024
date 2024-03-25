import pygame as pg

from classes.virtualRect import VirtualRect

class PhysicObject:
    image: pg.Surface           = None
    rect: pg.Rect               = None
    virtualRect: VirtualRect    = None

    def __init__(self, coordinates: tuple) -> None:
        self.rect = self.image.get_rect()
        self.virtualRect = VirtualRect(self.rect)

        self.virtualRect.x = coordinates[0]
        self.virtualRect.y = coordinates[1]
        self.rect.x = self.virtualRect.x
        self.rect.y = self.virtualRect.y

    def update(self) -> None:
       self.rect.x = self.virtualRect.x
       self.rect.y = self.virtualRect.y


    def draw_me(self, screen: pg.Surface) -> None:
        self.rect.x += 60
        self.rect.y += 240
        screen.blit(self.image, self.rect)
        self.rect.x -= 60
        self.rect.y -= 240