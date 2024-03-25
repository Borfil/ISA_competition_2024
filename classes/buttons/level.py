import pygame as pg

from classes.button import Button
from classes.settings import Settings

class LevelButton(Button):
    image: pg.Surface   = pg.image.load("images/level_base.png")
    level: str          = None
    active: bool        = False

    def __init__(self, settings: Settings, rect: tuple[int], arena: str) -> None:
        super().__init__(settings, rect)

        self.image = pg.image.load(f"images/{arena}.png")
        self.originaleImage = self.image
        self.level = arena

    def click_event(self, args: dict[str]):
        self.button_arranging()

        args["blockManager"].load_arena(args["objectManager"], args["settings"], self.level)
        args["settings"].background_off()
        args["settings"].play()

        
