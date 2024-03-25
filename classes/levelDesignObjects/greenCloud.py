import pygame as pg

from classes.cloudObject import CloudObject


class GreenCloud(CloudObject):
    image: pg.Surface   = pg.image.load("images/green_cloud.png")
    effect: float       = 2
