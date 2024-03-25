import pygame as pg

from classes.cloudObject import CloudObject


class GreyCloud(CloudObject):
    image: pg.Surface   = pg.image.load("images/grey_cloud.png")
    effect: float       = 0
