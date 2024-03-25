import pygame as pg
import json


from classes.objectManager import ObjectManager
from classes.settings import Settings


from classes.levelDesignObjects.block import Block
from classes.levelDesignObjects.deadBlock import DeadBlock
from classes.levelDesignObjects.vinBlock import VinBlock

from classes.levelDesignObjects.orangeOrb import OrangeOrb
from classes.levelDesignObjects.blueOrb import BlueOrb

from classes.levelDesignObjects.greenCloud import GreenCloud
from classes.levelDesignObjects.brownCloud import BrownCloud
from classes.levelDesignObjects.greyCloud import GreyCloud
from classes.levelDesignObjects.purpleCloud import PurpleCloud


from classes.physicObject import PhysicObject
from classes.player import Player



class BlockManager:
    currentBlock: int   = pg.K_1
    obstractions: dict  = { 
                            pg.K_1: Block, 
                            pg.K_2: DeadBlock,
                            pg.K_3: Player,
                            pg.K_4: VinBlock,
                            pg.K_5: OrangeOrb,
                            pg.K_6: BlueOrb,
                            pg.K_7: GreenCloud,
                            pg.K_8: PurpleCloud,
                            pg.K_9: GreyCloud,
                          }


    def define_current_block(self, key: int) -> None:
        if key in self.obstractions:
            self.currentBlock = key

    def place_block(self, objectManager: ObjectManager, mousePosition: tuple, settings: Settings) -> None:
        if self.obstractions[self.currentBlock] == Player:
            obj: PhysicObject = self.obstractions[self.currentBlock](settings, ((mousePosition[0]//20)*20, (mousePosition[1]//20)*20))
        else:
            obj: PhysicObject = self.obstractions[self.currentBlock](((mousePosition[0]//20)*20, (mousePosition[1]//20)*20))


        objectManager.add_new_object_to_active_rendering_list(obj)
        objectManager.add_new_object_to_new_list(obj)
    
    def back_for_one_obstraction(self, objectManager: ObjectManager) -> None:
        objectManager.slice_last_obstraction()
        
    def save_arena(self, objectManager: ObjectManager) -> None:
        arena = input("Enter arena name: ")
        try:
            with open(f"dataBase/{arena}.json") as file:
                testArena: dict[str, list] = json.load(file)

            testArena["obstractions"] = []
        except:
            testArena: dict[str, list[float]] = {}
            testArena["obstractions"] = []
        

        for obj in objectManager.newObjectsList:
            testArena["obstractions"].append([obj.__class__.__name__, [obj.virtualRect.x, obj.virtualRect.y]])

        with open(f"dataBase/{arena}.json", "w") as file:
            json.dump(testArena, file)


    def load_arena(self, objectManager: ObjectManager, settings: Settings, arena: str) -> None:
        with open(f"dataBase/{arena}.json") as file:
            testArena = json.load(file)

        objectManager.reset_active_lists()
        for obj in testArena["obstractions"]:
            if obj[0] == "Player":
                objectManager.player_appear(settings, (obj[1][0], obj[1][1]))
                
            else:
                block: object = objectManager.objectTypeDict[obj[0]]((obj[1][0], obj[1][1]))
                if obj[0] == "OrangeOrb" or obj[0] == "BlueOrb":
                    objectManager.add_new_object_to_field_list(block)
                elif obj[0] == "GreenCloud" or obj[0] == "BrownCloud" or obj[0] == "PurpleCloud" or obj[0] == "GreyCloud":
                    objectManager.add_new_object_to_cloud_list(block)
                else:
                    objectManager.add_new_object_to_collide_list(block)
                
                objectManager.add_new_object_to_new_list(block)
                objectManager.add_new_object_to_active_rendering_list(block)
                objectManager.add_new_object_to_event_list(block)

        self.adge_generate(objectManager, settings)

    def adge_generate(self, objectManager: ObjectManager, settings: Settings) -> None:
        row = colom = 0
        for row in range(settings.get_surface_size()[1]//20):
            for colom in range(settings.get_surface_size()[0]//20):
                if row < 13 or row > 46 or colom < 13 or colom > 46:
                    block = Block((colom*20-60, row*20-240))
                    
                    objectManager.add_new_object_to_collide_list(block)
                    objectManager.add_new_object_to_active_rendering_list(block)
                    objectManager.add_new_object_to_event_list(block)




        


