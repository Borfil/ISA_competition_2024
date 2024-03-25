import pygame as pg

from classes.cloudObject import CloudObject


class PurpleCloud(CloudObject):
    image: pg.Surface   = pg.image.load("images/purple_cloud.png")
    effect: float       = -1
