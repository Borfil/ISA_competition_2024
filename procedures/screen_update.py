import pygame as pg

from classes.settings import Settings
from classes.objectManager import ObjectManager

def screen_update(
        objectManager: ObjectManager, 
        settings: Settings, 
        screen: pg.Surface, 
        mainSurface: pg.Surface, 
        menuSurface: pg.Surface,
        mainImage: pg.Surface,
        menuImage: pg.Surface,
        emptyImage: pg.Surface
        ) -> None:

    screen.fill((0, 0, 0))
    mainSurface = mainImage.copy()
    if settings.get_background_state():
        menuSurface = menuImage.copy()
    else:
        menuSurface = emptyImage.copy()

    objectManager.render(mainSurface, menuSurface)
                    
    rotatedSurface = pg.transform.rotate(mainSurface, settings.rotateAngle)
    screen.blit(rotatedSurface, rotatedSurface.get_rect(center = mainSurface.get_rect(center = (settings.get_screen_size()[0]/2, settings.get_screen_size()[1]/2)).center))
    if not settings.get_active_state() and not settings.get_editor_state():
        screen.blit(menuSurface, (0, 0))

    pg.display.update()