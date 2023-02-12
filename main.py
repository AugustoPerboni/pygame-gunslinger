import pygame

from gunslinger_package.config import window_hight,window_width
from gunslinger_package.objects_classes.player import Player
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.functions import enemy_player_collision,redraw_game_window,bullet_interaction,wave_generator, enemy_turret_collision, show_money
from gunslinger_package.loaded_images.background import background
from gunslinger_package.loaded_images.brown_minotaur_images import brown_minotaur_images

# import time

pygame.init
pygame.font.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 45, True)

game_window = pygame.display.set_mode((window_width,window_hight))

player = Player()
bullets=[]
enemies = []   
turrets = []
wave_number = 1


# Game main loop
shoot_time_delay = 0
prog_run = True
end_of_screen = window_width
origin_background = (0,0)

while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 
    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False
    keys = pygame.key.get_pressed()

    if len(enemies) == 0:
        wave_number += 1
        print(f'Wave numero: {wave_number}')
        wave_generator(enemies,wave_number)

    
    [turret.shoot(enemies) for turret in turrets]
    [bullet_interaction(turret.bullets,enemies,turret.power,origin_background ) for turret in turrets]

    bullet_interaction(bullets,enemies,player.power,origin_background)
    
    enemy_player_collision(enemies,player)
    player.move(bullets,turrets,keys)
    enemy_turret_collision(enemies,turrets)
    show_money(player,game_window,font)


    origin_background = redraw_game_window(background,player,bullets,enemies,game_window,end_of_screen,origin_background,turrets,keys,font)

    
    
    

    

                



