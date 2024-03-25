import math as m

from classes.virtualRect import VirtualRect


def distance_checking(firstVirtual: VirtualRect, secondVirtual: VirtualRect, distance: float) -> bool:  
    if m.sqrt((firstVirtual.x - secondVirtual.x)**2 + (firstVirtual.y - secondVirtual.y)**2) <= distance:
        return True