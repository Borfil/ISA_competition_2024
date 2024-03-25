import pygame as pg

from classes.gravyObject import GravyObject
from classes.virtualRect import VirtualRect



class OrangeOrb(GravyObject):
    image: pg.Surface           = pg.image.load("images/orange_orb.png")
    field: pg.Surface           = pg.image.load("images/orange_field.png")
   


