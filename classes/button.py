import pygame as pg

from classes.settings import Settings

class Button:
    image: pg.Surface           = None
    originaleImage: pg.Surface  = None
    rect: pg.Rect               = None
    originalRect: pg.Rect        = None
    scaleSize: int              = 0
    settings: Settings          = None
    active: bool                = False
    toActiveButtons: list       = []
    toPassiveButtons: list      = []
    

    def __init__(self, settings: Settings, rect: tuple[int]) -> None:
        self.originaleImage = self.image
        self.rect = self.image.get_rect()

        self.originalRect = []
        
        self.settings = settings
        self.rect.x = rect[0]+60-self.rect.width/2
        self.rect.y = rect[1]+240-self.rect.height/2

        self.originalRect.append(self.rect.x); self.originalRect.append(self.rect.y)

    def update(self) -> None:
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint((mouse[0]+60, mouse[1]+240)) and self.active:
            if self.scaleSize <= 5:
                self.scaleSize += 1
                self.image = pg.transform.smoothscale(self.originaleImage, (self.rect.width+self.scaleSize, self.rect.height+self.scaleSize))
                self.rect.x = self.originalRect[0]-self.scaleSize/2
                self.rect.y = self.originalRect[1]-self.scaleSize/2
        else:
            if self.scaleSize > 0: 
                self.scaleSize -= 1
                self.image = pg.transform.smoothscale(self.originaleImage, (self.rect.width+self.scaleSize, self.rect.height+self.scaleSize))
                self.rect.x = self.originalRect[0]-self.scaleSize/2
                self.rect.y = self.originalRect[1]-self.scaleSize/2
            

    def fill_lists(self, toPassiveButtons: list, toActiveButtons: list) -> None:
        self.toActiveButtons = []
        self.toPassiveButtons = []

        for button in toActiveButtons:
            if type(button) == list:
                for but in button:
                    self.toActiveButtons.append(but)
            else:
                self.toActiveButtons.append(button)

        for button in toPassiveButtons:
            if type(button) == list:
                for but in button:
                    self.toPassiveButtons.append(but)
            else:
                self.toPassiveButtons.append(button)




    def click_checking(self, args: dict[str]) -> bool:
        mouse = pg.mouse.get_pos()
        if self.rect.collidepoint((mouse[0]+60, mouse[1]+240)) and self.active:
            self.click_event(args)
            return True
        return False

    def button_arranging(self) -> None:
        
        for button in self.toActiveButtons:
            button.on()

        for button in self.toPassiveButtons:
            button.off()

        self.off()

    def off(self) -> None:
        self.active = False
        
    def on(self) -> None:
        self.active = True

    def draw_me(self, screen: pg.Surface) -> None:
        if self.active:
            self.rect.x -= 60
            self.rect.y -= 240
            screen.blit(self.image, self.rect)
            self.rect.x += 60
            self.rect.y += 240


    

