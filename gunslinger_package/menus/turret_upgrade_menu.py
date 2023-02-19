import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

from gunslinger_package.menus.menu_elements.upgrade_button import UpgradeButton



class TurretMenu:
    ''' Creates a menu for every turret type element.'''
    def __init__(self):            
        self.upgrade_button = UpgradeButton(0,0)
        # Import placed inside __init__ to prevent circular imports
        from gunslinger_package.functions import create_font
        self.font = create_font(30)
        self.last_mouse_state = False

    def draw(self,turret,window):
        if turret.level <= 3:
            # Update properties ----------------------------------------------#
            self.upgrade_button.x = turret.x
            self.upgrade_button.y = turret.y
            self.upgrade_button.hitbox = (turret.x,turret.y - 78,self.upgrade_button.hitbox[2],self.upgrade_button.hitbox[3])
            # Print elements in game window -----------------------------------#
            window.blit(self.upgrade_button.image,(turret.x, turret.y - 80))
            text = self.font.render(str(turret.update_price),1,(0,255,0))
            window.blit(text,(turret.x + 50,turret.y - 70 ))
            # pygame.draw.rect(window,(0,0,0),self.upgrade_button.hitbox,2)

    def interaction(self,turret,window,player):
        self.draw(turret,window)
        
        # Import placed inside interaction to prevent circular imports
        from gunslinger_package.functions import is_cursor_over

        if not pygame.mouse.get_pressed()[0] :
            self.last_mouse_state = False
        if pygame.mouse.get_pressed()[0] and not(self.last_mouse_state) and player.money >= turret.update_price:
                
                self.last_mouse_state = True
                if is_cursor_over(self.upgrade_button):
                    player.money -= turret.update_price
                    turret.level_update()

