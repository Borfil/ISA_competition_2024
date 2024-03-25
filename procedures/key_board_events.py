import pygame as pg
from pygame.locals import QUIT
import sys

from classes.player import Player
from classes.objectManager import ObjectManager
from classes.blockManager import BlockManager
from classes.keyManager import KeyManager
from classes.settings import Settings


def key_board_events(
        objectManager: ObjectManager, 
        blockManager: BlockManager, 
        keyManager: KeyManager,
        settings: Settings,
        ) -> None:

    
    for event in pg.event.get():
        # (lctrl)
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        
        if event.type == pg.KEYDOWN:

            blockManager.define_current_block(event.key)

            if event.key == pg.K_ESCAPE and keyManager.K_LSHIFT:
                pg.quit()
                sys.exit()
            if event.key == pg.K_ESCAPE:
                if settings.get_active_state():
                    settings.stop()
                    objectManager.esc_buttons_appear()
                elif settings.get_editor_state():
                    settings.editor_off()
                    objectManager.esc_edit_buttons_appear()
                
            
            if settings.get_active_state():
                if event.key == pg.K_a or event.key == pg.K_d:
                    objectManager.player.set_hold_key(event.key)
                if event.key == pg.K_w:
                    objectManager.player.reverse_gravity_derection()
                
            if event.key == pg.K_LCTRL:
                keyManager.K_LCTRL = True
            if event.key == pg.K_LSHIFT:
                keyManager.K_LSHIFT = True

            if event.key == pg.K_s and keyManager.K_LCTRL and settings.get_editor_state():
                blockManager.save_arena(objectManager)
            if event.key == pg.K_o and keyManager.K_LCTRL and settings.get_editor_state():
                arena = input("Enter arena to open: ")
                blockManager.load_arena(objectManager, settings, arena)
            if event.key == pg.K_z and keyManager.K_LCTRL and settings.get_editor_state():
                blockManager.back_for_one_obstraction(objectManager)

            # if event.key == pg.K_o and keyManager.K_LCTRL:
            #     blockManager.load_arena(objectManager)
                
            
      

        elif event.type == pg.KEYUP:
            if settings.get_active_state():
                objectManager.player.clear_hold_key()
            if event.key == pg.K_LCTRL:
                keyManager.K_LCTRL = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if not keyManager.MAUSE:
                if settings.get_editor_state():
                    blockManager.place_block(objectManager, pg.mouse.get_pos(), settings)
                for button, args in objectManager.buttons.items():
                    state = button.click_checking(args)
                    if state:
                        break

            keyManager.MAUSE = True

        elif event.type == pg.MOUSEBUTTONUP:
            keyManager.MAUSE = False

    