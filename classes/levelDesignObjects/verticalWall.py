import pygame as pg

from classes.physicObject import PhysicObject

class VerticalWall(PhysicObject):
    image: pg.Surface   = pg.image.load("images/vertical_wall.png")