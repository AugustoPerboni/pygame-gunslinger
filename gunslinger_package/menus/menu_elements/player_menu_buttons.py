import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')
from gunslinger_package.menus.menu_elements.button import Button
from gunslinger_package.loaded_images.menu_images import player_update_button_image, player_life_button_image,player_power_button_image,player_shoot_speed_button_image

# Button.__init__ args = (self,x,y,hitbox_width,hitbox_height,image)

class PlayerUpgradeButton(Button):
    def __init__(self):
        Button.__init__(self,25,15,55,64,player_update_button_image)
        
class PlayerLifeButton(Button):
    def __init__(self):
        Button.__init__(self,25,15,55,64,player_life_button_image)

class PlayerPowerButton(Button):
    def __init__(self):
        Button.__init__(self,25,79,55,64,player_power_button_image)

class PlayerShootSpeedButton(Button):
    def __init__(self):
        Button.__init__(self,24,145,55,64,player_shoot_speed_button_image)
