import pygame as pg

from classes.physicObject import PhysicObject

class DeadBlock(PhysicObject):
    image: pg.Surface   = pg.image.load("images/dead_wall.png")