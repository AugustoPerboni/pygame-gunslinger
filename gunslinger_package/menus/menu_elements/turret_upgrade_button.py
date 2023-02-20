import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

from gunslinger_package.loaded_images.menu_images import turret_upgrade_button as update_button_image
from gunslinger_package.menus.menu_elements.button import Button

class UpgradeButton(Button):
    ''' Define the upgrate button.'''

    def __init__(self,x,y):
        # hitbox width = 50
        # hitbox height = 45
        Button.__init__(self,x,y,50,45,update_button_image)

    def draw_hitbox(self,window):
        pygame.draw.rect(window,(0,0,0),self.draw_hitbox,2)