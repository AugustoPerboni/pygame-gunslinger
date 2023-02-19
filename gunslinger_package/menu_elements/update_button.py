import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.loaded_images.menu_images import upgrade_button as update_button_image
from gunslinger_package.menu_elements.button import Button

class UpdateButton(Button):
    '''Define the update button element.'''
    def __init__(self,x,y):
        Button.init(x,y,40,30,update_button_image)

    def draw_hitbox(self,window):
        pygame.draw.rect(window,(0,0,0),self.draw_hitbox,2)