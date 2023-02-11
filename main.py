import pygame

from gunslinger_package.config import window_hight,window_width
from gunslinger_package.objects_classes.player import Player
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.functions import enemy_player_collision,redraw_game_window,bullet_interaction,wave_generator
from gunslinger_package.loaded_images.background import background
from gunslinger_package.loaded_images.brown_minotaur_images import brown_minotaur_images

# import time

pygame.init
clock = pygame.time.Clock()

game_window = pygame.display.set_mode((window_width,window_hight))

player = Player()
bullets=[]
enemies = []   
wave_number = 0
enemies.append(Enemy(window_width,2,1,brown_minotaur_images,'brown_minotaur')) # Enemy initial position
# enemies.append(Enemy(window_width + 500,5,5,brown_minotaur_images,'brown_minotaur'))

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

    # if len(enemies) == 0:
    #     wave_number += 1
    #     print(f'Wave numero: {wave_number}')
    #     wave_generator(enemies,wave_number)


    bullet_interaction(bullets,enemies,player.power)
    enemy_player_collision(enemies,player)
    player.move(bullets)
    origin_background = redraw_game_window(background,player,bullets,enemies,game_window,end_of_screen,origin_background)
    

    

                



