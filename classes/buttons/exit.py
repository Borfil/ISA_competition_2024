import pygame as pg
import sys

from classes.button import Button

class ExitButton(Button):
    image: pg.Surface   = pg.image.load("images/exit_button.png")
    active: bool        = True

    def click_event(self, args: dict[str]):
        pg.quit()
        sys.exit()
