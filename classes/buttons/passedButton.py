import pygame as pg

from classes.button import Button

class PassedButton(Button):
    image: pg.Surface   = pg.image.load("images/passed_button.png")
    active: bool        = False

    def click_event(self, args: dict[str]):
        self.button_arranging()

        args["objectManager"].reset_active_lists()
        args["settings"].reset_rotate_angle()
        args["settings"].background_on()