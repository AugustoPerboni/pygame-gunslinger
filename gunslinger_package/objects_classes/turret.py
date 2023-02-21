from gunslinger_package.functions import create_font
from gunslinger_package.loaded_images.menu_images import turret_upgrade_button
from gunslinger_package.objects_classes.projectile import Projectile
from gunslinger_package.config import window_width
from gunslinger_package.loaded_images.effects_images import image_turret_bullet
from gunslinger_package.loaded_images.turret_images import *
from gunslinger_package.objects_classes.element import Element
import pygame

import sys
sys.path.append(
    'C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

#from gunslinger_package.menu_elements.update_button import UpdateButton


class Turret(Element):

    def __init__(self, x):

        Element.__init__(self, x, 570, 128, 128, 0.25, 30)
        self.level = 1
        self.turret_top = turret_lvl1_top
        self.turret_base = turret_lvl1_base
        self.bullets = []
        self.is_shooting = False
        self.range = window_width / 4
        self.shoot_time_delay = 0
        self.life_bar_x = x
        self.life_bar_y = 545
        self.hitbox = (self.x, self.y-75, 100, 170)
        self.update_price = 75
        self.mouse_count = 0

        self.image_bullet = image_turret_bullet
        self.shoot_sound = pygame.mixer.Sound('sounds\\turret_lvl1_shoot.wav')

    def level_update(self):
        if self.level == 1:
            self.turret_top = turret_lvl2_top
            self.turret_base = turret_lvl2_base
            self.power = 30
            self.velocity = 0.5
            self.range = window_width / 2
            self.update_price = 150
            self.level += 1
            self.shoot_sound = pygame.mixer.Sound(
                'sounds\\turret_lvl2_shoot.wav')
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
            self.shoot_sound = pygame.mixer.Sound(
                'sounds\\turret_lvl4_shoot.wav')

    def draw(self, window, turrets, enemies):
        if self.life <= 0:
            for enemy in enemies:
                if self.hitbox[0] < enemy.hitbox[0] <= self.hitbox[0] + self.hitbox[2]:
                    enemy.is_hitting = False
                    enemy.walk_left = True
            del turrets[turrets.index(self)]

        # pygame.draw.rect(window,(255,0,0),self.hitbox,2)
        window.blit(self.turret_base, (self.x, self.y))
        window.blit(self.turret_top, (self.x, self.y))
        self.life_bar(window)

    def enemy_in_range(self, enemies):
        ''' Check if there is any enemy in turret's shooting range '''
        enemy_close = False
        for enemy in enemies:
            if abs(self.x - enemy.x) < self.range:
                enemy_close = True
        if enemy_close:
            self.is_shooting = True
        else:
            self.is_shooting = False

    def shoot(self, enemies):
        self.enemy_in_range(enemies)

        if self.is_shooting and self.shoot_time_delay == 0:
            bullet = Projectile(self.x + 2, self.y + 4, 1, self.image_bullet)
            bullet.hitbox = (self.x + 115, self.y + 7, 20, 10)
            self.shoot_sound.play()
            self.bullets.append(bullet)

        if self.shoot_time_delay >= (25 / self.velocity):
            self.shoot_time_delay = 0
        else:
            self.shoot_time_delay += 1

    def hit(self, power):
        self.life -= power*10/self.level

    def window_half_correction(self, player):
        if player.in_window_second_half:
            self.x -= window_width
            self.hitbox = (self.x, self.y-75, 100, 170)
            self.life_bar_x = self.x
            for bullet in self.bullets:
                bullet.x -= window_width
        else:
            self.x += window_width
            self.hitbox = (self.x, self.y-75, 100, 170)
            self.life_bar_x = self.x
            for bullet in self.bullets:
                bullet.x = window_width
