import pygame as pg

from classes.virtualRect import VirtualRect



class GravyObject:
    image: pg.Surface           = None
    field: pg.Surface           = None
    rect: pg.Rect               = None
    fieldRect: pg.Rect          = None
    virtualRect: VirtualRect    = None
    fieldRadius: int            = 100
    attractionStrength: float   = 0.5

    def __init__(self, coordinates: tuple) -> None:
        self.rect = self.image.get_rect()
        self.fieldRect = self.field.get_rect()
        self.virtualRect = VirtualRect(self.rect)


        self.virtualRect.x = coordinates[0]
        self.virtualRect.y = coordinates[1]

        self.rect.x = self.virtualRect.x
        self.rect.y = self.virtualRect.y

        self.fieldRect.x = self.rect.x - (self.fieldRadius - self.rect.width/2)
        self.fieldRect.y = self.rect.y - (self.fieldRadius - self.rect.height/2)

        self.field = self.field.convert_alpha()
        

    def update(self) -> None:
       self.rect.x = self.virtualRect.x
       self.rect.y = self.virtualRect.y

       self.fieldRect.x = self.rect.x - (self.fieldRadius - self.rect.width/2)
       self.fieldRect.y = self.rect.y - (self.fieldRadius - self.rect.height/2)


    def draw_me(self, screen: pg.Surface) -> None:
        self.rect.x += 60
        self.rect.y += 240
        self.fieldRect.x += 60
        self.fieldRect.y += 240

        screen.blit(self.field, self.fieldRect)
        screen.blit(self.image, self.rect)

        self.rect.x -= 60
        self.rect.y -= 240
        self.fieldRect.x -= 60
        self.fieldRect.y -= 240


