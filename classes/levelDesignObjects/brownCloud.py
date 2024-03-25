import pygame as pg

from classes.cloudObject import CloudObject


class BrownCloud(CloudObject):
    image: pg.Surface   = pg.image.load("images/brown_cloud.png")
    effect: float       = 0.5
