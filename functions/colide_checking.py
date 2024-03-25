import pygame as pg
import math as m

from classes.virtualRect import VirtualRect


def colide_checking(dynamicRect: VirtualRect, staticRect: VirtualRect, priviosCoordinates: list) -> str:
    sideList: dict[str, bool] = {"left-collide": False, "right-collide": False, "top-collide": False, "bottom-collide": False}

    
    if (dynamicRect.y + dynamicRect.height >= staticRect.y) and (dynamicRect.y + dynamicRect.height <= staticRect.y + staticRect.height) and (dynamicRect.x + dynamicRect.width >= staticRect.x+5) and (dynamicRect.x <= staticRect.x + staticRect.width-5):
        sideList["top-collide"] = True
    if (dynamicRect.y >= staticRect.y) and (dynamicRect.y <= staticRect.y + staticRect.height) and (dynamicRect.x + dynamicRect.width >= staticRect.x+5) and (dynamicRect.x <= staticRect.x + staticRect.width-5):
        sideList["bottom-collide"] = True
    if (dynamicRect.x + dynamicRect.width >= staticRect.x) and (dynamicRect.x + dynamicRect.width <= staticRect.x + staticRect.width) and (dynamicRect.y + dynamicRect.height >= staticRect.y+5) and (dynamicRect.y <= staticRect.y + staticRect.height-5):
        sideList["left-collide"] = True
    if (dynamicRect.x >= staticRect.x) and (dynamicRect.x <= staticRect.x + staticRect.width) and (dynamicRect.y + dynamicRect.height >= staticRect.y+5) and (dynamicRect.y <= staticRect.y + staticRect.height-5):
        sideList["right-collide"] = True


    trueValue: int = 0
    for value in sideList.values():
        if value:
            trueValue += 1

    if trueValue > 1:
        distanceList: list[float] = []
        dynMiddles: list[tuple[float]] = [
            ((dynamicRect.x+dynamicRect.x+dynamicRect.width)/2, dynamicRect.y), 
            ((dynamicRect.x+dynamicRect.x+dynamicRect.width)/2, dynamicRect.y+dynamicRect.height),
            ((dynamicRect.x), (dynamicRect.y+dynamicRect.y+dynamicRect.height)/2), 
            ((dynamicRect.x+dynamicRect.width), (dynamicRect.y+dynamicRect.y+dynamicRect.height)/2)
            ]
        StatMiddles: list[tuple[float]] = [
            ((staticRect.x+staticRect.x+staticRect.width)/2, staticRect.y), 
            ((staticRect.x+staticRect.x+staticRect.width)/2, staticRect.y+staticRect.height), 
            (staticRect.x, (staticRect.y+staticRect.y+staticRect.height)/2), 
            (staticRect.x+staticRect.width, (staticRect.y+staticRect.y+staticRect.height)/2) 
            ]
        activeSideOfDynamicRect: tuple = ()
        # print(dynamicRect)
        # print(dynMiddles)
        
        distanceList.append(m.sqrt((dynMiddles[0][0]-staticRect.get_center()[0])**2+(dynMiddles[0][1]-staticRect.get_center()[1])**2))
        distanceList.append(m.sqrt((dynMiddles[1][0]-staticRect.get_center()[0])**2+(dynMiddles[1][1]-staticRect.get_center()[1])**2))
        distanceList.append(m.sqrt((dynMiddles[2][0]-staticRect.get_center()[0])**2+(dynMiddles[2][1]-staticRect.get_center()[1])**2))
        distanceList.append(m.sqrt((dynMiddles[3][0]-staticRect.get_center()[0])**2+(dynMiddles[3][1]-staticRect.get_center()[1])**2))

        if min(distanceList) == distanceList[0]:
            # print(0)
            activeSideOfDynamicRect = dynMiddles[0]
        elif min(distanceList) == distanceList[1]:
            # print(1)
            activeSideOfDynamicRect = dynMiddles[1]
        elif min(distanceList) == distanceList[2]:
            # print(2)
            activeSideOfDynamicRect = dynMiddles[2]
        else:
            # print(3)
            activeSideOfDynamicRect = dynMiddles[3]

        distanceList = []

        distanceList.append(m.sqrt((activeSideOfDynamicRect[0]-StatMiddles[0][0])**2+(activeSideOfDynamicRect[1]-StatMiddles[0][1])**2))
        distanceList.append(m.sqrt((activeSideOfDynamicRect[0]-StatMiddles[1][0])**2+(activeSideOfDynamicRect[1]-StatMiddles[1][1])**2))
        distanceList.append(m.sqrt((activeSideOfDynamicRect[0]-StatMiddles[2][0])**2+(activeSideOfDynamicRect[1]-StatMiddles[2][1])**2))
        distanceList.append(m.sqrt((activeSideOfDynamicRect[0]-StatMiddles[3][0])**2+(activeSideOfDynamicRect[1]-StatMiddles[3][1])**2))

        if min(distanceList) == distanceList[0]:
            # print("top-collide")
            return "top-collide"
        elif min(distanceList) == distanceList[1]:
            # print("bottom-collide")
            return "bottom-collide"
        elif min(distanceList) == distanceList[2]:
            # print("left-collide")
            return "left-collide"
        else:
            # print("right-collide")
            return "right-collide"

    else:
        for state in sideList.keys():
            if sideList[state]:
                return state

