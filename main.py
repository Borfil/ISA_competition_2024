import pygame as pg
import os 

from classes.player import Player
from classes.settings import Settings
from classes.objectManager import ObjectManager
from classes.blockManager import BlockManager
from classes.keyManager import KeyManager

from classes.levelDesignObjects.block import Block

from functions.buttons_create import buttons_create
from procedures.screen_update import screen_update
from procedures.event_update import event_update
from procedures.key_board_events import key_board_events

clock = pg.time.Clock()

screen = pg.display.set_mode((1080, 720))

settings = Settings((1080, 720))
keyManager = KeyManager()


blockManager = BlockManager()
objectManager = ObjectManager()

buttons = buttons_create(settings, blockManager, objectManager)

objectManager.add_buttons(buttons, settings)


mainImage = pg.transform.scale(pg.image.load("images/play_background.png"), settings.get_surface_size())
menuImage = pg.transform.scale(pg.image.load("images/main_menu_background.png"), settings.get_screen_size())
emptyImage = pg.transform.scale(pg.image.load("images/empty_background.png").convert_alpha(), settings.get_screen_size())
mainSurface = mainImage.copy()
menuSurface = menuImage.copy()


while True:
    clock.tick(90)
    key_board_events(objectManager, blockManager, keyManager, settings)
    event_update(objectManager, blockManager, settings)
    screen_update(objectManager, settings, screen, mainSurface, menuSurface, mainImage, menuImage, emptyImage)
    


