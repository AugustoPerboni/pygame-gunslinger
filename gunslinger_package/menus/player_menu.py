import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

from gunslinger_package.menus.menu_elements.player_menu_buttons import PlayerUpgradeButton, PlayerLifeButton,PlayerPowerButton,PlayerShootSpeedButton
from gunslinger_package.functions import is_cursor_over
from gunslinger_package.functions import create_font

class PlayerMenu:
    def __init__(self):
        self.x = 25
        self.y = 15
        self.hitbox = (self.x - 5 ,self.y - 5, 155, 215)

        self.is_menu_selected = False
        self.menu_counter = 0
        self.last_mouse_state = False

        self.upgrade_button = PlayerUpgradeButton()
        self.life_button = PlayerLifeButton()
        self.power_button = PlayerPowerButton()
        self.shoot_speed_button = PlayerShootSpeedButton()
        self.font = create_font(30)

    def draw_menu_button(self,window):
        window.blit(self.upgrade_button.image,(self.upgrade_button.x,self.upgrade_button.y))

    def draw_menu(self,window,player):
        window.blit(self.life_button.image,(self.x,self.y))
        text = self.font.render('$' + str(player.life_update_price),1,(0,255,0))
        window.blit(text,(self.x + 65, self.y + 15))
        
        window.blit(self.power_button.image,(self.x,self.y + 64))
        text = self.font.render('$' + str(player.power_update_price),1,(0,255,0))
        window.blit(text,(self.x + 65, self.y + 79))

        window.blit(self.shoot_speed_button.image,(self.x - 1,self.y + 128))
        text = self.font.render('$' + str(player.shoot_speed_update_price),1,(0,255,0))
        window.blit(text,(self.x + 65, self.y + 143))
        
    def interaction(self,window,player):
        # pygame.draw.rect(window,(0,0,0),self.hitbox,1)
        # Draw menu or draw menu button --------------------------------------#
        if is_cursor_over(self.upgrade_button) and pygame.mouse.get_pressed()[0]:
            self.is_menu_selected = True

        if self.is_menu_selected:
            self.draw_menu(window,player)         
        else:
            self.draw_menu_button(window)
            
        # Keeps the menu printed until the cursor gets out of range
        if self.is_menu_selected and not is_cursor_over(self):
            self.is_menu_selected = False
            self.menu_counter = 0
            self.last_mouse_state = False

        # User menu interaction ----------------------------------------------#
        if self.is_menu_selected:
            if self.menu_counter < 10:
                self.menu_counter += 1

            if not pygame.mouse.get_pressed()[0]:
                self.last_mouse_state = False
            if pygame.mouse.get_pressed()[0] and self.menu_counter == 10 and not self.last_mouse_state:

                if is_cursor_over(self.life_button):
                    self.last_mouse_state = True
                    player.life_update()
                elif is_cursor_over(self.power_button):
                    player.power_update()
                    self.last_mouse_state = True
                elif is_cursor_over(self.shoot_speed_button):
                    player.shoot_speed_update()
                    self.last_mouse_state = True
