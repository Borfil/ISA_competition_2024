import pygame as pg

from classes.gravyObject import GravyObject



class BlueOrb(GravyObject):
    image: pg.Surface           = pg.image.load("images/blue_orb.png")
    field: pg.Surface           = pg.image.load("images/blue_field.png")
    attractionStrength: float   = -0.5



