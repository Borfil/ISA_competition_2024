import pygame as pg

from classes.button import Button
from classes.gravyObject import GravyObject
from classes.physicObject import PhysicObject
from classes.cloudObject import CloudObject

from classes.levelDesignObjects.block import Block
from classes.levelDesignObjects.vinBlock import VinBlock
from classes.levelDesignObjects.deadBlock import DeadBlock
from classes.levelDesignObjects.horizontWall import HorizontWall
from classes.levelDesignObjects.verticalWall import VerticalWall

from classes.levelDesignObjects.orangeOrb import OrangeOrb
from classes.levelDesignObjects.blueOrb import BlueOrb

from classes.levelDesignObjects.greenCloud import GreenCloud
from classes.levelDesignObjects.brownCloud import BrownCloud
from classes.levelDesignObjects.greyCloud import GreyCloud
from classes.levelDesignObjects.purpleCloud import PurpleCloud


from classes.player import Player
from classes.settings import Settings


class ObjectManager:
    objectActiveRenderingList: list[PhysicObject]   = []
    objectPasiveRenderingList: list[PhysicObject]   = []
    cloudRenderingList: list[CloudObject]           = []
    objectEventList: list[PhysicObject]             = []
    objectCollideList: list[PhysicObject]           = []
    objectFieldList: list[OrangeOrb]                = []
    objectCloudList: list[CloudObject]              = []
    newObjectsList: list[PhysicObject]              = []
    objectTypeDict: dict[str, PhysicObject]         = {

        "Block": Block, 
        "DeadBlock": DeadBlock,
        "HorizontWall": HorizontWall,
        "VerticalWall": VerticalWall,
        "OrangeOrb": OrangeOrb,
        "BlueOrb": BlueOrb,
        "GreenCloud": GreenCloud,
        "BrownCloud": BrownCloud,
        "PurpleCloud": PurpleCloud,
        "GreyCloud": GreyCloud,
        "VinBlock": VinBlock,

                                                        }
    buttons: dict[Button, dict[str]]                = {}
    escButtons: dict[Button, dict[str]]             = {}
    escEditButtons: dict[Button, dict[str]]             = {}
    passedButton: Button                            = None
    
    player: Player                          = None
        

    def add_buttons(self, buttons: list[list], settings: Settings) -> None:
        for butData in buttons:
            self.buttons[butData[0]] = butData[1]
            if butData[0].__class__.__name__ == "MainMenuButton" or butData[0].__class__.__name__ == "ContinuePlayButton" or butData[0].__class__.__name__ == "SettingsButton":
                self.escButtons[butData[0]] = butData[1]
            if butData[0].__class__.__name__ == "MainMenuButton" or butData[0].__class__.__name__ == "ContinueEditButton" or butData[0].__class__.__name__ == "SettingsButton":
                self.escEditButtons[butData[0]] = butData[1]
            if butData[0].__class__.__name__ == "PassedButton":
                settings.stop()
                self.passedButton = butData[0]

        for button in buttons:
            self.add_new_object_to_pasive_rendering_list(button[0])


    def render(self, mainSurface: pg.Surface, menuSurface: pg.Surface) -> None:
        if self.player:
            self.player.draw_me(mainSurface)
        for cloud in self.cloudRenderingList:
            cloud.draw_me(mainSurface)
        for obj in self.objectActiveRenderingList:
            obj.draw_me(mainSurface)
        for obj in self.objectPasiveRenderingList:
            obj.draw_me(menuSurface)

    def esc_buttons_appear(self) -> None:
        for button in self.escButtons:
            button.on()

    def esc_edit_buttons_appear(self) -> None:
        for button in self.escButtons:
            button.on()

    def player_appear(self, settings: Settings, coordinates: tuple) -> None:
        self.player = Player(settings, coordinates)

        self.add_new_object_to_new_list(self.player)
        self.add_new_object_to_event_list(self.player)

    def add_new_object_to_new_list(self, obj: PhysicObject) -> None:
        self.newObjectsList.append(obj)

    def add_new_object_to_pasive_rendering_list(self, obj: PhysicObject) -> None:
        self.objectPasiveRenderingList.append(obj)

    def add_new_object_to_active_rendering_list(self, obj: PhysicObject) -> None:
        self.objectActiveRenderingList.append(obj)

    def add_new_object_to_cloud_rendering_list(self, obj: CloudObject) -> None:
        self.cloudRenderingList.append(obj)

    def add_new_object_to_event_list(self, obj: PhysicObject) -> None:
        self.objectEventList.append(obj)

    def add_new_object_to_collide_list(self, obj: PhysicObject) -> None:
        self.objectCollideList.append(obj)

    def add_new_object_to_field_list(self, obj: GravyObject) -> None:
        self.objectFieldList.append(obj)

    def add_new_object_to_cloud_list(self, obj: CloudObject) -> None:
        self.objectCloudList.append(obj)

    def slice_last_obstraction(self) -> None:
        self.objectActiveRenderingList.pop()
        self.newObjectsList.pop()

    def reset_active_lists(self) -> None:
        self.player = None
        self.objectEventList            = []
        self.objectActiveRenderingList  = []
        self.objectCollideList          = []
        self.objectFieldList            = []
        self.objectCloudList            = []
        self.newObjectsList             = []