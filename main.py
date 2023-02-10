import pygame
from gunslinger_package.config import *
from gunslinger_package.objects_classes.player import Player
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.functions import enemy_player_collision,redraw_game_window,bullet_interaction
from gunslinger_package.loaded_images.background import background

pygame.init
clock = pygame.time.Clock()

game_window = pygame.display.set_mode((window_width,window_hight))

player = Player()
bullets=[]
enemies = []
enemies.append(Enemy(300,2,1,'brown_minotaur')) # Enemy initial position
enemies.append(Enemy(100,5,5,'brown_minotaur'))

# Game main loop
shoot_time_delay = 0
prog_run = True
while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 
    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False

    # Collisions
    bullet_interaction(bullets,enemies,player.power)
    enemy_player_collision(enemies,player)
    player.move(bullets)
    redraw_game_window(background,player,bullets,enemies,game_window)
                


                



