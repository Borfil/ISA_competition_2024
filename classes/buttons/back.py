import pygame as pg

from classes.button import Button

class BackButton(Button):
    image: pg.Surface   = pg.image.load("images/back_button.png")
    active: bool        = False

    def click_event(self, args: dict[str]):
        self.button_arranging()