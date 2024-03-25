import pygame as pg

from classes.button import Button

class PlayButton(Button):
    image: pg.Surface   = pg.image.load("images/play_button.png")
    active: bool        = True

    def click_event(self, args: dict[str]):
        self.button_arranging()


    

