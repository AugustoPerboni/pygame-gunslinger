import pygame

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.objects_classes.element import Element
from gunslinger_package.loaded_images.turret_images import *
from gunslinger_package.config import window_width
from gunslinger_package.objects_classes.projectile import Projectile
from gunslinger_package.loaded_images.menu_images import upgrade_button
from gunslinger_package.functions import create_font



class Turret(Element):
    
    def __init__(self,x):

        Element.__init__(self,x,570,128,128,0.25,20)
        self.level = 1
        self.turret_top = turret_lvl1_top
        self.turret_base = turret_lvl1_base
        self.bullets = []
        self.is_shooting = False
        self.range = window_width / 4
        self.shoot_time_delay = 0
        self.life_bar_x = x
        self.life_bar_y = 545
        self.hitbox = (self.x,self.y-80,100,90)
        self.update_price = 75
        self.mouse_count = 0

    def level_update(self):
        if self.level == 1:
            self.turret_top = turret_lvl2_top
            self.turret_base = turret_lvl2_base
            self.power = 30
            self.velocity = 0.5
            self.range = window_width / 2
            self.update_price = 150
            self.level += 1
        elif self.level == 2:
            self.turret_top = turret_lvl3_top
            self.turret_base = turret_lvl2_base
            self.power = 40
            self.velocity = 0.75
            self.range = window_width
            self.update_price = 250
            self.level += 1
        elif self.level == 3:
            self.turret_top = turret_lvl4_top
            self.turret_base = turret_lvl4_base
            self.power = 50
            self.velocity = 1
            self.range = 2 * window_width 
            self.level += 1

    def draw(self,window,turrets,enemies): 
        if self.life <= 0:               
            for enemy in enemies:
                if  self.hitbox[0] < enemy.hitbox[0] <= self.hitbox[0] + self.hitbox[2]:
                    enemy.is_hitting = False
                    enemy.walk_left = True
            del turrets[turrets.index(self)]     
            
        # pygame.draw.rect(window,(255,0,0),self.hitbox,2)
        window.blit(self.turret_base, (self.x,self.y))
        window.blit(self.turret_top, (self.x,self.y))
        self.life_bar(window)

    def draw_menu_update(self,window,font_size,player):
        ''' Draw the turret update menu and check if the player has enough money and 
        pressed the update button the level of the turret is increased. '''
        window.blit(upgrade_button,(self.x, self.y - 80))
        # pygame.draw.rect(window,(0,0,0),(self.x + 5,self.y- 75,40,40),2)
        font = create_font(font_size)
        text = font.render(str(self.update_price),1,(0,255,0))
        window.blit(text,(self.x + 50,self.y - 70 ))
        # Check if the player pressed the mouse to update the turret
        if self.mouse_count >= 5:
            self.mouse_count = 0
        elif self.mouse_count > 0:
            self.mouse_count += 1
        if pygame.mouse.get_pressed()[0] and self.mouse_count == 0 and player.money >= self.update_price:
            # The cursor should be over the update arrow
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (self.x + 5 < mouse_x < self.x +45) and (self.y - 75 < mouse_y < self.y - 45):
                self.mouse_count += 1
                player.money -= self.update_price
                self.level_update()


    def enemy_in_range(self,enemies):
        ''' Check if there is any enemy in turret's shooting range '''
        enemy_close = False
        for enemy in enemies:
            if abs(self.x - enemy.x):
                enemy_close = True
        if enemy_close:
            self.is_shooting = True
        else:
            self.is_shooting = False
    
    def shoot(self,enemies):
        self.enemy_in_range(enemies)

        if self.is_shooting and self.shoot_time_delay == 0:
            bullet = Projectile(self.x,self.y,1)
            bullet.hitbox = (self.x + 115 ,self.y + 7 ,20,10)
            self.bullets.append(bullet)
        
        if self.shoot_time_delay >= (25 / self.velocity):
            self.shoot_time_delay = 0
        else:
            self.shoot_time_delay += 1
        #print(self.shoot_time_delay)
    def hit(self,power):
        self.life -= power*10 
        print('Turret hit')
