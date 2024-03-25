import pygame as pg

from classes.button import Button

class EditorButton(Button):
    image: pg.Surface   = pg.image.load("images/editor_button.png")
    active: bool        = True

    def click_event(self, args: dict[str]):
        self.button_arranging()

        args["settings"].editor_on()
        args["settings"].background_off()
        args["blockManager"].adge_generate(args["objectManager"], args["settings"])
        
    

