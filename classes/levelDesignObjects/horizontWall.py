import pygame as pg

from classes.physicObject import PhysicObject

class HorizontWall(PhysicObject):
    image: pg.Surface   = pg.image.load("images/ground_wall.png")
