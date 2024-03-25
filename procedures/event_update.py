import pygame as pg

from classes.objectManager import ObjectManager
from classes.blockManager import BlockManager
from classes.physicObject import PhysicObject
from classes.settings import Settings
from classes.player import Player

from functions.distance_checking import distance_checking


def event_update(
        objectManager: ObjectManager, 
        blockManager: BlockManager,
        settings: Settings
        ) -> None:
    
    objectEventList: list[PhysicObject] = objectManager.objectEventList
    objectCollideList: list[PhysicObject] = objectManager.objectCollideList

    for obj in objectManager.buttons:
        obj.update()

    if objectManager.objectActiveRenderingList:
        (objectManager.objectActiveRenderingList[0].rect)

    


    if settings.get_active_state():

        if objectManager.player.passed:
            settings.stop()
            objectManager.passedButton.on()

        for obj in objectManager.objectFieldList:
            if distance_checking(objectManager.player.virtualRect, obj.virtualRect, obj.fieldRadius):
                objectManager.player.addition_force_impact(obj.virtualRect, obj.attractionStrength)

        for obj in objectManager.objectCloudList:
            obj.collide_event(objectManager.player)

        

        for obj in objectEventList:
            if obj.__class__ == Player:
                obj.update(objectCollideList)
            else:
                obj.update()

            