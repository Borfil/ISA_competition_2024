import pygame as pg

class VirtualRect:
    x: float        = 0
    y: float        = 0
    height: int     = 0
    width: int      = 0

    def __init__(self, rect: pg.Rect) -> None:
        self.x = rect.x
        self.y = rect.y
        self.height = rect.height
        self.width = rect.width

    def get_center(self) -> tuple:
        return (self.x+self.width/2, self.y+self.height/2)


    def __repr__(self) -> tuple:
        return f"VirtualRect (x: {round(self.x, 1)}, y: {round(self.y, 1)}, width: {round(self.width, 1)}, height: {round(self.height, 1)})"

    
