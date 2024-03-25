import pygame as pg

from classes.button import Button

class ContinueEditButton(Button):
    image: pg.Surface   = pg.image.load("images/continue_play_button.png")
    active: bool        = False

    def click_event(self, args: dict[str]):
        self.button_arranging()

        args["settings"].editor_on()