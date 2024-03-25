import pygame as pg
import numpy as np
import math as m

from classes.virtualRect import VirtualRect
from classes.settings import Settings
from classes.physicObject import PhysicObject

from classes.levelDesignObjects.block import Block

from functions.colide_checking import colide_checking


class Player(PhysicObject):
    image: pg.Surface           = pg.image.load("images/SLGCI_Sprite.png")
    mask: pg.Mask               = pg.mask.from_surface(image)
    rect: pg.Rect               = image.get_rect()
    virtualRect: VirtualRect    = VirtualRect(rect)
    priviosCoordinates: list    = [0, 0]
    checkPoint: tuple           = ()
    totalForse: np.ndarray[any] = np.array([0, 0])
    gravityConstant: float      = 0.1
    gravityAct: np.ndarray[any] = np.array([0, gravityConstant])
    bounceKoefitient:float      = 0.1
    orientationList: list[str]  = []
    effectList: list[float]     = []
    currentEffect: float        = 1
    alpha: int                  = 0
    holdKey: int                = 0
    passed: bool                = False

    settings: Settings          = None


    def __init__(self, settings: Settings, coordinates: tuple) -> None:
        self.virtualRect.x = coordinates[0]
        self.virtualRect.y = coordinates[1]

        self.rect.x = self.virtualRect.x
        self.rect.y = self.virtualRect.y

        self.gravityAct: np.ndarray[any] = np.array([0, self.gravityConstant])

        self.checkPoint = coordinates

        self.settings = settings


    def update(self, wall: Block) -> None:

        self.gravity_direction_change()
        self.effect_calculating()

        self.totalForse = self.totalForse + self.gravityAct*self.currentEffect


        self.collide_event(wall)

        self.priviosCoordinates[0] = self.virtualRect.x
        self.priviosCoordinates[1] = self.virtualRect.y

        self.virtualRect.x += self.totalForse[0]
        self.virtualRect.y += self.totalForse[1]

        self.rect.x = self.virtualRect.x
        self.rect.y = self.virtualRect.y

        self.currentEffect = 1


    def collide_event(self, objectCollideList: list[PhysicObject]) -> None:

        
        for obj in objectCollideList:
            if self.rect.colliderect(obj.rect):
                orientation = colide_checking(self.virtualRect, obj.virtualRect, self.priviosCoordinates)

                if orientation:
                    if obj.__class__.__name__ == "DeadBlock":
                        self.death()
                        continue
                    elif obj.__class__.__name__ == "VinBlock":
                        self.passed = True
                        continue

                if orientation == "left-collide":
                    self.virtualRect.x = obj.virtualRect.x - self.virtualRect.width
                    # self.totalForse -= np.array([self.gravityConstant, 0])
                    self.totalForse[0] = -self.totalForse[0]*self.bounceKoefitient

                elif orientation == "right-collide":
                    self.virtualRect.x = obj.virtualRect.x + obj.virtualRect.width
                    # self.totalForse += np.array([self.gravityConstant, 0])
                    self.totalForse[0] = -self.totalForse[0]*self.bounceKoefitient

                elif orientation == "top-collide":
                    self.virtualRect.y = obj.virtualRect.y - self.virtualRect.height 
                    # self.totalForse -= np.array([0, self.gravityConstant])
                    self.totalForse[1] = -self.totalForse[1]*self.bounceKoefitient

                elif orientation == "bottom-collide":
                    self.virtualRect.y = obj.virtualRect.y + obj.virtualRect.height 
                    # self.totalForse += np.array([0, self.gravityConstant])
                    self.totalForse[1] = -self.totalForse[1]*self.bounceKoefitient

    
    def gravity_direction_change(self) -> None:
        if self.holdKey == pg.K_a:
            self.alpha -= m.radians(self.settings.rotateKoeficient)
            self.settings.change_the_rotate_angle(-self.settings.rotateKoeficient)

            self.gravityAct[1] = (self.gravityConstant * m.cos(self.alpha))
            self.gravityAct[0] = (self.gravityConstant * m.sin(self.alpha))
            
        elif self.holdKey == pg.K_d:
            self.alpha += m.radians(self.settings.rotateKoeficient)
            self.settings.change_the_rotate_angle(self.settings.rotateKoeficient)

            self.gravityAct[1] = (self.gravityConstant * m.cos(self.alpha))
            self.gravityAct[0] = (self.gravityConstant * m.sin(self.alpha))


    def reverse_gravity_derection(self) -> None:
        self.alpha += m.radians(180)
        self.settings.change_the_rotate_angle(180)

        self.gravityAct[1] = (self.gravityConstant * m.cos(self.alpha))
        self.gravityAct[0] = (self.gravityConstant * m.sin(self.alpha))

    def addition_force_impact(self, objectsVirtual: VirtualRect, attractionStrength: float) -> None:
        yTerm = self.virtualRect.y-objectsVirtual.y
        xTerm = self.virtualRect.x-objectsVirtual.x
        sign = -1

        alpha = m.atan((yTerm)/(xTerm))
        if yTerm < 0 and xTerm > 0 or yTerm > 0 and xTerm > 0:
            sign = 1

        # print(sign)

        x = attractionStrength*m.cos(alpha)*sign
        y = attractionStrength*m.sin(alpha)*sign

        self.totalForse -= np.array([x, y])

    def effect_calculating(self) -> None:
        for effect in self.effectList:
            if effect >= 0:
                self.currentEffect *= effect

        if self.effectList and min(self.effectList) < 0:
            self.currentEffect *= -1

        self.effectList = []

    def death(self) -> None:
        self.virtualRect.x = self.checkPoint[0]
        self.virtualRect.y = self.checkPoint[1]
        self.totalForse[0] = self.totalForse[1] = 0
            
            
    def set_hold_key(self, key: int) -> None:
        self.holdKey = key

    def clear_hold_key(self) -> None:
        self.holdKey = None

    def add_effect(self, effect: float) -> None:
        self.effectList.append(effect)