#---------------------------------------
        


    # point: tuple = (((priviosCoordinates[0]*dynamicRect.y-priviosCoordinates[1]*dynamicRect.x)*(staticRect.x-staticRect.x+staticRect.width)-(priviosCoordinates[0]-dynamicRect.x)*(staticRect.x*staticRect.y+staticRect.height-staticRect.y*staticRect.x+staticRect.width))/((priviosCoordinates[0]-dynamicRect.x)*(staticRect.y-staticRect.y+staticRect.height)-(priviosCoordinates[1]-dynamicRect.y)*(staticRect.x-staticRect.x+staticRect.width)), ((priviosCoordinates[0]*dynamicRect.y-priviosCoordinates[1]*dynamicRect.x)*(staticRect.y-staticRect.y+staticRect.height)-(priviosCoordinates[1]-dynamicRect.y)*(staticRect.x*staticRect.y+staticRect.height-staticRect.y*staticRect.x+staticRect.width))/((priviosCoordinates[0]-dynamicRect.x)*(staticRect.y-staticRect.y+staticRect.height)-(priviosCoordinates[1]-dynamicRect.y)*(staticRect.x-staticRect.x+staticRect.width)))
    # if point[0]>staticRect.x and point[0]<staticRect.x+staticRect.width:
    #     return "top-collide"




    # if staticRect.x > priviosCoordinates[0]+dynamicRect.width:
    #     return "left-collide"
    # if staticRect.x+staticRect.width < priviosCoordinates[0]:
    #     return "right-collide"
    # if staticRect.y > priviosCoordinates[1]+dynamicRect.height:
    #     return "top-collide"
    # if staticRect.y+staticRect.height < priviosCoordinates[1]:
    #     return "bottom-collide"


    # if dynamicRect.clipline((staticRect.x, staticRect.y), (staticRect.x, staticRect.height)):
    #     return "left-collide"
    # if dynamicRect.clipline((staticRect.width, staticRect.y), (staticRect.x, staticRect.height)):
    #     return "right-collide"
    # if dynamicRect.clipline((staticRect.x, staticRect.y), (staticRect.width, staticRect.y)):
    #     return "top-collide"
    # if dynamicRect.clipline((staticRect.x, staticRect.height), (staticRect.width, staticRect.height)):
    #     return "bottom-collide"



    # points: list[float] = []
    # points.append(m.sqrt((dynamicRect.get_center()[0]-staticRect.x)**2 + (dynamicRect.get_center()[1]-staticRect.get_center()[1])**2))
    # points.append(m.sqrt((dynamicRect.get_center()[0]-staticRect.x + staticRect.width)**2 + (dynamicRect.get_center()[1]-staticRect.get_center()[1])**2))
    # points.append(m.sqrt((dynamicRect.get_center()[0]-staticRect.get_center()[0])**2 + (dynamicRect.get_center()[1]-staticRect.y)**2))
    # points.append(m.sqrt((dynamicRect.get_center()[0]-staticRect.get_center()[0])**2 + (dynamicRect.get_center()[1]-staticRect.y + staticRect.width)**2))
   

    # if min(points) == points[0]:
    #     return "left-collide"
    # if min(points) == points[1]:
    #     return "right-collide"
    # if min(points) == points[2]:
    #     return "top-collide"
    # if min(points) == points[3]:
    #     return "bottom-collide"
    

    # if (dynamicRect.x + dynamicRect.width >= staticRect.x) and (dynamicRect.x + dynamicRect.width <= staticRect.x + staticRect.width) and (dynamicRect.y + dynamicRect.height >= staticRect.y+5) and (dynamicRect.y <= staticRect.y + staticRect.height-5):
    #     return "left-collide"
    # if (dynamicRect.x >= staticRect.x) and (dynamicRect.x <= staticRect.x + staticRect.width) and (dynamicRect.y + dynamicRect.height >= staticRect.y+5) and (dynamicRect.y <= staticRect.y + staticRect.height-5):
    #     return "right-collide"
    # if (dynamicRect.y + dynamicRect.height >= staticRect.y) and (dynamicRect.y + dynamicRect.height <= staticRect.y + staticRect.height) and (dynamicRect.x + dynamicRect.width >= staticRect.x+5) and (dynamicRect.x <= staticRect.x + staticRect.width-5):
    #     return "top-collide"
    # if (dynamicRect.y >= staticRect.y) and (dynamicRect.y <= staticRect.y + staticRect.height) and (dynamicRect.x + dynamicRect.width >= staticRect.x+5) and (dynamicRect.x <= staticRect.x + staticRect.width-5):
    #     return "bottom-collide"

