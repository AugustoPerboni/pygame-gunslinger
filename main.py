import pygame
from pygame.locals import *

from gunslinger_package.config import window_hight,window_width
from gunslinger_package.objects_classes.player import Player
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.functions import enemy_player_collision,redraw_game_window,bullet_interaction,wave_generator, enemy_turret_collision, show_money, turret_menu_interaction
from gunslinger_package.loaded_images.background import background
from gunslinger_package.menus.turret_upgrade_menu import TurretMenu

# Inicializations ------------------------------------------------------------ #
pygame.init
pygame.font.init()
game_window = pygame.display.set_mode((window_width,window_hight))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 45, True)

# Objects with interactions
player = Player()
bullets=[]
enemies = []   
turrets = []

# Variables
wave_number = 0
prog_run = True
origin_background = (0,0)
shoot_time_delay = 0

# Menus
turret_menu = TurretMenu()

# Game main loop -------------------------------------------------------------#
while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 
    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False
    keys = pygame.key.get_pressed()

    # Wave generation --------------------------------------------------------#
    if len(enemies) == 0:
        wave_number += 1
        print(f'Wave numero: {wave_number}')
        wave_generator(enemies,wave_number)

    # Collisions -------------------------------------------------------------#
    [turret.shoot(enemies) for turret in turrets]
    [bullet_interaction(turret.bullets,enemies,turret.power,origin_background ) for turret in turrets]
    bullet_interaction(bullets,enemies,player.power,origin_background)
    enemy_player_collision(enemies,player)
    enemy_turret_collision(enemies,turrets)

    


    player.move(bullets,turrets,keys)
    show_money(player,game_window)

    # Draw window ------------------------------------------------------------#
    origin_background = redraw_game_window(background,player,bullets,enemies,game_window,window_width,origin_background,turrets,keys,font)

        # Mouse interactions and menu draws-----------------------------------#
    turret_menu_interaction(turrets,player,game_window,turret_menu)

    # Update display ---------------------------------------------------------#
    pygame.display.update()
    
     
    

    

                



