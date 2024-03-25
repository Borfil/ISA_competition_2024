from tkinter import Button
from classes.blockManager import BlockManager

from classes.buttons.continueEdit import ContinueEditButton
from classes.objectManager import ObjectManager
from classes.settings import Settings

from classes.buttons.play import PlayButton
from classes.buttons.exit import ExitButton
from classes.buttons.back import BackButton
from classes.buttons.level import LevelButton
from classes.buttons.mainMenu import MainMenuButton
from classes.buttons.continuePlay import ContinuePlayButton
from classes.buttons.editor import EditorButton
from classes.buttons.passedButton import PassedButton



def buttons_create(settings: Settings, blockManager: BlockManager, objectManager: ObjectManager) -> list[list]:
    buttonList: list[list[Button]] = []
    screenSize: list[int] = settings.get_screen_size()
    

    buttonList.append([PlayButton(settings, (screenSize[0]/2, screenSize[1]/2-85)), {}])
    buttonList.append([ExitButton(settings, (screenSize[0]/2, screenSize[1]/2+35)), {}])
    buttonList.append([BackButton(settings, (screenSize[0]/2, screenSize[1]/2+60)), {}])
    buttonList.append([MainMenuButton(settings, (screenSize[0]/2, screenSize[1]/2-100)), {"objectManager": objectManager, "settings": settings}])
    buttonList.append([ContinuePlayButton(settings, (screenSize[0]/2, screenSize[1]/2-160)), {"settings": settings}])
    buttonList.append([EditorButton(settings, (screenSize[0]/2, screenSize[1]/2-25)), {"objectManager": objectManager, "settings": settings, "blockManager": blockManager}])
    buttonList.append([PassedButton(settings, (screenSize[0]/2, screenSize[1]/2-25)), {"objectManager": objectManager, "settings": settings}])
    buttonList.append([ContinueEditButton(settings, (screenSize[0]/2, screenSize[1]/2-160)), {"settings": settings}])

    positionX = screenSize[0]/2-120
    positionY = screenSize[1]/2-120
    index = 1
    for row in range(2):
        for colom in range(5):
            buttonList.append([LevelButton(settings, (positionX, positionY), f"level_{index}"), {"blockManager": blockManager, "objectManager": objectManager, "settings": settings}])
            positionX += 60
            index += 1
        positionY += 60
        positionX = screenSize[0]/2-120

    levels: list = [buttonList[8][0], buttonList[9][0], buttonList[10][0], buttonList[11][0], buttonList[12][0], 
                    buttonList[13][0], buttonList[14][0], buttonList[15][0], buttonList[16][0], buttonList[17][0]]


    buttonList[0][0].fill_lists([buttonList[1][0], buttonList[5][0]], [buttonList[2][0], levels])
    buttonList[2][0].fill_lists([levels], [buttonList[1][0], buttonList[0][0], buttonList[5][0]])
    buttonList[3][0].fill_lists([buttonList[4][0]], [buttonList[0][0], buttonList[1][0], buttonList[5][0]])
    buttonList[4][0].fill_lists([buttonList[3][0]], [])
    buttonList[5][0].fill_lists([buttonList[0][0], buttonList[1][0]], [])
    buttonList[6][0].fill_lists([], [buttonList[0][0], buttonList[1][0], buttonList[5][0]])
    buttonList[7][0].fill_lists([buttonList[3][0]], [])
    for button in buttonList[8:]:
        button[0].fill_lists([levels, buttonList[2][0]], [])


    '''
    buttonList [
        00: PlayButton
        01: ExitButton
        02: BackButton
        03: MainMenuButton
        04: ContinuePlayButton
        05: EditorButton
        06: PassedButton
        07: ContinueEditButton
        08-17: LevelButton(level_1-level_10)
    ]
    '''

    return buttonList