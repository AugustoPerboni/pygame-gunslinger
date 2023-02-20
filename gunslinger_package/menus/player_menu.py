import pygame

('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

from gunslinger_package.menus.menu_elements.player_menu_buttons import PlayerUpgradeButton, PlayerLifeButton,PlayerPowerButton,PlayerShootSpeedButton
from gunslinger_package.functions import is_cursor_over

class PlayerMenu:
    def __init__(self):
        self.x = 20
        self.y = 10
        self.hitbox = (self.x,self.y,150,210)

        self.is_menu_selected = False
        self.menu_counter = 0
        self.last_mouse_state = False

        self.upgrade_button = PlayerUpgradeButton()
        self.life_button = PlayerLifeButton()
        self.power_button = PlayerPowerButton()
        self.shoot_speed_button = PlayerShootSpeedButton()

    def draw_menu_button(self,window):
        window.blit(self.upgrade_button.image,(self.upgrade_button.x,self.upgrade_button.y))

    def draw_menu(self,window):
        window.blit(self.life_button.image,(self.life_button.x,self.life_button.y))
        window.blit(self.power_button.image,(self.power_button.x,self.power_button.y))
        window.blit(self.shoot_speed_button.image,(self.shoot_speed_button.x,self.shoot_speed_button.y))
        
    def interaction(self,window):
        pygame.draw.rect(window,(0,0,0),self.hitbox,2)
        # Draw menu or draw menu button --------------------------------------#
        if is_cursor_over(self.upgrade_button) and pygame.mouse.get_pressed()[0]:
            self.is_menu_selected = True

        if self.is_menu_selected:
            self.draw_menu(window)         
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
                    print('Life Button Pressed')
                    self.last_mouse_state = True
                elif is_cursor_over(self.power_button):
                    print('Power Button Pressed')
                    self.last_mouse_state = True
                elif is_cursor_over(self.shoot_speed_button):
                    print('Shoot speed button pressed')
                    self.last_mouse_state = True